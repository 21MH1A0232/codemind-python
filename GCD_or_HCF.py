def hcfnaive(a,b):
    if(b==0):
        return abs(a)
    else:
        return hcfnaive(b,a%b)
m,n=map(int,input().split())
r=hcfnaive(m,n)
print(r)