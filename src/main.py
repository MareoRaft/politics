import os

from config import PATH
import lib
from lib.decorate import record_elapsed_time
from lib.data_container import DataContainer, row_string_to_row

def remove(file_path, noclobber=False):
	""" Removes a file.  If file exists and noclobber=True, it will ask if you want to overwrite it. """
	if os.path.lexists(file_path):
		if noclobber:
			proceed = input('The file {} will be overwritten.  To proceed, type "y" then RETURN.'.format(file_path))
			if proceed == "y":
				os.remove(file_path)
		else:
			os.remove(file_path)

def stream(dir_path):
	""" Simulate a data streaming situation """
	input_path = os.path.join(dir_path, 'input/itcont.txt')
	output_path = os.path.join(dir_path, 'output/repeat_donors.txt')

	percentile_path = os.path.join(dir_path, 'input/percentile.txt')
	percentile = get_percentile(percentile_path)

	# before beginning, clear output file
	remove(output_path)

	d = DataContainer()
	# To simulate streaming, I ONLY ALLOW myself to view the file ONE LINE at a time, and I MUST output updated information after each line read (and even close the filehandle to the output file)
	with open(input_path) as file:
		for line in file:
			(is_valid_row, row) = row_string_to_row(line)
			if not is_valid_row:
				continue
			d.append_row(line)
			d.sort()
			stats = d.stats()
			with open(output_path, 'w+') as out:
				out.write(stats)
	print('Streaming simulation complete!!  See output file {}'.format(output_path))

if __name__ == '__main__':
	dir_path = PATH('test', 1)
	stream(dir_path)
