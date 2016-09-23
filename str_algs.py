str1 = "hello, world"
str2 = ""
l=len(str1) - 1
for i in range(len(str1)):
	str2 += str1[l]
	l=l-1
print(str2)
	
