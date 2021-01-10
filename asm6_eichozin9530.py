mark = [ ]
A=0
B=0
C=0
D=0
E=0
N=0
while True:
	option = input('Enter (A, P, E): ')
	if option.upper() == 'A':
		         num = int(input('Enter mark: '))
		         mark.append(num)
	elif option.upper() == 'P':
		           E = 0
		           D = 0
		           C = 0
		           B = 0
		           A = 0
		           N = 0
		           for i in range(len(mark)):
		           
		           	if mark[i]>=0 and mark[i]<20:
		           	       E += 1
		           	elif mark[i]>=20 and mark[i]<40:
		           		   D += 1
		           	elif mark[i]>=80 and mark[i]<=100:
		           		   A += 1
		           	elif mark[i]>=60 and mark[i]<80:
		           		   B += 1
		           	elif mark[i]>=40 and mark[i]<60:
		           		   C += 1
		           	else:
		           		    N += 1
		               
		           print('Grade-E: ', E)
		           print('Grade-D: ', D)
		           print('Grade-C: ', C)
		           print('Grade-B: ', B)
		           print('Grade-A: ', A)
		           print('Invalid: ', N)
	elif option.upper() == 'E':
		    break
	else:
		    print('Invalid input')
	
	