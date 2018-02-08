""" config settings that python files can use """
from os import path
REPO_PATH = path.dirname(path.dirname(path.abspath(__file__)))

# Paths
PATH_DICT = {
	'repo': REPO_PATH,
	'input': path.join(REPO_PATH, 'input'),
	'output': path.join(REPO_PATH, 'output'),
	'tests': path.join(REPO_PATH, 'insight_testsuite/tests'),
}
def PATH(keyword, num=None):
	if num is None:
		return PATH_DICT[keyword]
	if keyword == 'test':
		return path.join(PATH_DICT['tests'], 'test_{}'.format(num))
	elif keyword == 'input':
		return path.join(PATH_DICT['tests'], 'test_{}/input'.format(num))
	elif keyword == 'output':
		return path.join(PATH_DICT['tests'], 'test_{}/output'.format(num))
	else:
		raise ValueError('Nonempty num and bad keyword.')

# Percentile
percentile_file_path = path.join(PATH('input'), 'percentile.txt')
with open(percentile_file_path) as file:
	percentile_string = file.read()
PERCENTILE = int(percentile_string.strip())
