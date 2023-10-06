def sum_(l,si,ei):
    if si==ei:
        return l[si]
    if si>ei:
        return -1
    mid=(si+ei)//2
    return sum_(l,si,mid)+sum_(l,mid+1,ei)
l=list(map(int,input().split()))
n=len(l)
print(sum_(l,0,n-1))