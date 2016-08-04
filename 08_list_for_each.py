def main():
	a = [1, 2, 3]
	print 'List a = ' + str(a)
	print 'Doing for-each loop and printing numbers and their squares\n'
	for num in a:
		print '\n------\n'
		print 'num = ' + str(num)
		print str(num) + '^2 = ' + str(num**2)
	
	print '\n------\n'
	a = [1, 2, 3, 4, 5, 6, 7, 8]
	even = []
	print 'List a => ' + str(a)
	print 'List even (empty right now) => ' + str(even)
	for num in a:
		if num%2 == 0:
			even.append(num)
	
	print 'even => ' + str(even)

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
