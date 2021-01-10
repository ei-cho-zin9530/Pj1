num=int(input())
n=[]
revs=[]
for i in range(num):
	p=input()
	n.append(p)
	revs.append(p[::-1])
print()	
for i in range(len(revs)):
	if(n[i]==revs[i]):
		print("plaindrome")
	else:
		print("not plaindrome")