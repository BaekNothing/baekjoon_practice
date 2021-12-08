#include <iostream>
#include <cstring>

int main(){
	int start;
	int end;
	int ary[1000001];
	int counter = 0;

	memset(ary, 0, sizeof(int) * 1000001);
	std::cin >> start;
	std::cin >> end;

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
	while(start <= end)
	{
		if(ary[start] == 0)
			std::cout << start << std::endl;
		start++;
	}
}
