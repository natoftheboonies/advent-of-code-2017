input = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".splitlines()

with open('input7','r') as fp:
	input = fp.readlines()

blah = dict()
fat = dict()

for t in input:
	inst = t.split('->')
	tower, weight = inst[0].split()
	weight = int(weight[1:-1])
	if len(inst)>1:
		holds = [x.strip() for x in inst[1].split(',')]
	else:
		holds = None
	blah[tower] = holds
	fat[tower] = weight
	#print(tower, weight, holds)

towers = set(blah.keys())

for k, _ in blah.items():
	for _, v in blah.items():
		if v and k in v:
			towers.remove(k)

bottom = towers.pop()
print("#1",bottom)


def weight(twr):
	f = fat[twr]
	if blah[twr]:
		weights = [weight(x) for x in blah[twr]]
		if len(set(weights)) != 1:
			over = max(weights)-min(weights)
			who = blah[twr][weights.index(max(weights))]
			print(who, fat[who],'->',fat[who]-over)
		f += sum(weights)

	return f


print(weight(bottom))



