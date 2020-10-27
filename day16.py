from collections import deque


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def sample():
	dancers = list(char_range('a','e'))
	inst = 's1,x3/4,pe/b'.split(',')
	print(dance(dancers,inst))

def dance(dancers,moves):
	dancers = deque(dancers)
	for m in moves:
		if m.startswith('s'):
			dancers.rotate(int(m[1:]))
		elif m.startswith('x'):
			x1, x2 = map(int,m[1:].split('/'))
			tmp = dancers[x2]
			dancers[x2] = dancers[x1]
			dancers[x1] = tmp
		elif m.startswith('p'):
			d1, d2 = m[1:].split('/')
			x1 = dancers.index(d1)
			x2 = dancers.index(d2)
			tmp = dancers[x2]
			dancers[x2] = dancers[x1]
			dancers[x1] = tmp
			
	return list(dancers)

def input():
	dancers = list(char_range('a','p'))
	with open('input16','r') as fp:
		moves = fp.read().strip().split(',')
	return dancers, moves

def part1():
	end = dance(*input())
	print('#1',''.join(end))

def part2():
	# find the loop:
	dancers, moves = input()
	start = dancers[:]
	loop = 0
	while True:
		loop+= 1
		dancers = dance(dancers,moves)
		if dancers==start:
			break
	#print('loop at',loop)
	remain = int(1e9)%loop
	for _ in range(remain):
		dancers = dance(dancers,moves)
	print('#2',''.join(dancers))

def main():
	#sample()
	part1()
	part2()
	
if __name__ == '__main__':
	main()
