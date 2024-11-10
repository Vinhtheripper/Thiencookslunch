def tinh(n):
    s=1
    i=1
    while (i<=n):
        if((i%3==0)or(i%5==0)):
            s*=i
        i+=1
    return s
print(tinh(5))