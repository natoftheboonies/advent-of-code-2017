from collections import deque


def sample():
	spinlock = deque([0])
	spin = 3
	for c in range(1,2018):
		# over-rotate to append
		spinlock.rotate(-spin-1)
		spinlock.append(c)
		spinlock.rotate(1) # de-rotate so cursor at inserted
	spinlock.rotate(3)
	print(list(spinlock)[0:7])


def part1():
	spinlock = deque([0])
	spin = 386
	for c in range(1,2018):
		# over-rotate to append
		spinlock.rotate(-spin-1)
		spinlock.append(c)
		spinlock.rotate(1) # de-rotate so cursor at inserted	
	print('#1',list(spinlock)[1])

def part2dumb():
	spinlock = deque([0])
	spin = 386
	# value after 0
	result = None
	for c in range(1,50000000):
		# over-rotate to append
		spinlock.rotate(-spin-1)
		spinlock.append(c)
		spinlock.rotate(1) # de-rotate so cursor at inserted	
		if spinlock[-1] == 0:
			result = spinlock[0]
	print('#2',result)	

def part2():
	spin = 386
	pos = 0
	result = None
	for c in range(1,50000000):
		pos = (pos+spin)%c
		if pos == 0:
			result = c
		pos += 1
	print('#2',result)	

def main():
	#sample()
	part1()
	part2()

if __name__ == '__main__':
	main()