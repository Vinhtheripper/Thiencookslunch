a=int(input('a'))
b=int(input('b'))
sum=0
for i in range(a,b+1):
    if i%2==0:
        sum+=i
    else:
        pass
print(sum)