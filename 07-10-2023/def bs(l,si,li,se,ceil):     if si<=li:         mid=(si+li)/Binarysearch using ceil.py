def bs(l,si,li,se,ceil):
    if si<=li:
        mid=(si+li)//2
        if l[mid]==se:
            return l[mid]
        if l[mid]<se:
            return bs(l,mid+1,li,se,ceil)
        if l[mid]>se:
            return bs(l,si,mid-1,se,l[mid])
    return ceil
l=list(map(int,input().split()))
s=int(input("enter search"))
n=len(l)
ceil=float('inf')
ans=bs(l,0,n-1,s,ceil)
print(ans)
