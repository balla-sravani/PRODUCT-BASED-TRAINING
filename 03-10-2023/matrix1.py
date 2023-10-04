l=[[1,0,0,1],[1,0,0,0],[1,0,1,0],[0,1,1,1]]
'''l=[]
for i in range(n):
    l.appned(list(map(int,input().split())))'''
n=len(l)
i=int(input())
j=int(input())
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
        if i<n-1:
            fun(l,i+1,j,n)
        if i>0:
            fun(l,i-1,j,n)
        if j<n-1:
            fun(l,i,j+1,n)
        if j>0:
            fun(l,i,j-1,n)
        
count=0
fun(l,i,j,n)
for k in range(n):
    for u in range(n):
        if l[k][u]==1: 
            count+=1
print(count)
