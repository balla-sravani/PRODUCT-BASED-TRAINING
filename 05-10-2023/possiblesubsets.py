def fun(l,target):
    def track(start,sum,subset):
        if sum==target:
            res.append(subset[:])
            return
        if sum>target or start==len(l):
            return 
        subset.append(l[start])
        track(start+1,sum+l[start ],subset)
        subset.pop()
        track(start+1,sum,subset)
    res=[]
    track(0,0,[])
    return res

l=list(map(int,input().split()))
target=int(input())
result=fun(l,target)
print(result)
    
        