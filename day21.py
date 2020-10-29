input = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""".splitlines()

with open('input21') as fp:
	input = fp.readlines()

rules = {}
for i in input:
	rule = i.split('=>')
	rules[tuple(rule[0].strip().split('/'))] = tuple(rule[1].strip().split('/'))

#print (rules)

def enhance(start):
	cur = tuple(start)
	#print('matching',cur)
	for _ in range(4):
		#print('cur',cur)
		if cur in rules:
			return rules[cur]
		cur_rev = tuple(''.join(reversed(x)) for x in cur)
		#print('cur_rev',cur_rev)
		if cur_rev in rules:
			return rules[cur_rev]
		cur = tuple(map(''.join,zip(*reversed(cur))))
	print('no match :(')
	return

def split(start):
	if len(start) < 4:
		return [start]
	if len(start)%2==0:
		#print('s',start)
		rows = [start[i:i+2] for i in range(0, len(start), 2)]
		#print("2",rows)
		rowcols = []			
		for x in rows:
			cols = [[y[i:i+2] for i in range(0, len(y), 2)] for y in x]
			rowcols.extend(zip(*cols))
		#print('3',rowcols)
		return rowcols
	elif len(start)%3==0:
		rows = [start[i:i+3] for i in range(0, len(start), 3)]
		rowcols = []			
		for x in rows:
			cols = [[y[i:i+3] for i in range(0, len(y), 3)] for y in x]
			rowcols.extend(zip(*cols))
		return rowcols
	else:
		print('broken')
		return
# given start ('#..#', '....', '....', '#..#')
# split1      [('#..#', '....',),('....', '#..#')]
# want to get (('#.','..'),('.#','..')),(('..','#.'),('',''))

import math

def combine(cur3):
	parts = math.isqrt(len(cur3))	
	third = len(cur3)//parts
	joined = []
	for x in range(parts):
		p = cur3[third*x:third*(x+1)]
		joined.extend(list(''.join(x) for x in zip(*p)))	
	return joined


def part1():
	start = '.#./..#/###'.split('/')
	cur = enhance(start)

	for _ in range(4):
		divide = split(cur)
		enhanced = [enhance(c) for c in divide]
		joined = combine(enhanced)
		cur = joined
	result = sum([x.count('#') for x in joined])
	print('#1',result)

def part2():
	start = '.#./..#/###'.split('/')
	cur = enhance(start)

	for _ in range(17):
		divide = split(cur)
		enhanced = [enhance(c) for c in divide]
		joined = combine(enhanced)
		cur = joined
	result = sum([x.count('#') for x in joined])
	print('#2',result)
	

if __name__ == '__main__':
	part1()
	part2()