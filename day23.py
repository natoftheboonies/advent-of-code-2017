class Duet2(object):
	"""docstring for Duet"""
	def __init__(self, id):
		super(Duet2, self).__init__()
		self.id = id
		self.register = {'a':self.id}
		self.messages = []		
		self.x = 0
		self.partner = None
		self.stuck = False
		self.done = False
		self.sent = 0
		self.mulcount = 0

	def regval(self, arg):
		try:
			return int(arg)
		except ValueError:	
			return self.register.get(arg,0)

	def run(self):
		if self.done or self.x < 0 or self.x >= len(inst):
			self.done = True
			return
		#print(self.x+1, ' '.join(inst[self.x]))
		todo = inst[self.x][0]
		arg = inst[self.x][1:]
		#print(f"prog {self.id}",arg)
		if todo == 'set':
			self.register[arg[0]]=self.regval(arg[1])
		elif todo == 'sub':
			self.register[arg[0]]=self.regval(arg[0])-self.regval(arg[1])			
		elif todo == 'mul':
			self.register[arg[0]]=self.regval(arg[0])*self.regval(arg[1])
			self.mulcount += 1
		elif todo == 'jnz':
			if self.regval(arg[0]) != 0:
				#print ("jgz {}".format(regval(arg[1])))
				self.x += self.regval(arg[1])
				return				
		self.x += 1
		self.stuck = False

	def done_or_stuck(self):
		return self.done or self.stuck	


inst = []
with open('./input23') as fp:
	inst = [line.strip().split(' ') for line in fp.readlines()]

def part1():
	duet = Duet2(0)
	result = None
	while not duet.done:
		result = duet.run()
	print('#1',duet.mulcount)


def part2x():
	duet = Duet2(1)
	result = None
	abort = 0
	print()
	while not duet.done and abort < 500:
		#print(duet.register)
		abort += 1
		result = duet.run()
	print('#2',duet.register)

def part2():
	# help from https://github.com/dp1/AoC17/blob/master/day23.5.txt
	count = 0
	for i in range(106500,123500+1,17):
		for j in range(2, i):
			if (i % j) == 0:
				count += 1
				break
	print('#2',count)


if __name__ == '__main__':
	part1()
	part2()	