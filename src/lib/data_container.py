import os
import csv

import pandas
import numpy

from config import PATH, COL_NAMES_FULL, COL_NAMES, COL_TYPES, COL_CONVERTERS, convert_zip_code, convert_year, convert_amount
from lib.decorate import record_elapsed_time

def row_string_to_row(row_string):
	""" Takes in a single line (string) and converts it to a 'row' for the dataframe """
	row_list = row_string.split('|')
	# probably not necessary:
	for val in row_list:
		val = val.strip()
	# if the transaction is from an entity, return False to show row invalid
	if row_list[15] != '':
		return (False, None)
	# restrict to just the columns we want
	row = {
		'recipient': row_list[0],
		'donor': row_list[7],
		'zip-code': convert_zip_code(row_list[10]),
		'year': convert_year(row_list[13]),
		'amount': convert_amount(row_list[14]),
	}
	return (True, row)

def ordinal_rank_percentile(percentile, lis):
	if percentile <= 0 or percentile > 100:
		raise ValueError('Percentile P must satisfy 0 < P <= 100.')
	lis = sorted(lis)
	num_vals = len(lis)
	# note the following would fail in python2
	ordinal_rank = int(numpy.ceil(percentile/100 * num_vals))
	ordinal_index = ordinal_rank - 1
	percentile_val = lis[ordinal_index]
	return percentile_val


class DataContainer:
	""" This has a 3D matrix whose dimentions are recipient, zip code, and year.  Each element of the matrix is a list of transactions that correspond to that recipient, zip code, year.  There is also a list of all donors for the purpose of identifying repeat donors.  This gives methods for inputting, sorting, and outputting data for our needs. """
	def __init__(self):
		# 'contribs' are constributions from *repeat donors* only
		# contribs EXCLUDE the first donation which was not a 'repeat'
		self.init_matrix()
		self.init_donor_list()

	def init_matrix(self):
		self.m = dict()

	def init_donor_list(self):
		self.people = dict()

	def contrib_num(self, block_id):
		# or for more speed, just keep track of the total in a separate variable
		return len(self.m[block_id])

	def contrib_amount(self, block_id):
		# or for more speed, just keep track of the total in a separate variable
		return sum(self.m[block_id])

	def __str__(self):
		return str(self.df)

	def add_repeat_contrib(self, amount, block_id):
		""" Takes in a row and adds the contrib to the data container """
		# add to matrix (ACTUALLY, the MATRIX could just be a single dictionary whose keys are the IDs year+zip_code+recipient)
		## remember, it's self.m[year][zip][recipient]
		if block_id not in self.m:
			self.m[block_id] = list()
		self.m[block_id].append(amount)

	def add_person(self, person_id):
		""" add to donor list """
		self.people[person_id] = None

	def percentile_contrib(self, percentile, block_id):
		""" Get the 'percentile' amount from the contrib_amounts list """
		# follow the 'ordinal-rank' method
		contrib_amounts = self.m[block_id]
		return ordinal_rank_percentile(percentile, contrib_amounts)

	def stats(self, percentile, year, zip_code, recipient, block_id):
		""" Return stats about the data """
		percentile_contrib = str(self.percentile_contrib(percentile, block_id))
		total_contrib_amount = str(self.contrib_amount(block_id))
		num_contribs = str(self.contrib_num(block_id))

		output_list = [recipient, zip_code, year, percentile_contrib, total_contrib_amount, num_contribs]
		output_string = '|'.join(output_list) + '\n'
		return output_string

	def has_donor(self, person_id):
		""" return true if the donor already exists in the df """
		return person_id in self.people
