'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    print(i)'''
'''
n=int(input("enter the value of n:"))
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
fun(n)
'''
'''
n=int(input("enter the value of n:"))
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
fun(n)'''
n=int(input("enter"))
sum1=0
def fun(n):
    if n==0:
        return
    else:
        return sum1+fun(n-1)
print("sum= ",sum1)
fun(n)
