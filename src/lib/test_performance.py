""" This file is meant to run the program on large amounts of data so that I can see how long things take to execute. """
from config import PATH
from lib.stream import stream

def test_performance():
	7 records
	stream(PATH('test', 3))

	# 1,000 records
	stream(PATH('test', 4))
	# opening and closing write handle: 8-9 seconds
	# keep write handle open: 7.5-8.5 seconds
	# without sorting: 6-7 seconds
	# with new dictionary structure: 0-1 seconds

	# 10,000 records
	stream(PATH('test', 5))
	# 0-1 seconds

	# 100,000 records
	stream(PATH('test', 6))
	# 1.5-2.5 seconds

