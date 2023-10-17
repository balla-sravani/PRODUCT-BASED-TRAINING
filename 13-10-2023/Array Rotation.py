nums=[2,3,4,5,6]
k=3
if k>=len(nums):
    k=k%len(nums)
if len(nums)==0:
    print(nums)
a=len(nums)-k
nums[:]=nums[a :]+nums[:a]
print(nums)
