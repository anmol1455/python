a="this is as cat bro"
b=a.split()
for i,n in enumerate(b):
	if(i%2==0):
		print(n[::-1])
	else:
		print(n)
