samples = """ne,ne,ne
ne,ne,sw,sw
ne,ne,s,s
se,sw,se,sw,sw""".splitlines()


hexsquare = """
        ------        
 ------  0, +2 ------ 
 -1, +1 ------ +1, +1  
 ------  0,  0 ------ 
 -1, -1 ------ +1, -1  
 ------  0, -2 ------ 
        ------        
"""

def reduce_moves(moves):
	if 'sw' in moves and 'ne' in moves:
		if moves['sw'] > moves['ne']:
			moves['sw'] -= moves['ne']
			moves.pop('ne')
		else:
			moves['ne'] -= moves['sw']
			moves.pop('sw')
	if 'nw' in moves and 'se' in moves:		
		if moves['nw'] > moves['se']:
			moves['nw'] -= moves['se']
			moves.pop('se')
		else:
			moves['se'] -= moves['nw']
			moves.pop('nw')
	if 's' in moves and 'n' in moves:
		if moves['s'] > moves['n']:
			moves['s'] -= moves['n']
			moves.pop('n')
		else:
			moves['n'] -= moves['s']
			moves.pop('s')
	return moves

def distance(moves):
	x = y = 0
	for d in moves:
		if 'e' in d:
			x += moves[d]
			if 's' in d:
				y -= moves[d]
			elif 'n' in d:
				y += moves[d]
		elif 'w' in d:
			x -= moves[d]
			if 's' in d:
				y -= moves[d]
			elif 'n' in d:
				y += moves[d]
		elif d == 's':
			y -= moves[d]*2
		elif d == 'n':
			y += moves[d]*2			
	#print(x,y)
	# (-355, -327)
	"""
	so go 355 ne which puts us at 0,28
	"""
	dx = abs(x)
	dy = (dx-abs(y))/2
	return abs(dx)+abs(dy)

with open('input11', 'r') as fp:
	input = fp.read().strip()

for x in [input]:
	path = x.split(',')
	moves = {}
	for p in path:
		if p in moves:
			moves[p] += 1
		else:
			moves[p] = 1
	#print moves
	moves = reduce_moves(moves)
	print("#1",distance(moves))


	maxdist = 0
	moves = {}
	for p in path:
		if p in moves:
			moves[p] += 1
		else:
			moves[p] = 1	
		cur = distance(reduce_moves(moves))
		if cur > maxdist:
			maxdist = cur
	print ('#2',maxdist)
	

	"""
	sw 3, se 2
	-1 -1
	-1 -1
	-1 -1
	+1 -1
	+1 -1
	------
	-1 -5
	so move ne 1
	1, 1
	------
	0 4
	then n y/2 times.

	alg = move left-right net of x (reduce y)
	then move y/2


	ne 2, s 2
	 1  1
	 1  1
	 0 -2
	 0 -2
	------
	+2 -2

	"""


	
	# 341 too low, as is 369
	# 743 right, but fails sample#3

