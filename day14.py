import day10

hexstuff = '0123456789abcdef'

def hex2bin(hash):
	return ''.join(map('{0:04b}'.format,[hexstuff.index(x) for x in hash]))

def sample():
	sample = 'flqrgnkx'
	for x in range(8):
		hash = day10.part2(sample+'-'+str(x))
		print(hex2bin(hash)[:8])
	print('sample',part1(sample))

def part1(input):
	used = 0
	for x in range(128):
		hash = day10.part2(input+'-'+str(x))
		used += hex2bin(hash).count('1')
	return used

def part2(input):
	grid = []
	for x in range(128):
		hash = day10.part2(input+'-'+str(x))
		grid.append([c for c in hex2bin(hash)])

	regions = 0
	for x in range(128):
		for y in range(128):
			if grid[y][x] == '1':
				regions += 1
				# how to grow a region? bfs, skipping if not '1'
				todo = [(x,y)]
				while todo:
					cx,cy = todo.pop()
					grid[cy][cx] = '#'	# instead of visited				
					for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
						px = cx+dx
						py = cy+dy
						if px < 128 and px >= 0 and py < 128 and py >= 0:
							if grid[py][px] == '1':
								todo.append((px,py))
	return regions

def main():
	#sample()	
	input = 'ljoxqyyw'
	print('#1',part1(input))
	print('#2',part2(input))

if __name__ == '__main__':
	main()

