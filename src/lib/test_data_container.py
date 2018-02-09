import os

import pytest

from config import *
from lib.data_container import *


def test_convert_zip_code():
	assert convert_zip_code('90017') == '90017'
	assert convert_zip_code('028956146') == '02895'
	assert convert_zip_code('307502818') == '30750'

def test_row_string_to_row():
	# entity
	row_string = 'C00629618|N|TER|P|201701230300133512|15C|IND|PEREZ, JOHN A|LOS ANGELES|CA|90017|PRINCIPAL|DOUBLE NICKEL ADVISORS|01032017|40|H6CA34245|SA01251735122|1141239|||2012520171368850783'
	assert row_string_to_row(row_string) is None

	# individual, no newline
	row_string = 'C00177436|N|M2|P|201702039042410894|15|IND|DEEHAN, WILLIAM N|ALPHARETTA|GA|300047357|UNUM|SVP, SALES, CL|01312017|384||PR2283873845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029337'
	assert row_string_to_row(row_string) == ['C00177436', 'DEEHAN, WILLIAM N', '30004', '01312017', '384']

	# individual, newline
	row_string = 'C00384818|N|M2|P|201702039042412112|15|IND|ABBOTT, JOSEPH|WOONSOCKET|RI|028956146|CVS HEALTH|VP, RETAIL PHARMACY OPS|01122017|250||2017020211435-887|1147467|||4020820171370030285
'
	assert row_string_to_row(row_string) == ['C00384818', 'ABBOTT, JOSEPH', '02895', '01122017', '250']

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
	print(d.df)
	## zips in order
	correct_zip_order = ['02895', '02895', '02895', '02895', '30004', '30750']
	zip_order = [row[1]['zip-code'] for row in d.df.iterrows()]
	assert zip_order == correct_zip_order
	## names in suborder
	correct_name_order = ['ABBOTT, JOSEPH', 'ABBOTT, JOSEPH', 'SABOURIN, JAMES', 'SABOURIN, JAMES', 'DEEHAN, WILLIAM N', 'JEROME, CHRISTOPHER']
	name_order = [row[1]['name'] for row in d.df.iterrows()]
	assert name_order == correct_name_order
