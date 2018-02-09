import os

import pandas

from config import COL_NAMES_FULL, COL_NAMES, COL_TYPES, COL_CONVERTERS
from lib.decorate import record_elapsed_time


class DataContainer:
	""" This is a wrapper around a pandas dataframe that gives methods for inputting, sorting, and outputting data for our needs """
	def __init__(self, dir_path):
		# create dataframe
		self.init_dataframe(dir_path)
		# OMIT records that have nonempty 'entity'
		self.df = self.df[self.df['entity'].isnull()]

	def init_dataframe(self, dir_path):
		""" Takes in dir containing CSV file and creates dataframe with only the info we want. """
		file_path = os.path.join(dir_path, 'itcont.txt')
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

	def sort(self):
		""" Sorts the dataframe by zip-code and name. """
		# see https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
		self.df = self.df.sort_values(
			by=['zip-code', 'name'],
			kind='quicksort', # 'quicksort', 'mergesort', 'heapsort'
			na_position='first' # well there really SHOULDN'T be any NaNs.  We need to validate our data better
		)

