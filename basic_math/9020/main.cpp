#include <iostream>
#include <cstdio>
#include <queue>

int isDecimal(int number);

int main()
{
    int number = 0;
    std::queue <int> q;
    int first = 0;
    int second = 0;
    int counter = 0;

    scanf("%d", &counter);
    while(counter > 0)
    {
        scanf("%d", &number);
        q.push(number);
        counter--;
    }
    while(!q.empty())
    {
        number = q.front();
        q.pop();
        first = number / 2;
        second = number - first;
        while(first >= 2)
        {
            if (isDecimal(first) && isDecimal(second))
            {        
                printf("%d %d\n", first, second);
                break;
            }
            first--;
            second = number - first;
        }
        counter--;
    }
    return 0;
}

int isDecimal(int number)
{
    int counter = 2;
    if (number == 2)
        return 1;
    while(counter * counter <= number)
    {
        if(number % counter == 0)
        {
            return 0;
        }
        counter++;
    }
    return 1;
}