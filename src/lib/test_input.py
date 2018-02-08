import os

import pytest

from config import PATH
from lib.input import *


def test_convert_zip_code():
	assert convert_zip_code('90017') == '90017'
	assert convert_zip_code('028956146') == '02895'
	assert convert_zip_code('307502818') == '30750'

def test_dir_to_dataframe():
	# a single entity
	df = dir_to_dataframe(PATH('input', 1))
	assert len(df) == 0

	# a single individual (not entity)
	df = dir_to_dataframe(PATH('input', 2))
	assert df.iloc[0]['politician'] == 'C00177436'
	assert df.iloc[0]['name'] == 'DEEHAN, WILLIAM N'
	assert df.iloc[0]['zip-code'] == '30004'
	assert df.iloc[0]['tx-date'] == '01312017'
	assert df.iloc[0]['tx-amount'] == 384
	assert not isinstance(df.iloc[0]['entity'], str)

	# seven people (one of which is entity)
	df = dir_to_dataframe(PATH('input', 3))
	assert len(df) == 6
