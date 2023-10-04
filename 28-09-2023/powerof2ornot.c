#include<stdio.h>
int main()
{
	int n,count=0;
	scanf("%d",&n);
	if(n==1)
	{
		printf("not power of 2");
	}
	while(n)
	{
		count++;
		n=n&(n-1);
		
	}
	if(count==1)
	{
		printf("yes");
	}
	else
	{
		printf("no");
	}
	
} 

