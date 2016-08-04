def main():
	d = {}
	d['a'] = 'alpha'
	d['b'] = 'beta'
	d['g'] = 'gamma'
	d['z'] = 'zeta'
	
	print 'Dictionary d =>\n' + str(d)
	print '\n'
	print 'd[\'a\'] = ' + d['a']
	print '\'a\' in d => ' + str('a' in d)
	print '\'x\' in d => ' + str('x' in d)
	print 'g.get(\'a\') = ' + str(d.get('a'))
	print 'g.get(\'x\') = ' + str(d.get('x'))
	
	print '\n----\n'
	print 'd.keys() => ' + str(d.keys()) + '\t(Keys are in random order)'
	print 'd.values() => ' + str(d.values()) + '\t(Values are in same random order as keys)'
	
	print '\n----\n'
	print 'Printing dictionary(hash-table) in sorted order'
	for k in sorted(d.keys()):
		print k + ' --> ' + d[k]
	
	print '\nUsing d.items() to get dictionary as a list of tuples'
	print d.items()
	for tuple in d.items():
		print str(tuple) + ' =>\t' + tuple[0] + ' --> ' + tuple[1]

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
