#include <iostream>

using namespace std;

int main(void)
{
	int	*w;
	int *h;
	int counter = 0;
	int result = 0;
	int temp = 0;

	cin >> counter;	
	temp = -1;
	w = (int *)malloc(sizeof(int) * counter);
	h = (int *)malloc(sizeof(int) * counter);
	while (++temp < counter)
		cin >> *(w + temp) >> *(h + temp);
	for (int i = 0; i < temp; i++)
	{
		counter = 1;
		for (int k = 0; k < temp; k++)
		{
			if (i == k)
				continue;
			if (*(w + i) < *(w + k) && *(h + i) < *(h + k))
				counter++;
		}
		cout << counter << " ";
	}
	exit(0);
}
