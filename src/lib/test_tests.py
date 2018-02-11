import os

import pytest

from config import *
from lib.stream import stream


def test_tests():
	stream(PATH('test', 8))

