import os

import pytest

from lib.download import *

REPO_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEST1_PATH = os.path.join(REPO_DIR, 'insight_testsuite/tests/test_1/input/itcont.txt')

def test_verify_end_year():
	# good years
	verify_end_year('1980')
	verify_end_year('1982')
	verify_end_year('2000')
	verify_end_year('2018')

	# bad years
	## too early
	with pytest.raises(AssertionError):
		verify_end_year('1978')
	## odd numbered year
	with pytest.raises(AssertionError):
		verify_end_year('2001')
	## too late
	with pytest.raises(AssertionError):
		verify_end_year('2020')

def test_end_year_to_url():
	assert end_year_to_url('1980') == 'https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/1980/indiv80.zip'
	assert end_year_to_url('2012') == 'https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/2012/indiv12.zip'
