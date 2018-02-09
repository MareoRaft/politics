import os

import pytest

from config import *
from lib.data_container import *


def test_convert_zip_code():
	assert convert_zip_code('90017') == '90017'
	assert convert_zip_code('028956146') == '02895'
	assert convert_zip_code('307502818') == '30750'

def test_init():
	# a single entity
	d = DataContainer(PATH('input', 1))
	assert len(d.df) == 0

	# a single individual (not entity)
	d = DataContainer(PATH('input', 2))
	assert d.df.iloc[0]['politician'] == 'C00177436'
	assert d.df.iloc[0]['name'] == 'DEEHAN, WILLIAM N'
	assert d.df.iloc[0]['zip-code'] == '30004'
	assert d.df.iloc[0]['tx-date'] == '01312017'
	assert d.df.iloc[0]['tx-amount'] == 384
	assert not isinstance(d.df.iloc[0]['entity'], str)

	# seven people (one of which is entity)
	d = DataContainer(PATH('input', 3))
	assert len(d.df) == 6

def test_sort():
	# six legit people
	d = DataContainer(PATH('input', 3))
	d.sort()
	## zips in order
	correct_zip_order = ['02895', '02895', '02895', '02895', '30004', '30750']
	zip_order = [row[1]['zip-code'] for row in d.df.iterrows()]
	assert zip_order == correct_zip_order
	## names in suborder
	correct_name_order = ['ABBOTT, JOSEPH', 'ABBOTT, JOSEPH', 'SABOURIN, JAMES', 'SABOURIN, JAMES', 'DEEHAN, WILLIAM N', 'JEROME, CHRISTOPHER']
	name_order = [row[1]['name'] for row in d.df.iterrows()]
	assert name_order == correct_name_order
