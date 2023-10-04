def check(arr, target, n):
    
    if target == 0:
        return True
    if n == 0:
        return False
        
    if arr[n-1] > target:
        return check(arr, target, n-1)
        
    return check(arr, target-arr[n-1], n-1) or check(arr, target, n-1)
arr = list(map(int,input().split(",")))
target = int(input("enter target"))
ans = check(arr, target, len(arr))
if ans == True:
    print("solution found")
else:
    print("solution not found")
 '''
def csum(nums,target):
    def track(start,sum):
        if sum==target:
            return True
        if sum>target or start==len(nums):
            return False
        if track(start+1,sum+nums[start]):
            subset.append(nums[start])
            return True
        return track(start+1,sum)
    subset=[]
    if track(0,0):
        return True,subset
    else:
        return False,[]

nums=[1,2,3,4,5]
target_sum=9
bool, subset=check_subset(nums,target_sum)
if bool:'''
