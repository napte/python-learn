#sorts by last character of the string
def my_string_sort_key_function(str):
	return str[-1]

def main():
	a = [1, 2, 3]
	print 'List a = ' + str(a)
	b = a
	print 'List b = ' + str(b)
	print 'Doing "b=a" does "not" make a copy'
	print '\nChanging first element of List a'
	a[0] = 'Changed'
	print 'a = ' + str(a)
	print 'b = ' + str(b)
	print 'Both lists are same. Length of list = ' + str(len(a))
	
	print '\nNow let\'s make a copy'
	copy = a[:]
	print 'Copy -' + str(copy)
	copy[0] = 0;
	
	print 'Copy = ' + str(copy)
	print 'a = ' + str(a)
	print 'Copy and a are "not" same'
	
	print '\n------\n'
	print 'Trying out the "in" function'
	a = [1, 2, 3]
	print 'List a => ' + str(a)
	result = 2 in a
	print '2 in a => ' + str(result)
	result = 12 in a
	print '12 in a => ' + str(result)
	
	print '\n------\n'
	print 'Trying out the "append" and "pop" functions'
	a = [0, 1, 2, 3]
	print 'List a => ' + str(a)
	a.append(4)
	print 'List a => ' + str(a)
	a_of_0 = a.pop(0)
	print 'List a => ' + str(a)
	print 'a_of_0 = ' + str(a_of_0)
	
	print '\n------\n'
	print 'Trying out sorting functions'
	a = [4, 1, 2, 6]
	print 'List a => ' + str(a)
	a.sort()
	print 'List after calling "a.sort()" => ' + str(a)
	a = [4, 1, 2, 6]
	print '\nBack to unsorted. List a => ' + str(a)
	print '\nUsing the "sorted(iterable)" function'
	print 'sorted(a) = ' + str(sorted(a))
	print 'Note : "sorted" is more efficient'
	print 'But, the original list "a" remains unchanged'
	print 'List a => ' + str(a)
	print '\nReverse sorting with "sorted(iterable, reverse=True)"'
	reverse_sorted = sorted(a, reverse=True)
	print 'reverse_sorted => ' + str(reverse_sorted)
	
	print '\n------\n'
	a = ['aaa', 'bb', 'cccc', 'd']
	print 'List a => ' + str(a)
	print 'sorted(a) = ' + str(sorted(a))
	print 'Sorts by text'
	print '\nLet\'s sprt by length of string'
	print 'Using sorted(a, key=len) => ' + str(sorted(a, key=len))
	
	a = ['bbc', 'ooad', 'zzzz', 'cbz', 'yamaha-fz', 'aaaa', 'maruti']
	print 'List a => ' + str(a)
	print '\nUsing sorted(a, key=my_string_sort_key_function) => '
	print str(sorted(a, key=my_string_sort_key_function))

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
