#include <iostream>

void ft_digit(int *position, int counter)
{
	if (counter == 0)
		return;
	*position += counter % 10;
	ft_digit(position, counter / 10);
	return ;
}

int main(void)
{
	int target;
	int counter;
	int position;
	int printed;

	std::cin >> target;
	counter = 0;
	position = 0;
	printed = 0;
	while(counter < target)
	{
		counter++;
		position = counter;
		ft_digit(&position, counter);
		if (position == target)
		{
			printed = 1;
			std::cout << counter << "\n";
			break;
		}
	}
	if (!printed)
		std::cout << "0\n";
	return (0);
}
