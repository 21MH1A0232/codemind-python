n=int(input())
l=list(map(int,input().split()))
for el in l:
    if el%2==0:
        print(el,end=' ')
for el in l:
    if el%2==1:
        print(el,end=' ')
