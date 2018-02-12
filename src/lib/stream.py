import os


def clear(file_path, noclobber=False):
	""" Removes a file.  If file exists and noclobber=True, it will ask if you want to overwrite it. """
	if os.path.lexists(file_path) and noclobber:
		proceed = input('The file {} will be overwritten.  To proceed, type "y" then RETURN.'.format(file_path))
		if proceed != "y":
			raise SystemExit('Cannot proceed with program until file is deleted.')
	# 'Clear' the file.  (Create new file if doesn't exist, replace content with '' if it exists.)
	with open(file_path, 'w'):
		pass

def stream(input_path, output_path, process_line, *args):
	""" Simulate a data streaming situation.  To simulate, we may only read the file ONE LINE at a time, and we must output information after that line is read, but before reading the next line.

	Params
	------
	process_line: the function which takes in each line from the input file and returns what to output to the output file
	"""

	with open(output_path, 'a') as output_file:
		# Reading the file in binary mode tolerates non-UTF-8 characters
		with open(input_path, 'rb') as input_file:
			for input_line in input_file:
				# We tolerate non-UTF-8 characters by ignoring them.  There is definitely a better way to do this, and the current method should be changed in the future (nor is the following line compatible with python2):
				input_line = str(input_line)[2:-3]
				output_line = process_line(input_line, *args)
				if output_line is not None:
					output_file.write(output_line)

