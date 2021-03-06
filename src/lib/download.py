""" (Note: This module is not currently in use.)  This module automates downloading voter data from the government website.  It remains part of this repository as a potentially helpful tool.
"""
import os
import subprocess

import wget
import zipfile

from config import PATH
from lib.decorate import record_elapsed_time


def verify_end_year(yr):
	yr = int(yr)
	assert yr >= 1980
	assert yr <= 2018 # maybe GET CURRENT YEAR instead, rounding down to even
	assert yr % 2 == 0

def end_year_to_url(year):
	""" Takes an end_year (for example, in 2011-2012, the 'end year' is 2012) and returns the url for corresponding the datafile. """
	yr = str(year)
	assert len(yr) == 4
	short_yr = yr[2:4]
	url_template = 'https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/{}/indiv{}.zip'
	url = url_template.format(yr, short_yr)
	return url

def download_data(year, dir_path):
	verify_end_year(year)
	url = end_year_to_url(year)
	# download
	zip_filename = wget.download(url, out=dir_path)
	# unzip
	zip_file_path = os.path.join(dir_path, zip_filename)
	zip_ref = zipfile.ZipFile(zip_file_path, 'r')
	zip_ref.extractall(dir_path)
	zip_ref.close()

@record_elapsed_time
def download_all_data():
	for year in range(1980, 2020, 2):
		download_data_for_year(year, PATH('input'))
