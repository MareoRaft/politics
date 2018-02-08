import os

from config import PATH
import lib
from lib.decorate import record_elapsed_time

@record_elapsed_time
def input_data(file_path):
	""" Inputs the data with the appropriate method (overloaded depending on what is input into the function). """
	# for now, only CSV.  but soon we will consider other methods...
	df = lib.input.dir_to_dataframe(file_path)
	return df

@record_elapsed_time
def output_data(data):
	print(data)

if __name__ == '__main__':
	file_path = PATH('test', 1)
	data = input_data(file_path)
	output_data(data)

