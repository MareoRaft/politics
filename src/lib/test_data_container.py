import os

import pytest

from config import *
from lib.data_container import *
from lib.stream import stream


def test_convert_zip_code():
	assert convert_zip_code('90017') == '90017'
	assert convert_zip_code('028956146') == '02895'
	assert convert_zip_code('307502818') == '30750'

def test_convert_year():
	assert convert_year('1986') == '1986'
	assert convert_year('01032017') == '2017'
	assert convert_year('01122018') == '2018'

def test_row_string_to_row():
	# entity
	row_string = 'C00629618|N|TER|P|201701230300133512|15C|IND|PEREZ, JOHN A|LOS ANGELES|CA|90017|PRINCIPAL|DOUBLE NICKEL ADVISORS|01032017|40|H6CA34245|SA01251735122|1141239|||2012520171368850783'
	is_valid, row = row_string_to_row(row_string)
	assert not is_valid

	# individual, no newline
	row_string = 'C00177436|N|M2|P|201702039042410894|15|IND|DEEHAN, WILLIAM N|ALPHARETTA|GA|300047357|UNUM|SVP, SALES, CL|01312017|384||PR2283873845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029337'
	is_valid, row = row_string_to_row(row_string)
	assert is_valid
	assert row == {
		'recipient': 'C00177436',
		'donor': 'DEEHAN, WILLIAM N',
		'zip-code': '30004',
		'year': '2017',
		'amount': 384,
	}

	# individual, newline
	row_string = 'C00384818|N|M2|P|201702039042412112|15|IND|ABBOTT, JOSEPH|WOONSOCKET|RI|028956146|CVS HEALTH|VP, RETAIL PHARMACY OPS|01122017|250||2017020211435-887|1147467|||4020820171370030285\n'
	is_valid, row = row_string_to_row(row_string)
	assert is_valid
	assert row == {
		'recipient': 'C00384818',
		'donor': 'ABBOTT, JOSEPH',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}

def test_init():
	# a single entity
	d = DataContainer()
	assert len(d.df) == 0

def test_append_row():
	# one row
	d = DataContainer()
	row = {
		'recipient': 'C00384818',
		'donor': 'ABBOTT, JOSEPH',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}
	d.append_row(row)
	assert len(d.df) == 1

	# two rows
	d = DataContainer()
	row = {
		'recipient': 'C00384818',
		'donor': 'ABBOTT, JOSEPH',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}
	d.append_row(row)
	row = {
		'recipient': 'C00384818',
		'donor': 'ABBOTT, JOSEPH 2',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}
	d.append_row(row)
	assert len(d.df) == 2

def test_stream():
	# a single entity
	d = stream(PATH('test', 1))
	assert len(d.df) == 0

	# a single individual (not entity)
	d = stream(PATH('test', 2))
	assert d.df.iloc[0]['recipient'] == 'C00177436'
	assert d.df.iloc[0]['donor'] == 'DEEHAN, WILLIAM N'
	assert d.df.iloc[0]['zip-code'] == '30004'
	assert d.df.iloc[0]['year'] == '2017'
	assert d.df.iloc[0]['amount'] == 384

	# seven people (one of which is entity)
	d = stream(PATH('test', 3))
	assert len(d.df) == 6

def test_sort():
	# six legit people
	d = stream(PATH('test', 3))
	d.sort()
	## zips in order
	correct_zip_order = ['02895', '02895', '02895', '02895', '30004', '30750']
	zip_order = [row[1]['zip-code'] for row in d.df.iterrows()]
	assert zip_order == correct_zip_order
	## donors in suborder
	correct_donor_order = ['ABBOTT, JOSEPH', 'ABBOTT, JOSEPH', 'SABOURIN, JAMES', 'SABOURIN, JAMES', 'DEEHAN, WILLIAM N', 'JEROME, CHRISTOPHER']
	donor_order = [row[1]['donor'] for row in d.df.iterrows()]
	assert donor_order == correct_donor_order
