""" This file is meant to run the program on large amounts of data so that I can see how long things take to execute. """
from config import PATH
from main import main

def test_performance():
	# 7 records
	main(PATH('test', 3))

	# 1,000 records
	main(PATH('test', 4))
	# opening and closing write handle: 8-9 seconds
	# keep write handle open: 7.5-8.5 seconds
	# without sorting: 6-7 seconds
	# with new dictionary structure: 0-1 seconds

	# 10,000 records
	main(PATH('test', 5))
	# 0-1 seconds

	# 100,000 records
	main(PATH('test', 6))
	# 1.5-2.5 seconds

	# 1,000,000 records
	main(PATH('test', 7))
	# 15.5 - 16.5 seconds
	# tuples same speed as concatenation
	# better to pass around pieces or pre-calculate IDs than to pass around rows
	# 15.5 - 16 seconds

	# # 10,000,000 records (actually, a little less)
	# main(PATH('test', 9))
	# # 84 seconds
