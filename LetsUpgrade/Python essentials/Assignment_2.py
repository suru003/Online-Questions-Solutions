s=-1
while(s!=0):
	s = int(input("send me your plane's height or 0 to exit. "),10)
	if(s==0):
		break
	if(s<=1000):
		print("Safe to land")
	elif(1000<s<5001):
		print("Bring down to 1000")
	else:
		print("Turn Around")
