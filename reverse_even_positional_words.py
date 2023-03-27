s=input().split()
for i in range(len(s)):
    if(i%2==0):
        l=s[i]
        print(l[::-1],end=' ')
    else:
        print(s[i],end=' ')