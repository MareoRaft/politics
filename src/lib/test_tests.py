import pytest

from config import *
from main import main


def test_1():
	main(PATH('test', 1))

def test_2():
	main(PATH('test', 2))

def test_3():
	main(PATH('test', 3))

def test_4():
	main(PATH('test', 4))

def test_5():
	main(PATH('test', 5))

def test_6():
	main(PATH('test', 6))

def test_7():
	main(PATH('test', 7))

def test_8():
	main(PATH('test', 8))

def test_9():
	main(PATH('test', 9))
