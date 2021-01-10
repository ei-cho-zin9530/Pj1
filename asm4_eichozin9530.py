num=int(input("Enter a number:"))
if num%2 == 0:
	print("Even")
else:
	print("Odd")
if num>-1 and num<=19:
    print("E")
elif num>19 and num<=39:
    print("D")
elif num>39 and num<=59:
    print("C")
elif num>59 and num<=79:
    print("B")
elif num>79 and num<=100:
    print("A")
else:
    print("Invalid")