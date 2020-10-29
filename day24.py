sample = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""".splitlines()

with open ('input24','r') as fp:
	Xsample = fp.readlines()

ports = list()

for x in sample:
	ports.append(tuple(map(int,x.strip().split('/'))))

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
	valid_bridge = []
	for t in valid_idx:
		(x,y) = ports[t]
		valid_bridge.append([(x,y)])
		if y==edge:
			for tail in findmatch(used+[t],x):
				valid_bridge.append([(x,y)]+tail)
		elif x==edge:
			for tail in findmatch(used+[t],y):
				valid_bridge.append([(x,y)]+tail)
		else:
			print('trouble')
		# print('t',(x,y))

	if not valid_bridge:
		return valid_bridge
	maxstrength = 0
	maxbridge = None
	for bridge in valid_bridge:
		strength = sum([x+y for (x,y) in bridge])
		if strength > maxstrength:
			maxbridge = bridge
			maxstrength = strength
	return valid_bridge


starts = [(x,y) for (x,y) in ports if x==0 or y==0]
# print(starts)
maxbridge = 0
for start in starts:
	used = [ports.index(start)]
	if start[0] == 0:
		edge = start[1]
	else:
		edge = start[0]
	for tail in findmatch(used,edge):
		bridge = [start]+tail
		strength = sum([x+y for (x,y) in bridge])
		if strength > maxbridge:
			maxbridge = strength
		
print('#1',maxbridge)
	#break
