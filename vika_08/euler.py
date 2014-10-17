import sys

def euler1(n):
	return sum([x for x in range(1,n) if x % 5 == 0 or x % 3 == 0])


if __name__ == '__main__':
	if(len(sys.argv) < 2):
			print 'Missing number argument'
			sys.exit(1)

	for x in sys.argv[1:]:
		print euler1(int(x))
