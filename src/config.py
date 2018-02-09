""" config settings that python files can use """
from os import path
REPO_PATH = path.dirname(path.dirname(path.abspath(__file__)))

# Paths
PATH_DICT = {
	'repo': REPO_PATH,
	'input': path.join(REPO_PATH, 'input'),
	'output': path.join(REPO_PATH, 'output'),
	'tests': path.join(REPO_PATH, 'insight_testsuite/tests'),
}
def PATH(keyword, num=None):
	if num is None:
		return PATH_DICT[keyword]
	if keyword == 'test':
		return path.join(PATH_DICT['tests'], 'test_{}'.format(num))
	elif keyword == 'input':
		return path.join(PATH_DICT['tests'], 'test_{}/input'.format(num))
	elif keyword == 'output':
		return path.join(PATH_DICT['tests'], 'test_{}/output'.format(num))
	else:
		raise ValueError('Nonempty num and bad keyword.')

# Percentile
percentile_file_path = path.join(PATH('input'), 'percentile.txt')
with open(percentile_file_path) as file:
	percentile_string = file.read()
PERCENTILE = int(percentile_string.strip())

# Data columns
## col names for government input files
COL_NAMES_FULL = [
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
## col names we need, (subset of col_names_full)
COL_NAMES = [
	'politician',
	'name',
	'zip-code',
	'tx-date',
	'tx-amount',
	'entity', # indicates if contribution came from an entity not a person
]
## the data type of each column
COL_TYPES = {
	'politician': str,
	'name': str,
	'tx-date': str,
	'tx-amount': int,
	'entity': str,
}
## the data cleaner for each column
def convert_zip_code(zip_code):
	return zip_code[0:5]
COL_CONVERTERS = {
	'zip-code': convert_zip_code,
}
