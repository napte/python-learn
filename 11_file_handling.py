import sys

def cat(filename):
	f = open(filename, 'rU')
	for line in f:
		print line,
	f.close()

def cat_in_memory_list(filename):
	f = open(filename, 'rU')
	lines = f.readlines();
	print lines
	f.close()

def read_file(filename):
	f = open(filename, 'rU')
	text = f.read()
	print text,
	f.close()

def main():
	cat(sys.argv[1])
	print '\n----\nReading file in memory as a list of lines\n'
	cat_in_memory_list(sys.argv[1])
	print '\n----\nread_file\n'
	read_file(sys.argv[1])

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
