def isUgly(n):
    if (n == 1):#6 false
        return 1
    if (n <= 0):#6 false
        return 0
    if (n % 2 == 0):#
        return (isUgly(n // 2))#0
    if (n % 3 == 0):
        return (isUgly(n // 3))#0
    if (n % 5 == 0):
        return (isUgly(n // 5))
    return 0
n=int(input())
if(isUgly(n)==1):
    print("Ugly Number")
else:
    print("Not Ugly Number")
 