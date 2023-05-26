def primeNumber(n):
    k=0
    for i in range(1,n+1):
        if n%i==0:
            k=k+1
    if k==2:
        return 1
    else:
        return 0

n=int(input())
a=primeNumber(n)
if a==1:
    print("prime")
else:
    print("not a prime")