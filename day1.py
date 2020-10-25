# day1.py

def captcha_sum(input):
	result = 0
	for x in range(1,len(input)):
		if input[x]==input[x-1]:
			result+=int(input[x])
	if input[x]==input[0]:
		result += int(input[x])
	return result


# samples = ["1122", "1111", "1234", "91212129"]
# for x in samples:
# 	print(x,captcha_sum(x))

with open('input1','r') as fp:
	input = fp.read().strip()

print("#1",captcha_sum(input))

def captcha_pt2(input):
	offset = int(len(input)/2)
	result = 0
	for x in range(len(input)):
		pair = (x+offset)%(offset*2)
		if input[x]==input[pair]:
			result += int(input[x])
	return result

# samples = ["1212","1221","123425","123123","12131415"]
# for x in samples:
# 	print(x,captcha_pt2(x))

print("#2",captcha_pt2(input))



