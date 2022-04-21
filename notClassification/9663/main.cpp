#include <iostream>
#include <cstdio>

bool compUp(int src, int dest, int distance)
{
	if (dest - distance == src)
		return true;
	return false;
}

bool compDown(int src, int dest, int distance)
{
	if (dest + distance == src)
		return true;
	return false;
}

int findQueen(int index, int pos, int ary[15], int max)
{
	int result = 1;
	ary[index] = pos;

	//std::cout << index << ", " << pos << ", " << max << "\n" ;
	for (int i = 0; i < 15; i ++)
	 	std::cout << ary[i];
	std::cout << "\n";

	for (int i = 0; i < index; i++)
	{
		if (compUp(ary[index], ary[i], index - i) ||
				compDown(ary[index], ary[i], index - i) ||
			  ary[index] == ary[i])
		{
				std::cout << ary[index] << " " << ary[i] << "\n";
				if(pos <= max)
				{
					std::cout << "true" << "\n";
					result += findQueen(index, pos + 1, ary, max);
				}
				else
				{
					std::cout << "false" << "\n";
					return(0);
				}
		}
	}
	if(index < max)
		result += findQueen(index + 1, 1, ary, max);
	if (index == max)
		return (result);
	return (0);
}

int main(void)
{

	int ary[15];
	for (int i = 0; i < 15; i++)
		ary[i] = 0;
	int max = 0;
	int result = 0;

	std::cin >> max;
	result = findQueen(0, 1, ary, max - 1);
	std::cout << result;

  return (0);
}
