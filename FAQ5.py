mass = [1,2,3,4,4,5,6,7,7]
m = {}
for i in mass:
	if i in m:
		m[i] += 1
		print ("Повторяющееся число:" , i)
	else:
		m[i] = 1
