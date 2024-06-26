def squr(numner,epsilon=1e-6):
    if number<0:
        raise ValueError("cannot compute square")
    if number<1:
        left,right=number,1
    else:
        left,right=0,number
    while abs(left - right)>epsilon:
        mid=(left+right)/2
        mid_squared=mid*mid
        if mid_squared<number:
            left=mid
        else:
            right=mid
    return (left+right)/2
number=int(input())
res=squr(number)
print(f"the square root of {number} is apporximately",res)