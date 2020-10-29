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
