import re
import sys

def match(pat, text):
	match = re.search(pat, text)
	if match:
		print '"' + match.group() + '" found in "' + text + '"'
	else:
		print 'pattern "' + pat + '" not found in text "', text  + '"'

def main():
	match('Nik', 'Welcome Nikhil the great')
	match('apt', 'Welcome Nikhil the great')
	match('\w*\sNikhil\s\w*', 'Hi Nikhil the great.')
	match('\d\s+\d\s+\d\s+\d\s+\d', '1 2    3\t4\n5') 
	if len(sys.argv) == 3:
		match(sys.argv[1], sys.argv[2])

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
