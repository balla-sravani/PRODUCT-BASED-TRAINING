l=list(map(int,input().split()))
n=len(l)
target=int(input())
left=0
right=n-1
while left<right:
     sum=l[left]+l[right]
     if sum==target:
         print("found")
         break
     elif sum<target:
         left+=1
     else:
         right-=1