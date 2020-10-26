input = """0: 3
1: 2
4: 4
6: 4""".splitlines()

with open('input13','r') as fp:
	input = fp.readlines()

from pprint import pprint

def playgame():
	severity = 0
	delays = [0]
	layers = {}
	for x in input:
		layer, depth = map(int,x.split(':'))
		# layer = repr, dir
		layers[layer] = ([0]*depth, -1)
		layers[layer][0][0] = 1
	for s in range(100):
		#print('round',s)
		#pprint(layers)
		delays.append(0)
		if s in layers:
			if layers[s][0][0] == 1:
				severity += s*len(layers[s][0])	
		for d in range(s+1):
			if s-d in layers:
				if layers[s-d][0][0] == 1:
					delays[d] = 1
		for l in layers:
			layer, dy = layers[l]
			pos = layer.index(1)
			#print('layer',l,'found',pos, 'dy',dy)
			if (pos == len(layer)-1 and dy == 1) or (pos == 0 and dy == -1):
				#print('switch!')
				dy = -dy
			layer[pos+dy] = 1
			layer[pos]=0
			layers[l] = (layer,dy)
		if s == max(layers):
			print("#1",severity)

		#print('round',s,delays)
		if s-delays.index(0)>max(layers):
			return delays.index(0)

	return -1

print("#2",playgame())

# ok the didn't work.  let's see if we can evaluate a packet
# where is a scanner at time n?  not just mod, because it switches direction. hmmm
"""
0 1 2 3
    4
  5
6
  7
     8
       9
    10
  11
12

so 4 has period of 6

0 1 2
4 3  
  5 6
8 7

3 has period of 4

1 2
3 4
5 6

2 has period of 2?

0 1 2 3 4 5
  9 8 7 6
10
  11

6 has period of 10

5 has period of 8

so, 2n-2 , and that will tell us when it's at the top, anyway!


then, we are caught if position % 2*range-2 == 0?
sample is caught at 0, 6
6%(2*4-2) = 0
"""





# for o in range(15):
# 	if playgame(o)==0:
# 		print('#2',o) # 1968 too low