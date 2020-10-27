
sample = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
""".splitlines()

with open('input19','r') as fp:
	sample = fp.readlines()

maze = []
for x in sample:
	if len(x) > 0:
		maze.append([c for c in x])

start = (maze[0].index('|'),0) # x,y

d = (0,1)

letters = []

#print(start, len(maze),len(maze[0]))

steps = 0
cur = start
while True:
	found = maze[cur[1]][cur[0]]
	if found in '|-':
		move = (cur[0]+d[0],cur[1]+d[1])
		#print('move',d,'to',move)
	elif found.isalpha():
		letters.append(found)
		move = (cur[0]+d[0],cur[1]+d[1])
		#print('move',d,'to',move)	
	elif found == '+':
		look = [(0,1),(1,0),(0,-1),(-1,0)]
		look.remove((-d[0],-d[1]))
		#print('look',look)
		for l in look:
			see = (cur[0]+l[0],cur[1]+l[1])
			if see[1] < len(maze) and see[0] < len(maze[0]) and maze[see[1]][see[0]] != ' ':
				d = l
				move = (cur[0]+d[0],cur[1]+d[1])
				break
	else:
		break
	cur = move
	steps += 1	
print('#1',''.join(letters))
print('#2',steps)



