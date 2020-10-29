from collections import defaultdict

sample = """..#
#..
...""".splitlines()

with open('input22') as fp:
	sample = [l.strip() for l in fp.readlines()]


def parse_input(sample):
	infected = set()

	for y in range(len(sample)):
		cur = sample[y]
		for x in range(len(cur)):
			c = cur[x]
			if c == '#':
				infected.add((x,y))
	return infected

def part1():
	infected = parse_input(sample)
	#print(infected)

	pos = (len(sample[0])//2,len(sample)//2)
	#print(pos)
	d = (0,-1) # up
	# right: (0,-1) > (1,0) > (0,1) > (-1,0) ... -y,x
	# left: y,-x

	bursts = 0
	for _ in range(10000):
		if pos in infected:
			# turn right, clean node, move
			d = (-d[1],d[0])
			infected.remove(pos)
			pos = (pos[0]+d[0],pos[1]+d[1])
		else:
			# turn left, infect node, move
			d = (d[1],-d[0])
			infected.add(pos)
			bursts += 1
			pos = (pos[0]+d[0],pos[1]+d[1])

	print('#1',bursts)


def part2():
	infected = parse_input(sample)
	weakened = set()
	flagged = set()

	pos = (len(sample[0])//2,len(sample)//2)
	#print(pos)
	d = (0,-1) # up

	bursts = 0
	for _ in range(10000000):
		if pos in infected:
			# turn right, clean node, move
			d = (-d[1],d[0])
			infected.remove(pos)
			flagged.add(pos)
		elif pos in weakened:
			weakened.remove(pos)
			infected.add(pos)
			bursts += 1
		elif pos in flagged:
			d = (-d[0],-d[1])
			flagged.remove(pos)
		else: # clean			
			# turn left, infect node, move
			d = (d[1],-d[0])
			weakened.add(pos)
		pos = (pos[0]+d[0],pos[1]+d[1])
	print('#2',bursts)

if __name__ == '__main__':
	part1()
	part2()

