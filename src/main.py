import os

from config import PATH
from lib.decorate import record_elapsed_time
from lib.stream import stream

if __name__ == '__main__':
	dir_path = PATH('test', 1)
	stream(dir_path)
