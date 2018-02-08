import os

import pytest

from lib.input import *

REPO_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEST1_PATH = os.path.join(REPO_DIR, 'insight_testsuite/tests/test_1/input/itcont.txt')

def test_convert_zip_code():
	assert convert_zip_code('90017') == '90017'
	assert convert_zip_code('028956146') == '02895'
	assert convert_zip_code('307502818') == '30750'

def test_csv_to_dataframe():
	df = csv_to_dataframe(TEST1_PATH)
	assert df.iloc[0]['politician'] == 'C00629618'
	assert df.iloc[0]['name'] == 'PEREZ, JOHN A'
	assert df.iloc[0]['zip-code'] == '90017'
	assert df.iloc[0]['tx-date'] == '01032017'
	assert df.iloc[0]['tx-amount'] == 40
	assert df.iloc[0]['entity'] == 'H6CA34245'

