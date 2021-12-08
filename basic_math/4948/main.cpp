#include <iostream>
#include <cstring>
#include <cstdio>

int countDecimal(int start, int pre, int ary[250000]);

int main(){
	int start;
	int pre = -1;
	int ary[250000];

	memset(ary, 0, sizeof(int) * 250000);
	while(true)
	{
		scanf("%d", &start);
		if(start == 0)
			break;
		printf("%d\n", countDecimal(start, pre, ary));
		pre = start;
	}
}

int countDecimal(int start, int pre, int ary[250000]){
	int end;
	int counter = 0;
	
	end = start * 2;
	if(pre != -1)
		counter = pre;
	ary[0] = 1;
	ary[1] = 1;	
	while(counter <= end)
	{
		if(ary[counter] == 1)
		{
		}
		else
		{
			int dup = 2;
			while(counter * dup <= end)
			{
				ary[counter * dup] = 1;
				dup++;
			}
		}
		counter++;
	}
	start++;
	counter = 0;
	while(start <= end)
	{
		if(ary[start] == 0)
			counter++;
		start++;
	}

	return (counter);
}
