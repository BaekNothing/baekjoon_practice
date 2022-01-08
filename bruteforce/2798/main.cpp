#include <iostream>
#include <vector>

using namespace std;

int bruteforce(int size, int max, vector<int> v)
{
	int x = 0;
	int y = 1;
	int z = 2;
	int comp;
	int temp;

	temp = 0;
	while (x < size - 2)
	{
		y = x + 1;
		while (y < size - 1)
		{
			z = y + 1;
			while (z < size)
			{
				comp = v.at(x) + v.at(y) + v.at(z);
				if(comp > temp && comp <= max)
					temp = comp;
				z++;
			}
			y++;
		}
		x++;
	}
	return (temp);
}

int main(void)
{
	int input;
	int max;
	int counter;
	int temp;
	vector<int> v;

	counter = 0;
	cin >> input >> max;
	while(counter < input)
	{
		cin >> temp;
		v.push_back(temp);
		counter++;
	}
	cout << bruteforce(input, max, v) << "\n";
	return (0);
}
