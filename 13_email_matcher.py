import re
import sys

def is_email(text):
	match = re.search('(\w[\w.]*)@(\w[\w.]*)', text)
	if match:
		print '"' + match.group() + '" found in "' + text + '"'
		if match.group() == text:
			print '\nText ' + text + ' is an email address'
			print 'Username = ' + match.group(1)
			print 'Server = ' + match.group(2)
	else:
		print 'Text "' + text  + '" (is NOT/does not contain) an email address'

def main():
	if len(sys.argv) != 2:
		print '\nUSAGE:\n' + sys.argv[0] + ' <text>'
		sys.exit(1)
	is_email(sys.argv[1])

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
