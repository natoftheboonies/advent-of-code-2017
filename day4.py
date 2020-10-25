input = ['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa']

with open('input4', 'r') as fp:
	input = fp.readlines()

count = 0
for x in input:
	words = x.split()
	wordSet = set(words)
	if len(words) == len(wordSet):
		print(x, 'good')
		count += 1
	else:
		print(x, 'bad')

print(count)

#input.append('abcde xyz ecdab')

count = 0
for x in input:
	words = x.split()
	words = [''.join(sorted(w)) for w in words]
	wordSet = set(words)
	if len(words) == len(wordSet):
		print(x, 'good')
		count += 1
	else:
		print(x, 'bad')

print(count)