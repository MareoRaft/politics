""" config settings that python files can use """
from os import path
REPO_PATH = path.dirname(path.dirname(path.abspath(__file__)))

# Paths
PATH_DICT = {
	'repo': REPO_PATH,
	'input': path.join(REPO_PATH, 'input'),
	'output': path.join(REPO_PATH, 'output'),
	'tests': path.join(REPO_PATH, 'insight_testsuite/tests'),
	'temp': path.join(REPO_PATH, 'temp-tests'),
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
def get_percentile(file_path):
	""" gets percentile from percentile file """
	with open(file_path) as file:
		percentile_string = file.read()
	percentile = int(percentile_string.strip())
	return percentile

# Data columns
## col names for government input files
COL_NAMES_FULL = [
	'recipient', # CMTE_ID 0
	'amendment-indicator', # AMNDT_IND 1
	'report-type', # RPT_TP 2
	'tx-indicator', # TRANSACTION_PGI 3
	'image-num', # IMAGE_NUM 4
	'tx-type', # TRANSACTION_TP 5
	'entity-type', # ENTITY_TP 6
	'name', # NAME 7
	'city', # CITY 8
	'state', # STATE 9
	'zip-code', # ZIP_CODE 10
	'employer', # EMPLOYER 11
	'occupation', # OCCUPATION 12
	'year', # TRANSACTION_DT 13
	'amount', # TRANSACTION_AMT 14
	'entity', # OTHER_ID 15
	'tx-ID', # TRAN_ID 16
	'file-num', # FILE_NUM 17
	'memo-code', # MEMO_CD 18
	'memo-text', # MEMO_TEXT 19
	'sub-ID', # SUB_ID 20
]
## col names we need, (subset of COL_NAMES_FULL)
COL_NAMES = [
	'recipient', # 0
	'name', # 7
	'zip-code', # 10
	'year', # 13
	'amount', # 14
]
## the data type of each column
COL_TYPES = {
	'recipient': str,
	'name': str,
}
## the data cleaner for each column
def convert_zip_code(zip_code):
	return zip_code[:5]
def convert_year(date_string):
	return date_string[-4:]
def convert_amount(amount_string):
	return int(amount_string)
COL_CONVERTERS = {
	'zip-code': convert_zip_code,
	'year': convert_year,
	'amount': convert_amount,
}
