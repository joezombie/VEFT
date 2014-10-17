import sys

def even(n):
	return (n % 2 == 0)

def oddOrEven(n):
	if(even(n)):
		print 'The number', n, 'is even'
	else:
		print 'The number', n, 'is odd'
		
if __name__ == "__main__":
	if(len(sys.argv) < 2):
			print 'Missing number argument'
			sys.exit(1)

	for x in sys.argv[1:]:
		oddOrEven(int(x))
