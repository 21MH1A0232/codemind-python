n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if l.count(i)==i and i not in a:
        a.append(i)
if len(a)==0:
    print("-1")
else:
    print("{:.2f}".format(sum(a)/len(a)))