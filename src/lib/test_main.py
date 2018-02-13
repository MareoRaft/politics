""" This file is meant to test the entire program in its entirety.  It is also meant to run the program on large amounts of data so that I can see how long things take to execute. """
from config import PATH
from main import main


def test_main_1():
	# a single entity
	d = main(PATH('test', 1))
	assert len(d.donors) == 0

def test_main_2():
	# a single individual (not entity)
	d = main(PATH('test', 2))
	assert len(d.donors) == 1

def test_main_3():
	# 7 records (but only 4 donors)
	d = main(PATH('test', 3))
	assert len(d.donors) == 4

def test_main_4():
	# 1,000 records
	main(PATH('test', 4))
	# opening and closing write handle: 8-9 seconds
	# keep write handle open: 7.5-8.5 seconds
	# without sorting: 6-7 seconds
	# with new dictionary structure: 0-1 seconds

def test_main_5():
	# 10,000 records
	main(PATH('test', 5))
	# 0-1 seconds

def test_main_6():
	# 100,000 records
	main(PATH('test', 6))
	# 1.5-2.5 seconds

# def test_main_7():
# 	# 1,000,000 records
# 	main(PATH('test', 7))
# 	# 15.5 - 16.5 seconds
# 	# tuples more or less the same speed as concatenation
# 	# 15.5 - 16 seconds

def test_main_8():
	# A slew of use cases that could catch potential glitches
	main(PATH('test', 8))

# def test_main_9():
# 	# 10,000,000 records (actually, a little less)
# 	main(PATH('test', 9))
# 	# 84 seconds

