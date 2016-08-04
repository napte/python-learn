import sys

# This code will give an error only when you pass a name other than nikhil
# Python does NOT evaluate a line which it does not run
def hello(name):
	if name == 'Nikhil' or name == 'nikhil':
		name = name + ' the Great'
	else:
		DoesNotExist();
	name = name + ' !!'
	print 'Hello' , name

def main():
	hello(sys.argv[1])

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
