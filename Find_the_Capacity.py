S,T,B=map(int,input().split())
C=2*S*T*B*512
c=C//1024
s=str(c)
a="KB"
print(s+a)