
input = 312051

sample =  input#1024 # 12 23

"""
bottom right corners 1^2, 3^2, 5^2, 7^2, ...

12 is 3 more than 9, and 13 less than 25
23 is 14 more than 9 and 2 less than 25

1 1
3 9
5 25
7 49
9 81
11 121
13 169
15 225
17 289
19 361
21 441
23 529
25 625
27 729
29 841
31 961
33 1089
35 1225

12 is on ring 3, had 5 per side
	2 to middle, already 1 so 1

23 is on ring 3, has 5 per side
	corners are 25,21,17,13 (-4)
	so to get to middle, 5-1/2=2, but we alreday 2 so 0
	then right-1 in, so 2. 2+0=2
1024 is on ring 17, has 33 per side
	corners are 1089, 1057, 1025, 993
		so to get to middle, (33-1)/2=16 spaces, but we alredy 1 so 15.
		then ring-1 in, so 16.  15+16=31
"""

ring = 1

while pow(ring*2-1,2) < sample:
	ring += 1
perside = ring*2-1

print ('ring',ring, perside)
corners = [pow(perside,2)-(perside-1)*x for x in range(4)]
corner = min([c for c in corners if c > sample])
diff = corner - sample
dist1 = abs(int((perside-1)/2-diff))
print("#1",dist1+ring-1)

"""

square = prior + adjacent on ring (0 to 3 squares)


17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23  24  25


#23 has #22 + #7 + #8 + #9
so first, calc which squares to add, then add recursively.

6 -> 4 -> 2 -> 1
49, 43, 37, 31 -> 25, 21, 17, 13 -> 9,7,5,3 -> 1

hmm, let's just build the spiral


center (0,0)
x <->, y ^v
so, counter-clockwise starting right from (0,0):
 (0,0), (1,0),
 	turn ^ (1,1),
 	turn < (0,1), (-1,1),
 	turn v (-1,0), (-1,-1),
 	turn > (0,-1), (1,-1)
then (2,-1), turn ^

"""

neighbors = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

spiral = dict()
x, y = 0, 0

step = 0

#start down so we turn left
dx, dy = 0, -1

spiral[(0,0)] = 1

for _ in range(100):
	step += 1
	# turn if top right or bottom left: x == y
	# or top left: x < 0 and x == -y
	# or bottom right: x > 0 and x == -y+1 (begin next ring)
	if (x == y) or (x < 0 and x == -y) or (x > 0 and x == -y+1):
		#print(f"turn, x={x},y={y}")
		# rotate counter clockwise
		dx, dy = -dy, dx
	x, y = x+dx, y+dy
	sum = 0
	for n in neighbors:
		sum += spiral.get((x+n[0],y+n[1]),0)
	spiral[(x,y)] = sum
	if sum > input:
		print('#2',sum)
		break

