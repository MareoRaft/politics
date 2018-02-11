import os

from config import get_percentile
from lib.helpers import row_string_to_row, get_donor_id, get_block_id
from lib.data_container import Donors, Contributions

def clear(file_path, noclobber=False):
	""" Removes a file.  If file exists and noclobber=True, it will ask if you want to overwrite it. """
	if os.path.lexists(file_path) and noclobber:
		proceed = input('The file {} will be overwritten.  To proceed, type "y" then RETURN.'.format(file_path))
		if proceed != "y":
			raise SystemExit('Cannot proceed with program until file is deleted.')
	# 'Clear' the file.  (Create new file if doesn't exist, replace content with '' if it exists.)
	with open(file_path, 'w'):
		pass

def stream(dir_path):
	""" Simulate a data streaming situation """
	input_path = os.path.join(dir_path, 'input/itcont.txt')
	output_path = os.path.join(dir_path, 'output/repeat_donors.txt')

	percentile_path = os.path.join(dir_path, 'input/percentile.txt')
	percentile = get_percentile(percentile_path)

	# Before beginning, clear the output file.
	clear(output_path)

	donors = Donors()
	contribs = Contributions()
	# To simulate streaming, I ONLY ALLOW myself to view the file ONE LINE at a time, and I MUST output updated information after each line is read, before reading the next line.
	with open(output_path, 'a') as out:
		# Reading the file in binary mode tolerates non-UTF-8 characters
		with open(input_path, 'rb') as file:
			for line in file:
				# We tolerate non-UTF-8 characters by ignoring them.  There is definitely a better way to do this, and the current method should be changed in the future:
				line = str(line)[2:-3]
				(is_valid_row, row) = row_string_to_row(line)
				if not is_valid_row:
					continue
				# Add donor to list.  They cannot get added twice since the 'add' method is idempotent.
				donor_id = get_donor_id(row)
				donors.add(donor_id, row['year'])
				# If the donor is making a 'repeat contribution', record it in the contribution list.
				is_repeat_donor = donors.is_repeat(donor_id, row['year'])
				if is_repeat_donor:
					block_id = get_block_id(row)
					contribs.add(row['amount'], block_id)
					# Output the statistics line to repeat_donors.txt.
					stats = contribs.stats(percentile, row['year'], row['zip-code'], row['recipient'], block_id)
					out.write(stats)
	print('Streaming simulation complete!!  See output file {}'.format(output_path))
	return donors
