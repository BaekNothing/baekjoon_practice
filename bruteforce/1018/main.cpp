#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

void charComp(char c, char comp, int *one, int *zero)
{
	if (c == comp)
		*one += 1;
	else
		*zero += 1;
	//cout << c << " " << comp << (c == comp ? " OK" : " KO") << "\n";
}

void strComp(char c, int h, int g, int *one, int *zero)
{
	if (h % 2 == 0)
	{
		if (g % 2 == 0)
			charComp(c, 'B', one, zero);
		else
			charComp(c, 'W', one, zero);
	}	
	else
	{
		if (g % 2 == 0)
			charComp(c, 'W', one, zero);
		else
			charComp(c, 'B', one, zero);
	}
//	cout << c << "\n";
}


int checker(char **c, int width, int height)
{
	int counter_zero;
	int	counter_one;
	int result;

	result = 2501;
	for (int i = 0; i <= height - 8; i++)
	{
		for (int k = 0; k <= width - 8; k++)
		{
			counter_zero = 0;
			counter_one = 0;
			for (int h = 0; h < 8; h++)
			{	
				for (int g = 0; g < 8; g++)
					strComp(*(*(c + i + h) + k + g), h, g, &counter_one, &counter_zero);
			}
//	cout << "one " << counter_one << " zero " << counter_zero << " result " << result << endl;
			if ((counter_one < counter_zero ? counter_one : counter_zero) < result)
				result = counter_one < counter_zero ? counter_one : counter_zero;
		}
	}
	return (result);
}

int main(void)
{
	int width, height;
	char **c;
	int counter;

	cin >> height >> width;
	c = (char **)malloc(sizeof(string) * (height + 1));
	counter = 0;
	while (counter < height)
	{
		*(c + counter) = (char *)malloc(sizeof(char) * (width + 1));
		cin >> *(c + counter);
		counter++;
	}
	cout << checker(c, width, height) << "\n";
	exit (0);
}
