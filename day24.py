sample = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""".splitlines()

with open ('input24','r') as fp:
	sample = fp.readlines()

ports = list()

for x in sample:
	ports.append(tuple(map(int,x.strip().split('/'))))

dups = [(x,y) for (x,y) in ports if x==y]
#ports = [(x,y) for (x,y) in ports if x!=y]
# print(ports)

def findmatch(used,edge):
	# print('u',used)
	valid_idx = []
	for idx,(x,y) in enumerate(ports):
		if idx in used:
			continue
		if x==edge or y==edge:
			valid_idx.append(idx) 
	# print('v',valid_idx)
	maxstrength = 0
	for t in valid_idx:
		(x,y) = ports[t]
		if x+y > maxstrength:
			maxstrength = x+y
		if y==edge:
			strength = x+y+findmatch(used+[t],x)
			if strength > maxstrength:
				maxstrength = strength
		elif x==edge:
			strength = x+y+findmatch(used+[t],y)
			if strength > maxstrength:
				maxstrength = strength				
		else:
			print('trouble')
		# print('t',(x,y))
	return maxstrength

def part1():
	starts = [(x,y) for (x,y) in ports if x==0 or y==0]
	# print(starts)
	maxbridge = 0
	for start in starts:
		used = [ports.index(start)]
		if start[0] == 0:
			edge = start[1]
		else:
			edge = start[0]
		strength = start[0]+start[1]+findmatch(used,edge)
		if strength > maxbridge:
			maxbridge = strength
			
	print('#1',maxbridge)
		#break


def findlongest(used,edge):
	# print('u',used)
	valid_idx = []
	for idx,(x,y) in enumerate(ports):
		if idx in used:
			continue
		if x==edge or y==edge:
			valid_idx.append(idx) 
	# print('v',valid_idx)
	valid_bridge = []
	for t in valid_idx:
		(x,y) = ports[t]
		valid_bridge.append([(x,y)])
		if y==edge:
			for tail in findlongest(used+[t],x):
				valid_bridge.append([(x,y)]+tail)
		elif x==edge:
			for tail in findlongest(used+[t],y):
				valid_bridge.append([(x,y)]+tail)
		else:
			print('trouble')
		# print('t',(x,y))

	if not valid_bridge:
		return valid_bridge

	longest = max([len(x) for x in valid_bridge])
	#print(longest)
	return [x for x in valid_bridge if len(x) == longest]

def part2():

	starts = [(x,y) for (x,y) in ports if x==0 or y==0]
	# print(starts)
	maxlen = 0
	valid_bridge = []
	for start in starts:
		used = [ports.index(start)]
		if start[0] == 0:
			edge = start[1]
		else:
			edge = start[0]
		for tail in findlongest(used,edge):
			#print(tail)
			bridge = [start]+tail
			if len(bridge) >= maxlen:
				valid_bridge.append(bridge)
				maxlen = len(bridge)
	
	longest = max([len(x) for x in valid_bridge])
	#print(longest)
	valid_bridge = [x for x in valid_bridge if len(x) == longest]


	maxbridge = max([sum([x+y for (x,y) in bridge]) for bridge in valid_bridge])
	# strength = sum([x+y for (x,y) in bridge])
	# if strength > maxbridge:
	# 	maxbridge = strength


			
	print('#2',maxbridge)


if __name__ == '__main__':
	# optimization: Exclude dupes from the calculation and add them back at end.
	# https://www.reddit.com/r/adventofcode/comments/7lunzu/2017_day_24_so_can_it_be_done_more_efficiently/
	#print(dups)
	part1()
	part2()