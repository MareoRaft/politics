import sys
import os

from config import PATH, get_percentile
from lib.helpers import row_string_to_row, get_donor_id, get_block_id
from lib.data_container import Donors, Contributions
from lib.stream import stream, clear

def process_line(line, percentile, donors, contribs):
	(is_valid_row, row) = row_string_to_row(line)
	if not is_valid_row:
		return None
	# Add donor to list.  They cannot get added twice since the 'add' method is idempotent.
	donor_id = get_donor_id(row)
	donors.add(donor_id, row['year'])
	# If the donor is making a 'repeat contribution', record it in the contribution list.
	is_repeat_donor = donors.is_repeat(donor_id, row['year'])
	if is_repeat_donor:
		block_id = get_block_id(row)
		contribs.add(row['amount'], block_id)
		# Output the statistics line to repeat_donors.txt.
		stats_string = contribs.stats(percentile, row['year'], row['zip-code'], row['recipient'], block_id)
		return stats_string

def main(dir_path):
	input_path = os.path.join(dir_path, 'input/itcont.txt')
	output_path = os.path.join(dir_path, 'output/repeat_donors.txt')
	percentile_path = os.path.join(dir_path, 'input/percentile.txt')

	percentile = get_percentile(percentile_path)
	donors = Donors()
	contribs = Contributions()

	# Before beginning, clear the output file.
	clear(output_path)
	stream(input_path, output_path, process_line, percentile, donors, contribs)

	# Only for testing purposes:
	return donors


if __name__ == '__main__':
	main(PATH('repo'))

