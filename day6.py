
banks = [0,2,7,0]

input = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'.split()
banks = [int(x.strip()) for x in input]

seen = list()

count = 0
while True:
	state = tuple(banks)
	if state in seen:
		where = seen.index(state)
		print('#2',len(seen)-where)
		break
	count+=1
	seen.append(state)
	dist = max(banks)
	p = banks.index(dist)
	#print(banks,p)
	banks[p] = 0
	while dist>0:
		p += 1
		banks[p%len(banks)] += 1
		dist -= 1




print('#1',count)