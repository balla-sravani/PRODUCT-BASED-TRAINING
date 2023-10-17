def knapsack(W,wt,val,n):
   dp=[[0 for x in range(W+1)] for x in range(n+1)]
   for i in range(n+1):
       for w in range(W+1):
           if w==0 or i==0:
               dp[i][w]=0
           elif wt[i-1]<=w:
                dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
           else:
                dp[i][w]=dp[i-1][w]
   return dp[n][W]
#val=[60,100,120]
#wt=[2,3,4]
#W=7
#n=3
val=list(map(int,input().split()))
wt=list(map(int,input().split()))
W=int(input())
n=int(input())
print(knapsack(W,wt,val,n))
                
    