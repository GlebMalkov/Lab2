mas=[]
for i in range(int(input())):
	mas.append(int(input()))

def minn(mas):
	a=min(mas)
	return a

def avg(mas):
	s=0
	for x in mas:
		s += x
	return s/len(mas)
	
print(minn(mas))
print(avg(mas))

	
