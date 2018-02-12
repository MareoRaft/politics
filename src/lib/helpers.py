import math

from config import convert_zip_code, convert_year, convert_amount


def get_donor_id(row):
	return (row['zip-code'], row['name'])

def get_block_id(row):
	return (row['year'], row['zip-code'], row['recipient'])

def row_string_to_row(row_string):
	""" Takes in a single line (string) then validates and converts it to a 'row' for the dataframe.

	Returns
	-------
	(is_valid, row)
	is_valid: bool, tells you if you should discard the row or not
	row: the converted cleaned row
	"""

	# if row is empty, move on
	if row_string.strip() == '':
		return (False, None)
	row_list = row_string.split('|')
	# clean away whitespace
	for val in row_list:
		val = val.strip()
	# restrict to just the columns we want
	row = {
		'recipient': row_list[0],
		'name': row_list[7],
		'zip-code': row_list[10],
		'year': row_list[13],
		'amount': row_list[14],
	}

	# Check for a bad row.
	## if the transaction is from an entity, return False to show row invalid
	if row_list[15] != '':
		return (False, None)
	## If TRANSACTION_DT is an invalid date (e.g., empty, malformed)
	if len(row['year']) < 4:
		return (False, None)
	## If ZIP_CODE is an invalid zip code (i.e., empty, fewer than five digits)
	if len(row['zip-code']) < 5:
		return (False, None)
	## If the NAME is an invalid name (e.g., empty, malformed)
	if len(row['name']) == 0:
		return (False, None)
	## If any lines in the input file contains empty cells in the CMTE_ID or TRANSACTION_AMT fields
	if len(row['recipient']) == 0:
		return (False, None)
	if len(row['amount']) == 0:
		return (False, None)
	# if the amount is 0 or negative, ignore
	try:
		int(row['amount'])
	except:
		return (False, None)
	if int(row['amount']) <= 0:
		return (False, None)

	# Clean values
	row['zip-code'] = convert_zip_code(row['zip-code'])
	row['year'] = convert_year(row['year'])
	row['amount'] = convert_amount(row['amount'])
	# Return clean row
	return (True, row)

def ordinal_rank_percentile(percentile, lis):
	if percentile <= 0 or percentile > 100:
		raise ValueError('Percentile P must satisfy 0 < P <= 100.')
	lis = sorted(lis)
	num_vals = len(lis)
	# the int and float conversions are for compatibility with python2
	ordinal_rank = int(math.ceil(float(percentile)/100 * num_vals))
	ordinal_index = ordinal_rank - 1
	percentile_val = lis[ordinal_index]
	return percentile_val
