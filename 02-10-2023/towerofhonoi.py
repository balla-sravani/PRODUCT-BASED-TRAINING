def toh(n,src,aux,des):
    if n==0:
        return 
    if n==1:
        return 1
    else:
        return toh(n-1,src,des,aux)+1+toh(n-1,aux,src,des)
n=int(input())
print(toh(n,'src','aux','des'))
