lower=int(input())
upper=int(input())
for i in range(lower+1,upper-1):
	if(i>1):
		for j in range(2,i):
			if(i%j==0):
				break
		else:
			print(i)
