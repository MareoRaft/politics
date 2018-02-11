import sys
import os

from config import PATH
from lib.decorate import record_elapsed_time
from lib.stream import stream

if sys.version_info[0] < 3:
	raise SystemExit('Please use Python version 3.')

if __name__ == '__main__':
	dir_path = PATH('repo')
	stream(dir_path)
