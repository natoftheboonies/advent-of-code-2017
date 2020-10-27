import day10

hexstuff = '0123456789abcdef'

def hex2bin(hash):
	return ''.join(map('{0:04b}'.format,[hexstuff.index(x) for x in hash]))

def part1(input):
	used = 0
	for x in range(128):
		hash = day10.part2(input+'-'+str(x))
		used += hex2bin(hash).count('1')
	return used

def sample():
	sample = 'flqrgnkx'
	for x in range(8):
		hash = day10.part2(sample+'-'+str(x))
		print(hex2bin(hash)[:8])
	print('sample',part1(sample))

def main():
	#sample()	
	input = 'ljoxqyyw'
	print('#1',part1(input))


if __name__ == '__main__':
	main()

mine = 'a0c20170'
