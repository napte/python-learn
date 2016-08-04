import sys

def cat(filename):
	try:
		f = open(filename, 'rU')
		text = f.read()
		print '\n----' + filename
		print text
		f.close()
	except IOError:
		print 'IOError for file ' + filename

def main():
	args = sys.argv[1:]
	for arg in args:
		cat(arg)

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()