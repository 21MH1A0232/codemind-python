num1,num2=map(int,input().split())
if num1>num2:
    max=num1
else:
    max=num2
while(True):
    if(max%num1==0 and max%num2==0):
        print(max)
        break
    max+=1