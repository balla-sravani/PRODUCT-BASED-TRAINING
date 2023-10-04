'''
1.iterate over the matrix,when ever yoy find 1-> count ++ and start travelling recursively top,bottom,right, and left.
right->i,j+1'
left->i,j-1
top=i-1,j
bottom=i+1,j'''
l=[[0,1,0,1],[1,1,0,0],[0,0,1,0],[0,0,1,1]]
'''l=[]
for i in range(n):
    l.appned(list(map(int,input().split())))'''
n=len(l)
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
for i in range(n):
    for j in range(n):
        if l[i][j]==1: 
            count+=1
            fun(l,i,j,n)
print(count)
        



