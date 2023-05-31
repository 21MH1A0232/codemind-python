n=int(input())
l=list(map(int,input().split()))
c=0
sum=0
k=[]
for el in l:
    sum=sum+el
avg=sum//len(l)
for el in l:
    if el>=avg:
        c+=1
print(c)
   
