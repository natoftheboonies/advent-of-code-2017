

with open('input5', 'r') as fp:
	input = [int(x) for x in fp.readlines()]

#input = [0,3,0,1,-3]

pos = 0
step = 0
while True:
	if pos > len(input)-1:
		break
	step += 1
	jmp = input[pos]
	if input[pos] < 3:
		input[pos]+=1
	else:
		input[pos]-=1
	pos+=jmp

print(step)