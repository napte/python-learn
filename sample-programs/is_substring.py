import sys;

def is_substring(str, substring):
	match_count = 0
	match_index = 0
	i = 0
	while i < len(str):
		c = str[i]
		if c == substring[match_count]:
			if match_count == 0:
				match_index = i + 1
			match_count = match_count + 1
			if match_count == len(substring):
				return 1
			else:
				a = 0	#dummy statement
		else:
			match_count = 0
			if match_index > 0:
				i = match_index
				match_index = 0
				continue
		i = i + 1
	return 0

def usage(program):
	print 'USAGE - ', program, ' <string> <substring>'
	sys.exit(1)

def main():
	if len(sys.argv) != 3:
		usage(sys.argv[0])

	is_substr = is_substring(sys.argv[1], sys.argv[2])
	if is_substr:
		print sys.argv[2], ' IS a substring of ', sys.argv[1]
	else:
		print sys.argv[2], ' is NOT a substring of ', sys.argv[1] 

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()