#include <iostream>
#include <cstdio>

void recursive(int pos, int counter, int input, int tag)
{
	int xpos;
	int ypos;

	if (counter == 1)
	{
		if (tag == 0)
			std::cout << " ";
		else
			std::cout << "*";
		if(pos % input == input - 1)
			std::cout << "\n";
		return;
	}

	xpos = pos % input % counter;
	ypos = pos / input % counter;
	if (tag == 0 || 
		(xpos / (counter / 3)) % 3 == 1 && (ypos / (counter / 3)) % 3 == 1)
		recursive(pos, counter/3, input, 0);
	else
		recursive(pos, counter/3, input, 1);
	if (counter == input && pos < input * input - 1)
		recursive(pos + 1, counter, input, 1);
}

int main(void)
{
	int counter;

	std::cin >> counter;
	recursive(0, counter, counter, 1);
	
    return (0);
}
