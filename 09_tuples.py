def main():
	a = (1, 2, 3)
	print 'Tuple a = ' + str(a)
	print 'Length of tuple = ' + str(len(a))
	
	print '\n----\nTuples Sorting - \n'
	list_of_tuples = [(1, 'b'), (2, 'a'), (1, 'a')]
	print 'list_of_tuples => ' + str(list_of_tuples)
	list_of_tuples = sorted(list_of_tuples)
	print 'After sorting'
	print 'list_of_tuples => ' + str(list_of_tuples)

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
