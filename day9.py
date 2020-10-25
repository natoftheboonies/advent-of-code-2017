


def readstream(sample):
	depth = result = 0
	gc = 0
	ptr = 0
	garbage = False
	while ptr < len(sample):
		#print(ptr,sample[ptr],garbage)
		if sample[ptr] == "!":
			ptr +=1
		elif garbage:
			if sample[ptr] == '>':
				garbage = False
			else:
				gc += 1
		elif sample[ptr] == '{':
			depth += 1
		elif sample[ptr] == '}':
			result += depth
			depth -= 1
		elif sample[ptr] == '<':
			garbage = True
		ptr += 1
	return result, gc

sample = '{{<!>},{<!>},{<!>},{<a>}}'


samples = """{}
{{{}}}
{{},{}}
{{{},{},{{}}}}
{<a>,<a>,<a>,<a>}
{{<ab>},{<ab>},{<ab>},{<ab>}}
{{<!!>},{<!!>},{<!!>},{<!!>}}
{{<a!>},{<a!>},{<a!>},{<ab>}}""".splitlines()

# for sample in samples:
# 	print(readstream(sample))

with open('input9','r') as fp:
	input = fp.read().strip()

print('#1',readstream(input)[0])

samples = """<>
<random characters>
<<<<>
<{!>}>
<!!>
<!!!>>
<{o"i!a,<{i<a>""".splitlines()

# for sample in samples:
# 	print(readstream(sample)[1])

print('#2',readstream(input)[1])