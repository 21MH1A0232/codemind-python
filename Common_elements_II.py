N,M=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
k=[]
for i in l1:
    if i not in k and i not in l2:
        k.append(i)
for j in l2:
    if j not in k and j not in l1:
        k.append(j)
print(*k)