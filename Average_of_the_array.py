n=int(input())
l=list(map(int,input().split()))
s=0
for el in l:
    s+=el
avg=s/len(l)
print("{:.2f}".format(avg))