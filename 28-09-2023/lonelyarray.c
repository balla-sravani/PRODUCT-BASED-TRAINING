#include <stdio.h>

int main()
{
    int n,i,res=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
        
    }
    for(i=0;i<n;i++)
    {
      res=res^a[i];
    }
    printf("%d",res);
}
    



