import os

import lib
from lib.decorate import record_elapsed_time

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST1_PATH = os.path.join(REPO_DIR, 'insight_testsuite/tests/test_1/input/itcont.txt')

@record_elapsed_time
def input_data(file_path):
	""" Inputs the data with the appropriate method (overloaded depending on what is input into the function). """
	# for now, only CSV.  but soon we will consider other methods...
	df = lib.input.csv_to_dataframe(file_path)
	return df

@record_elapsed_time
def output_data(data):
	print(data)

if __name__ == '__main__':
	file_path = TEST1_PATH
	data = input_data(file_path)
	output_data(data)

