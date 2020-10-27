
class Duet(object):
	"""docstring for Duet"""
	def __init__(self, id):
		super(Duet, self).__init__()
		self.id = id
		self.register = {'p':self.id}
		self.messages = []		
		self.x = 0
		self.partner = None
		self.stuck = False
		self.done = False
		self.sent = 0

	def regval(self, arg):
		try:
			return int(arg)
		except ValueError:	
			return self.register.get(arg,0)

	def run(self):
		if self.done or self.x < 0 or self.x >= len(inst):
			self.done = True
			return

		todo = inst[self.x][0]
		arg = inst[self.x][1:]
		#print(f"prog {self.id}",arg)
		if todo == 'snd':
			if not self.partner:
				self.messages.append(self.regval(arg[0]))
			else:
				self.partner.messages.append(self.regval(arg[0]))
				self.partner.blocked = False
				self.sent+=1
		elif todo == 'set':
			self.register[arg[0]]=self.regval(arg[1])
		elif todo == 'add':
			self.register[arg[0]]=self.regval(arg[0])+self.regval(arg[1])
		elif todo == 'mul':
			self.register[arg[0]]=self.regval(arg[0])*self.regval(arg[1])
		elif todo == 'mod':
			self.register[arg[0]]=self.regval(arg[0])%self.regval(arg[1])
		elif todo == 'rcv':
			#if self.regval(arg[0]) != 0:
				#print("exit singing: {}".format(self.lastSound))
			if not self.partner: # part1 mode
				return self.messages.pop()
			else:
				if len(self.messages) > 0:
					self.register[arg[0]] = self.messages.pop(0)
				else:
					self.stuck = True
					return
		elif todo == 'jgz':
			if self.regval(arg[0]) > 0:
				#print ("jgz {}".format(regval(arg[1])))
				self.x += self.regval(arg[1])
				return
		self.x += 1
		self.stuck = False

	def done_or_stuck(self):
		return self.done or self.stuck	
		

inst = []
with open('./input18') as fp:
	inst = [line.strip().split(' ') for line in fp.readlines()]

def part1():
	duet = Duet(0)
	result = None
	while not result:
		result = duet.run()
	print('#1',result)

def part2():
	duet0 = Duet(0)
	duet1 = Duet(1)
	duet0.partner = duet1
	duet1.partner = duet0
	count = 0
	while not (duet0.done_or_stuck() and duet1.done_or_stuck()):
		duet0.run()
		duet1.run()
	print('#2',duet1.sent)

def main():
	part1()
	part2()

if __name__ == '__main__':
	main()



	

