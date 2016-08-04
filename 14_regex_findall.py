#$>python 14_regex_findall.py "blah blah asd@qwerty.com foo bar. My gmail account is nikatpict@gmail.com; whereas nik_apte@irctc.com is the IRCTC account."
['asd@qwerty.com', 'nikatpict@gmail.com', 'nik_apte@irctc.com']
import re
import sys

def get_emails(text):
	list_of_emails = re.findall('\w[\w.]*@\w[\w.]*\w', text)
	print list_of_emails

def get_users_and_servers(text):
	list_of_tuples = re.findall('(\w[\w.]*)@(\w[\w.]*\w)', text)
	print list_of_tuples

def main():
	print
	if len(sys.argv) != 2:
		print '\nUSAGE:\n' + sys.argv[0] + ' <text>'
		sys.exit(1)
	get_emails(sys.argv[1])
	print '\n--------\n'
	get_users_and_servers(sys.argv[1])

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()