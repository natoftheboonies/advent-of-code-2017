sample = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
""".splitlines()

with open('input12','r') as fp:
	sample = fp.readlines()

network = {}
for x in sample:
	inst = x.split('<->')
	src, dst = int(inst[0]),list(map(int,inst[1].split(',')))
	network[src] = dst


def findnetwork(start):
	found = set()
	found.add(start)

	while True:
		cur = set(found)
		for x in network:
			for y in cur:
				if x in network[y]:
					found.add(x)
		if cur == found:
			# nobody new
			break	
	return found		

print('#1',len(findnetwork(0)))

found = []
groups = 0

for x in network:
	if x in found:
		continue
	groups += 1
	found.extend(findnetwork(x))

print('#2',groups)