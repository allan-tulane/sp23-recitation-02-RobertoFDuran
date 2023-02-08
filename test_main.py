from main import *

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == 2
	assert work_calc(20, 3, 2) == 3
	assert work_calc(30, 4, 2) == 1

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 1
	assert work_calc(20, 1, 2, lambda n: n*n) == 20
	assert work_calc(30, 3, 2, lambda n: n) == 30
