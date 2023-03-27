n=input().split()
for i in range(len(n)-1,-1,-1):
    l=n[i]
    print(l[::-1],end=' ')