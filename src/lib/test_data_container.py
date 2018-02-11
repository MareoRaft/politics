import os

import pytest

from config import *
from lib.helpers import get_donor_id, get_block_id
from lib.data_container import *
from lib.stream import stream


# Donors
def test_Donors_init():
	d = Donors()

def test_Donors_add():
	# one person
	d = Donors()
	row = {
		'recipient': 'C00384818',
		'name': 'ABBOTT, JOSEPH',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}
	d.add(row['zip-code'] + row['name'], row['year'])
	assert len(d.donors) == 1
	assert '02895ABBOTT, JOSEPH' in d.donors

	# two rows
	d = Donors()
	row = {
		'recipient': 'C00384818',
		'name': 'ABBOTT, JOSEPH',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}
	d.add(get_donor_id(row), row['year'])
	row = {
		'recipient': 'C00384818',
		'name': 'ABBOTT, JOSEPH 2',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}
	d.add(get_donor_id(row), row['year'])
	assert len(d.donors) == 2


# Contributions
def test_Contributions_init():
	c = Contributions()

def test_Contributions_add():
	# one contrib
	c = Contributions()
	row = {
		'recipient': 'C00384818',
		'name': 'ABBOTT, JOSEPH',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}
	b_id = get_block_id(row)
	c.add(row['amount'], b_id)
	assert len(c.contribs[b_id]) == 1

	# two rows
	c = Contributions()
	row = {
		'recipient': 'C00384818',
		'name': 'ABBOTT, JOSEPH',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}
	c.add(row['amount'], get_block_id(row))
	row = {
		'recipient': 'C00384818',
		'name': 'ABBOTT, JOSEPH 2',
		'zip-code': '02895',
		'year': '2017',
		'amount': 250,
	}
	b_id = get_block_id(row)
	c.add(row['amount'], b_id)
	assert len(c.contribs[b_id]) == 2


# stream
def test_stream():
	# a single entity
	d = stream(PATH('test', 1))
	assert len(d.donors) == 0

	# a single individual (not entity)
	d = stream(PATH('test', 2))
	assert len(d.donors) == 1

	# seven records (but only 4 donors)
	d = stream(PATH('test', 3))
	assert len(d.donors) == 4

