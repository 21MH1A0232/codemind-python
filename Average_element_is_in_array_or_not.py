n=int(input())
l=list(map(int,input().split()))
s=0
for el in l:
    s+=el
    avg=s//len(l)
if avg in l:
    print("True")
else:
    print("False")