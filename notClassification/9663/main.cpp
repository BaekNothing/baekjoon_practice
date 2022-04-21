#include <iostream>
#include <cstdio>

bool compUp(int src, int dest, int distance)
{
	std::cout << src << dest << distance << "\n";
	if (dest - distance == src)
		return true;
	return false;
}

bool compDown(int src, int dest, int distance)
{
	std::cout << src << dest << distance << "\n";
	if (dest + distance == src)
		return true;
	return false;
}

void printAry(int ary[16])
{
	for (int i = 1; i < 16; i ++)
		std::cout << ary[i];
	std::cout << "\n";
}

int findQueen(int index, int pos, int ary[16], int max)
{
	int result = 1;
	ary[index] = pos;

	printAry(ary);

	for (int i = 1; i < index; i++)
		if (compUp(ary[index], ary[i], index - i) ||
				compDown(ary[index], ary[i], index - i) ||
			  ary[index] == ary[i])
					return(0);
	if(index < max)
		result += findQueen(index + 1, 1, ary, max);
	if(pos < max)
		result += findQueen(index, pos + 1, ary, max);
	if (index == max)
		return (result);
	return (0);
}

int main(void)
{

	int ary[16];
	for (int i = 0; i < 16; i++)
		ary[i] = 0;
	int max = 0;
	int result = 0;

	std::cin >> max;
	result = findQueen(1, 1, ary, max);
	std::cout << result;

  return (0);
}
