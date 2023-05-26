def rev(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
    
num=int(input())
print(rev(num))