import os

import pytest

from config import *
from lib.stream import stream


def test_1():
	stream(PATH('test', 1))

def test_2():
	stream(PATH('test', 2))

def test_3():
	stream(PATH('test', 3))

def test_4():
	stream(PATH('test', 4))

def test_5():
	stream(PATH('test', 5))

def test_6():
	stream(PATH('test', 6))

def test_7():
	stream(PATH('test', 7))

def test_8():
	stream(PATH('test', 8))

def test_9():
	stream(PATH('test', 9))
