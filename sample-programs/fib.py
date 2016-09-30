import sys

def fib(n):
	a = 0
	b = 1
	c = a + b
	for i in range(1, n):
		c = a + b
		a = b
		b = c
	
	return c

def fib_rec(n):
	if n <= 1:
		return n
	return fib_rec(n-1) + fib_rec(n-2)

def usage(program):
	print 'USAGE : python ', program, ' <n>'
	sys.exit(1)

def main():
	if len(sys.argv) != 2:
		usage(sys.argv[0])
	n = int(sys.argv[1])
	for i in range(1, n+1):
		print str(fib(i)), '\t',
	print
	for i in range(1, n+1):
		print str(fib_rec(i)), '\t',

# Standard boilerplate code that calls the main function
if __name__ == '__main__':
	main()
