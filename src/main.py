from lib.decorate import record_elapsed_time

@record_elapsed_time
def do_stuff():
	print('hello.  When you are ready, hit Return.')
	input()

if __name__ == '__main__':
	do_stuff()

