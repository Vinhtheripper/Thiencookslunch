import math
n=int(input('Nhập:'))
sum=math.sqrt(n)
for i in range(n-1,0,-1):
    sum=math.sqrt(i+sum)
print(sum)

