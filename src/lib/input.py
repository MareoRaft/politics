from lib.decorate import record_elapsed_time

import pandas

# WE WANT TO IMPORT only THE "Contributions by Individuals" files from https://classic.fec.gov/finance/disclosure/ftpdet.shtml


@record_elapsed_time
def csv_to_dataframe(file_path):
	""" Takes in politics formated CSV file and creates dataframe with only the columns we want. """
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
	df = pandas.read_csv(file_path, delimiter='|', header=None, names=col_names_full, usecols=col_names)

