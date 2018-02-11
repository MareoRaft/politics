import sys

from lib.stream import stream

if sys.version_info[0] < 3:
	raise SystemExit('Please use Python version 3.')

if __name__ == '__main__':
	dir_path = PATH('repo')
	stream(dir_path)
