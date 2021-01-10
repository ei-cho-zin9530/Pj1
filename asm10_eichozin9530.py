num=int(input())
n=[]
final=""
for i in range(num):
	str=input()
	letters=""
	words=str.split()
	for word in words:
		letters=letters+word[0]
	final=".".join(letters).upper()
	n.append(final)
print()
for i in range(len(n)):
	print(n[i])