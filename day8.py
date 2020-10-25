# day8.py

from collections import defaultdict

reg = defaultdict(int)

input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".splitlines()

with open('input8','r') as fp:
	input = fp.readlines()

def evalcond(ptr, op, amt):
	amt = int(amt)
	return eval('reg[ptr]'+op+'amt')
	# if op == '<':
	# 	return reg[ptr] < amt
	# elif op == '>':
	# 	return reg[ptr] > amt
	# elif op == '==':
	# 	return reg[ptr] == amt
	# elif op == '!=':
	# 	return reg[ptr] != amt
	# elif op == '>=':
	# 	return reg[ptr] >= amt
	# elif op == '<=':
	# 	return reg[ptr] <= amt
	# else:
	# 	print('unexpected op', op)

maxreg = 0

for x in input:
	inst, cond = x.split('if')
	if evalcond(*cond.split()):
		ptr, op, amt = inst.split()
		amt = int(amt)
		if op == 'inc':
			reg[ptr]+=amt
		elif op == 'dec':
			reg[ptr]-=amt
		else:
			print('unexpected op', op)
		if reg[ptr] > maxreg:
			maxreg = int(reg[ptr])


print('#1',max(reg.values()))
print('#2',maxreg)


