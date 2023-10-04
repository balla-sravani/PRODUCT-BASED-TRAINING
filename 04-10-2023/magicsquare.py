n=int(input())
sq=[[0]*n for i in range(n)]#insert 0 in the matrix so that we can acsess te matrix
num=1
i=n//2#middle row
j=n-1#last column place 1 frist
while num<=(n*n):
    if i<0  and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
        if sq[i][j]:
            i=i+1
            j=j-2
            continue
        sq[i][j]=num
        num+=1
        i=i-1
        j=j+1
for i in sq:
    print(* i)# to remove commas and brackets can use *
print("magic constant is:",n*((n*n)+1)//2)
            
