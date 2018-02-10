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
	""" This is a wrapper around a pandas dataframe that gives methods for inputting, sorting, and outputting data for our needs """
	def __init__(self):
		# 'contribs' are constributions from *repeat donors* only
		# contribs EXCLUDE the first donation which was not a 'repeat'
		self.contrib_amounts = []
		self.init_dataframe()

	def contrib_num(self):
		# or for more speed, just keep track of the total in a separate variable
		return len(self.contrib_amounts)

	def total_contrib_amount(self):
		# or for more speed, just keep track of the total in a separate variable
		return sum(self.contrib_amounts)

	def init_dataframe(self):
		# DataFrame.__init__ doesn't allow you to specify a different data type for each col, so I will just use read_csv to perform the intialization instead
		file_path = PATH('blank-csv')
		self.df = pandas.read_csv(file_path,
			delimiter='|',
			header=None,
			names=COL_NAMES_FULL,
			usecols=COL_NAMES,
			dtype=COL_TYPES,
			converters=COL_CONVERTERS
			# infer_datetime_format=True,
			# parse_dates=['tx-date']
		)

	def __str__(self):
		return str(self.df)

	def sort(self):
		""" Sorts the dataframe by zip-code and donor. """
		# see https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
		self.df = self.df.sort_values(
			by=['zip-code', 'donor'],
			kind='quicksort', # 'quicksort', 'mergesort', 'heapsort'
			na_position='first' # well there really SHOULDN'T be any NaNs.  We need to validate our data better
		)

	def append_row(self, row):
		""" Takes in a row and appends it to the dataframe """
		self.df = self.df.append(row, ignore_index=True)

	def percentile_contrib(self, percentile):
		""" Get the 'percentile' amount from the contrib_amounts list """
		# follow the 'ordinal-rank' method
		return ordinal_rank_percentile(percentile, self.contrib_amounts)

	def stats(self, row, percentile):
		""" Return stats about the data """
		recipient = row['recipient']
		zip_code = row['zip-code']
		year = row['year']
		percentile_contrib = str(self.percentile_contrib(percentile))
		total_contrib_amount = str(self.total_contrib_amount())
		num_contribs = str(self.contrib_num())

		output_list = [recipient, zip_code, year, percentile_contrib, total_contrib_amount, num_contribs]
		output_string = '|'.join(output_list) + '\n'
		return output_string

	def has_donor(self, person):
		""" return true if the donor already exists in the df """
		(zip_code, donor) = person
		results = self.df[(self.df['zip-code'] == zip_code) & (self.df['donor'] == donor)]
		return bool(len(results))
