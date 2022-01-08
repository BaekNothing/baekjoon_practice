#include <iostream>
#include <cmath>

using namespace std;

void hanoi(int n, int start, int mid, int dest)
{	
	if (n == 1)
	{
		cout << start << " " << dest << endl;
		return;
	}

	hanoi(n - 1, start, dest, mid);

	cout << start << " " << dest << endl;

	hanoi(n - 1, mid, start, dest);
}

int main(void)
{
	int counter;
	cin >> counter;
	
	cout << powf(2, counter) - 1 << endl;

	hanoi(counter, 1, 2, 3);
	return (0);
}
