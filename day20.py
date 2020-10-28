
sample="""p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>""".splitlines()

with open('input20') as fp:
	sample = fp.readlines()

particles = {}

min_accel = 1e5
blah = None
for part in range(len(sample)):
	p, v, a = sample[part].strip().split('>, ')
	p = list(map(int,p[3:].split(',')))
	v = list(map(int,v[3:].split(',')))
	a = list(map(int,a[3:-1].split(',')))

	#print(part,':',p,v,a)
	particles[part] = (p,v,a)

	accel = sum(map(abs,[x for x in a]))
	if accel < min_accel:
		min_accel = accel
		blah = part
		#print(f"{part}: {p}{v}{a} ({accel})")

# in the long term, minimum accelleration wins # at least in my data!
print('#1',blah)

for _ in range(500):
	# move the particles
	locations = {} #loc -> items
	for i in particles:
		part = particles[i]
		p, v, a = part
		for x in range(3):
			v[x]+=a[x]
			p[x]+=v[x]
		p = tuple(p)
		if p in locations:
			locations[p].add(i)
		else:
			locations[p] = set([i])
	# remove collided:
	particles = {k:v for k,v in particles.items() if len(locations[tuple(v[0])])==1}

			
print('#2',len(particles))
print()




