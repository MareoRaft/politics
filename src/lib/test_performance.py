""" This file is meant to run the program on large amounts of data so that I can see how long things take to execute. """
from config import PATH
from lib.stream import stream

def test_performance():
	# 1,000 records
	stream(PATH('test', 4))
	# opening and closing write handle: 8-9 seconds
	# keep write handle open: 7.5-8.5 seconds
	# without sorting: 6-7 seconds
