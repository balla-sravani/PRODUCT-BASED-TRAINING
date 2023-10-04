def reverse(string):
    l = list(string)
    i=0
    j=len(l)-1
    while i<j:
        if not l[i].isalnum():
            i = i+1
        elif not l[j].isalnum():
            j = j-1
        else:
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
    rev = ''.join(l)
    return rev
string = input("Enter the String:")
print(reverse(string))
