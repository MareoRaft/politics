import os
import csv

import pandas

from config import COL_NAMES_FULL, COL_NAMES, COL_TYPES, COL_CONVERTERS
from lib.decorate import record_elapsed_time


def row_string_to_row(row_string)
	""" Takes in a single line (string) and converts it to a 'row' for the dataframe """
	row_list = row_string.split('|')
	# probably not necessary:
	for val in row_list:
		val = val.strip()
	# if the transaction is from an entity, return False to show row invalid
	if row_list[15] != '':
		return (False, None)
	# restrict to just the columns we want
	row = [
		row_list[0],
		row_list[7],
		convert_zip_code(row_list[10]),
		row_list[13],
		row_list[14],
	]
	return (True, row)


class DataContainer:
	""" This is a wrapper around a pandas dataframe that gives methods for inputting, sorting, and outputting data for our needs """
	def __init__(self):
		# create dataframe
		self.init_dataframe()

	def init_dataframe(self, dir_path):
		self.df = pandas.DataFrame(
			data=None,
			index=None,
			columns=COL_NAMES,
			dtype=COL_TYPES,
			copy=False
		)

	def sort(self):
		""" Sorts the dataframe by zip-code and name. """
		# see https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
		self.df = self.df.sort_values(
			by=['zip-code', 'name'],
			kind='quicksort', # 'quicksort', 'mergesort', 'heapsort'
			na_position='first' # well there really SHOULDN'T be any NaNs.  We need to validate our data better
		)

	def append_row(self, row):
		""" Takes in a row and appends it to the dataframe """
		new_row_index = df.index.max() + 1
		df.loc[new_row_index] = row
