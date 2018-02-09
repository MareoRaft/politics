import pytest

from config import PATH
from lib.input import dir_to_dataframe
from lib.mutate import *

def test_sort_dataframe():
	# six legit people
	df = dir_to_dataframe(PATH('input', 3))
	df = sort_dataframe(df)
	## zips in order
	correct_zip_order = ['02895', '02895', '02895', '02895', '30004', '30750']
	zip_order = [row[1]['zip-code'] for row in df.iterrows()]
	assert zip_order == correct_zip_order
	## names in suborder
	correct_name_order = ['ABBOTT, JOSEPH', 'ABBOTT, JOSEPH', 'SABOURIN, JAMES', 'SABOURIN, JAMES', 'DEEHAN, WILLIAM N', 'JEROME, CHRISTOPHER']
	name_order = [row[1]['name'] for row in df.iterrows()]
	assert name_order == correct_name_order
