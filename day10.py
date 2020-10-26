from collections import deque

ptr = skip = 0
rope = deque(range(5))
inputs = [3, 4, 1, 5]
rope = deque(range(256))
inputs = [106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118]

for x in inputs:
	work = list(rope)
	rope = deque(list(reversed(work[:x])))
	rope.extend(work[x:])
	rope.rotate(-x-skip)
	ptr += x+skip
	skip += 1

rope.rotate(ptr)
print("#1",rope[0]*rope[1])

suffix = [17, 31, 73, 47, 23]

rope = deque(range(256))

input = '106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118' #'AoC 2017' #'1,2,3'
inputs = list(map(ord, list(input)))
inputs.extend(suffix)

ptr = skip = 0

for _ in range(64):
	for x in inputs:
		work = list(rope)
		rope = deque(list(reversed(work[:x])))
		rope.extend(work[x:])
		rope.rotate(-x-skip)
		ptr += x+skip
		skip += 1

rope.rotate(ptr)

sparse = list(rope)
dense = []

from functools import reduce
from operator import xor

for x in range(16):
	dense.append(reduce(xor, sparse[x*16:x*16+16]))

print("#2",''.join(map("{:02x}".format, dense)))
