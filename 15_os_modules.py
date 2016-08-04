import os
import sys

def list_dir(dir):
	for filename in os.listdir(dir):
		print 'Filename = ' + filename
		print 'Full path = ' + os.path.join(dir, filename)
		print 'Abs Path = ' + os.path.abspath(filename)
		print

def path_exists(path):
	return os.path.exists(path)

def usage():
	sys.stderr.write('\nUSAGE:\n')
	sys.stderr.write(sys.argv[0] + ' --listdir <dir>\n')
	sys.stderr.write(sys.argv[0] + ' --path_exists <path>\n')
	sys.stderr.write(sys.argv[0] + ' --mkdir <dir>\n')

def main():
	if len(sys.argv) != 3:
		usage()
		sys.exit(1)

	cmd = sys.argv[1]
	if cmd == '--listdir':
		dir = sys.argv[2]
		list_dir(dir)
	elif cmd == '--path_exists':
		path = sys.argv[2]
		if path_exists(path):
			print 'Path ' + path + ' exists'
		else:
			print 'Path ' + path + ' does NOT exist'
	elif cmd == '--mkdir':
		dir = sys.argv[2]
		os.mkdir(dir)

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()