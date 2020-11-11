mass = [1,2,3,4,2,5,6,6]
s = set()
m = []
for i in mass:
	if i in s:
		continue
	s.add(i)
	m.append(i)
print(m)
