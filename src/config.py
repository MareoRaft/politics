""" config settings that python files can use """
from os import path
REPO_PATH = path.dirname(path.dirname(path.abspath(__file__)))

# Paths
PATH = {
	'repo': REPO_PATH,
	'input': path.join(REPO_PATH, 'input'),
	'output': path.join(REPO_PATH, 'output'),
	'tests': path.join(REPO_PATH, 'insight_testsuite/tests'),
}
PATH['test1'] = path.join(PATH['tests'], 'test_1')
PATH['input1'] = path.join(PATH['test1'], 'input')
PATH['output1'] = path.join(PATH['test1'], 'output')
