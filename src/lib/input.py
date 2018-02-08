import os

import pandas

from lib.decorate import record_elapsed_time

# col names for government input files
col_names_full = [
	'politician', # CMTE_ID
	'amendment-indicator', # AMNDT_IND
	'report-type', # RPT_TP
	'tx-indicator', # TRANSACTION_PGI
	'image-num', # IMAGE_NUM
	'tx-type', # TRANSACTION_TP
	'entity-type', # ENTITY_TP
	'name', # NAME
	'city', # CITY
	'state', # STATE
	'zip-code', # ZIP_CODE
	'employer', # EMPLOYER
	'occupation', # OCCUPATION
	'tx-date', # TRANSACTION_DT
	'tx-amount', # TRANSACTION_AMT
	'entity', # OTHER_ID
	'tx-ID', # TRAN_ID
	'file-num', # FILE_NUM
	'memo-code', # MEMO_CD
	'memo-text', # MEMO_TEXT
	'sub-ID', # SUB_ID
]
# col names we need, (subset of col_names_full)
col_names = [
	'politician',
	'name',
	'zip-code',
	'tx-date',
	'tx-amount',
	'entity', # indicates if contribution came from an entity not a person
]
# the data type of each column
col_types = {
	'politician': str,
	'name': str,
	'tx-date': str,
	'tx-amount': int,
	'entity': str,
}

def convert_zip_code(zip_code):
	return zip_code[0:5]

# the data cleaner for each column
col_converters = {
	'zip-code': convert_zip_code,
}

@record_elapsed_time
def dir_to_dataframe(dir_path):
	""" Takes in dir containing CSV file and creates dataframe with only the info we want. """
	file_path = os.path.join(dir_path, 'itcont.txt')
	df = pandas.read_csv(file_path,
		delimiter='|',
		header=None,
		names=col_names_full,
		usecols=col_names,
		dtype=col_types,
		converters=col_converters
		# infer_datetime_format=True,
		# parse_dates=['tx-date']
	)
	# OMIT records that have nonempty 'entity'
	df = df[df['entity'].isnull()]
	return df
