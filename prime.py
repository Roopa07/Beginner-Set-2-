no=int(input())
if (no>1):
	for i in range (2,no):
		if(no%i==0):
			print("No")
			break
		else:
			print("Yes")
			break
else:
	print("No")
