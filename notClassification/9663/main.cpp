#include <iostream>
#include <cstdio>

int result = 0;
int ary[15];
int max;

bool compUp(int src, int dest, int distance)
{
	if (src - distance == dest)
		return true;
	return false;
}

bool compDown(int src, int dest, int distance)
{
	if (src + distance == dest)
		return true;
	return false;
}

void printAry()
{
	// std::cout << "this is complete ary ";
	// for(int i = 0; i < 15; i++)
	// 	std::cout << ary[i];
	// std::cout << std::endl;
}

bool compAry(int index){
	printAry();
	for (int i = 0; i < index; i++)
		if (compDown(ary[index], ary[i], index - i) ||
			compUp(ary[index], ary[i], index - i) ||
			ary[index] == ary[i] )
			{ //std::cout << "index is " << index <<"false\n"; 
			  return false;}
	//std::cout << "index is " << index <<"true\n";
	return true;		
}

int findQueen(int index)
{
	if (index == max)
	{
		printAry();
		result++;
		return(0);
	}
	for (int i = 0; i < max; i++)
	{
		ary[index] = i;
		if (compAry(index))
			findQueen(index + 1);
	}
	return (0);
}

int main(void)
{
	for (int i = 0; i < 15; i++)
		ary[i] = 0;

	std::cin >> max; 
	findQueen(0);
	std::cout << result;

  return (0);
}
