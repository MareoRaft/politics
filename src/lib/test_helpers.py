import pytest

from lib.helpers import *

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
		'name': 'DEEHAN, WILLIAM N',
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
		'name': 'ABBOTT, JOSEPH',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}

	# amount of 0
	row_string = 'C00384818|N|M2|P|201702039042412112|15|IND|ABBOTT, JOSEPH|WOONSOCKET|RI|028956146|||01122017|0||2017020211435-887|1147467|||'
	is_valid, row = row_string_to_row(row_string)
	assert not is_valid

	# negative amount
	row_string = 'C00384818|N|M2|P|201702039042412112|15|IND|ABBOTT, JOSEPH|WOONSOCKET|RI|028956146|||01122017|-250||2017020211435-887|1147467|||4020820171370030285\n'
	is_valid, row = row_string_to_row(row_string)
	assert not is_valid

def test_ordinal_rank_percentile():
	vals = [15, 20, 35, 40, 50]
	p = 0
	with pytest.raises(ValueError):
		ordinal_rank_percentile(p, vals)

	vals = [15, 20, 35, 40, 50]
	p = 1
	assert ordinal_rank_percentile(p, vals) == 15

	vals = [15, 20, 35, 40, 50]
	p = 5
	assert ordinal_rank_percentile(p, vals) == 15

	vals = [15, 20, 35, 40, 50]
	p = 30
	assert ordinal_rank_percentile(p, vals) == 20

	vals = [15, 20, 35, 40, 50]
	p = 40
	assert ordinal_rank_percentile(p, vals) == 20

	vals = [15, 20, 35, 40, 50]
	p = 50
	assert ordinal_rank_percentile(p, vals) == 35

	vals = [15, 20, 35, 40, 50]
	p = 100
	assert ordinal_rank_percentile(p, vals) == 50

	vals = [6, 3, 7, 8, 8, 20, 16, 9, 10, 13, 15]
	p = 25
	assert ordinal_rank_percentile(p, vals) == 7

	vals = [6, 3, 7, 8, 8, 20, 16, 9, 10, 13, 15]
	p = 50
	assert ordinal_rank_percentile(p, vals) == 9

	vals = [6, 3, 7, 8, 8, 20, 16, 9, 10, 13, 15]
	p = 75
	assert ordinal_rank_percentile(p, vals) == 15

	vals = [6, 3, 7, 8, 8, 20, 16, 9, 10, 13, 15]
	p = 100
	assert ordinal_rank_percentile(p, vals) == 20

