import os

import pandas

from lib.decorate import record_elapsed_time

@record_elapsed_time
def sort_dataframe(df):
	""" Takes in dataframe and sorts by zip-code and name. """
	# see https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
	df = df.sort_values(
		by=['zip-code', 'name'],
		kind='quicksort', # 'quicksort', 'mergesort', 'heapsort'
		na_position='first' # well there really SHOULDN"T be any.  We will need to validate our data better
	)
	return df
