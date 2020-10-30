from collections import defaultdict

sample = """Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
""".splitlines()

with open('input25') as fp:
	sample = [x.strip() for x in fp.readlines()]

blah = iter(sample)
begin = next(blah)[-2:-1]
repeat = int(next(blah).split()[5])
rules = {}
try:
	while True:
		next(blah)
		state = next(blah)[-2:-1]
		#print(state,':')
		conds = {}
		for _ in range(2):
			cond = int(next(blah)[-2:-1])
			write = int(next(blah)[-2:-1])
			move = next(blah).split()[-1][0]
			move = -1 if move == 'l' else 1
			cont = next(blah)[-2:-1]
			#print(cond,write,move,cont)
			conds[cond] = (write,move,cont)
		rules[state] = conds
except StopIteration:
	pass

print(begin, repeat)
print(rules)

tape = defaultdict(int)
cursor = 0
nextrule = begin

for _ in range(repeat):
	rule = rules[nextrule]
	cond = rule[tape[cursor]]
	tape[cursor] = cond[0]
	cursor += cond[1]
	nextrule = cond[2]
print('#1',sum(tape.values()))

