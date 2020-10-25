
sample = """5 1 9 5
7 5 3
2 4 6 8""".splitlines()

with open('input2','r') as fp:
	input = fp.readlines()

result = 0
for x in input:
	row = list(map(int,x.split()))
	result += max(row)-min(row)

print ("#1",result)

sample = """5 9 2 8
9 4 7 3
3 8 6 5""".splitlines()

result = 0
for x in input:
	row = list(map(int,x.split()))
	for i in row:
		for j in row:
			if i == j: continue
			if i%j==0:
				result += int(i/j)
print("#2",result)