import os
import csv

import pandas

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


class DataContainer:
	""" This is a wrapper around a pandas dataframe that gives methods for inputting, sorting, and outputting data for our needs """
	def __init__(self):
		self.init_dataframe()

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

	def stats(self, row, percentile):
		""" Return stats about the data """
		recipient = row['recipient']
		zip_code = row['zip-code']
		year = row['year']
		total_amount_contributions = str(0) # for this specific (recipient, year, zip_code)
		total_num_tx = str(0) # same
		percentile = str(percentile)

		output_list = [recipient, zip_code, year, percentile, total_amount_contributions, total_num_tx]
		output_string = '|'.join(output_list)
		return output_string

	def has_donor(self, person):
		""" return true if the donor already exists in the df """
		(zip_code, donor) = person
		results = self.df[(self.df['zip-code'] == zip_code) & (self.df['donor'] == donor)]
		return bool(len(results))
