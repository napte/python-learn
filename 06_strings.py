import sys

def hello(name):
	print
	if name.lower() == 'nikhil':
		name = name + ' the Great'
	else:
		name = name + ' you moron'
	name = name + ' !!'
	print 'Hello' , name

def print_length(name):
	print
	print len(name)
	print 'Let\'s put a fancy message'
	print "Did you notice the quote (') that got printed btw?"
	print 'There are' , str(len(name)) + ' characters in ' + name

def print_upper(name):
	print "\n"
	print name.upper() , "(Converted to uppercase)"
	print '\nBtw in Python, Strings are IMMUTABLE.. if you know what I mean'

def print_first_char(name):
	print
	print 'Your name starts with ' + name[0].upper()

def print_excluding_ends(name):
	print
	print "Your name exluding the first and last character is " + name[1:len(name)-1]

def usage(program):
	print "\n----USAGE----"
	print "python " + program + " <name>"

def main():
	if len(sys.argv) < 2:
		usage(sys.argv[0])
		sys.exit(1)
	name = sys.argv[1]
	hello(name)
	print_length(name)
	print_upper(name)
	print_first_char(name)
	print_excluding_ends(name);
	

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
