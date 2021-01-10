num = int(input())
count = 0
sum = 0
average = 0
for i in range(num):
      a = int(input())
      count += 1
      sum += a
average = sum / count
print(average)