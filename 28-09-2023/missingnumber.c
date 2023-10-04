#include <stdio.h>
int main()
{
    int a[]={0,1,2,3,4,6};
    int x=0,i=0;
    for(i=0;i<6;i++)
    x=x^i;
    for(i=0;i<6-1;i++)
    x=x^a[i];
    printf("%d",x);
    
}
