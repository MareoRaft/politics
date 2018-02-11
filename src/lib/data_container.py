import os
import csv

import numpy

from config import PATH, COL_NAMES_FULL, COL_NAMES, COL_TYPES, COL_CONVERTERS, convert_zip_code, convert_year, convert_amount
from lib.decorate import record_elapsed_time

def row_string_to_row(row_string):
	""" Takes in a single line (string) and converts it to a 'row' for the dataframe """
	row_list = row_string.split('|')
	# probably not necessary:
	for val in row_list:
		val = val.strip()
	# restrict to just the columns we want
	row = {
		'recipient': row_list[0],
		'name': row_list[7],
		'zip-code': row_list[10],
		'year': row_list[13],
		'amount': row_list[14],
		'entity': row_list[15],
	}

	# Check for a bad row.
	## if the transaction is from an entity, return False to show row invalid
	if row_list[15] != '':
		return (False, None)
	## If TRANSACTION_DT is an invalid date (e.g., empty, malformed)
	if len(row['year']) < 4:
		return (False, None)
	## If ZIP_CODE is an invalid zip code (i.e., empty, fewer than five digits)
	if len(row['zip-code']) < 5:
		return (False, None)
	## If the NAME is an invalid name (e.g., empty, malformed)
	if len(row['name']) == 0:
		return (False, None)
	## If any lines in the input file contains empty cells in the CMTE_ID or TRANSACTION_AMT fields
	if len(row['recipient']) == 0:
		return (False, None)
	if len(row['amount']) == 0:
		return (False, None)
	# if the amount is 0 or negative, ignore
	try:
		int(row['amount'])
	except:
		return (False, None)
	if int(row['amount']) <= 0:
		return (False, None)

	# Clean values, then succeed.
	row['zip-code'] = convert_zip_code(row['zip-code'])
	row['year'] = convert_year(row['year'])
	row['amount'] = convert_amount(row['amount'])
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
		self.donors = dict()

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

	def add_donor(self, donor_id, year):
		""" add to donor list """
		if donor_id not in self.donors:
			self.donors[donor_id] = year

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

	def is_repeat_donor(self, donor_id, year):
		""" return true if the donor already exists in the df """
		if donor_id in self.donors:
			if year > self.donors[donor_id]:
				return True
		return False

