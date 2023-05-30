def rev(num):
    rev=0
    while num>0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev
n=int(input())#12
sq1=n**2#144
rsq1=rev(n)#21
sq2=rsq1**2#441
rsq2=rev(sq2)#144
if sq1==rsq2:
    print("True")
else:
    print("False")

