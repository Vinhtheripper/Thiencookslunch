import math
n=3
s=7
sum=(2*s+1)**2/n
for i in range(n-1,0,-1):
    sum=sum+(2*s+1)**2/i
print(sum)