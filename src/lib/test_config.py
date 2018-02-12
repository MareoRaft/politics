from config import *


def test_convert_zip_code():
	assert convert_zip_code('90017') == '90017'
	assert convert_zip_code('028956146') == '02895'
	assert convert_zip_code('307502818') == '30750'

def test_convert_year():
	assert convert_year('1986') == '1986'
	assert convert_year('01032017') == '2017'
	assert convert_year('01122018') == '2018'

def test_round_normally():
	assert round_normally(0) == 0
	assert round_normally(0.2) == 0
	assert round_normally(0.5) == 1
	assert round_normally(0.6) == 1
	assert round_normally(1) == 1
	assert round_normally(1.367) == 1
	assert round_normally(1.5) == 2
	assert round_normally(1.8) == 2
	assert round_normally(2.0) == 2

def test_convert_amount():
	assert convert_amount('0') == 0
	assert convert_amount('0.2') == 0
	assert convert_amount('0.5') == 1
	assert convert_amount('0.6') == 1
	assert convert_amount('1') == 1
	assert convert_amount('1.367') == 1
	assert convert_amount('1.5') == 2
	assert convert_amount('1.8') == 2
	assert convert_amount('2.0') == 2

