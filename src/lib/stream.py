import os

from config import get_percentile
from lib.data_container import DataContainer, row_string_to_row

def clear(file_path, noclobber=False):
	""" Removes a file.  If file exists and noclobber=True, it will ask if you want to overwrite it. """
	if os.path.lexists(file_path) and noclobber:
		proceed = input('The file {} will be overwritten.  To proceed, type "y" then RETURN.'.format(file_path))
		if proceed != "y":
			raise SystemExit('Cannot proceed with program until file is deleted.')
	# 'clear' the file (create new file if doesn't exist, replace content with '' if exists).
	with open(file_path, 'w'):
		pass

def stream(dir_path):
	""" Simulate a data streaming situation """
	input_path = os.path.join(dir_path, 'input/itcont.txt')
	output_path = os.path.join(dir_path, 'output/repeat_donors.txt')

	percentile_path = os.path.join(dir_path, 'input/percentile.txt')
	percentile = get_percentile(percentile_path)

	# before beginning, clear output file
	clear(output_path)

	d = DataContainer()
	# To simulate streaming, I ONLY ALLOW myself to view the file ONE LINE at a time, and I MUST output updated information after each line read (and even close the filehandle to the output file)
	with open(output_path, 'a') as out:
		# reading the file in binary mode seems to be more tolerant, so we convert each line to a str manually
		with open(input_path, 'rb') as file:
			for line in file:
				# the saddest way to tolerate bad characters ever:
				line = str(line)[2:-3]
				(is_valid_row, row) = row_string_to_row(line)
				if not is_valid_row:
					continue
				# before adding person, detect if they've already contributed
				donor_id = row['zip-code'] + row['name']
				is_repeat_donor = d.has_donor(donor_id)
				# add person
				d.add_donor(donor_id)
				if is_repeat_donor:
					block_id = row['year'] + row['zip-code'] + row['recipient']
					# add the contrib to the list of repeat contribs
					d.add_repeat_contrib(row['amount'], block_id)
					stats = d.stats(percentile, row['year'], row['zip-code'], row['recipient'], block_id)
					out.write(stats)
	print('Streaming simulation complete!!  See output file {}'.format(output_path))
	return d
