#include <iostream>

using namespace std;

int checksix(long input, int flag)
{
    if (input / 10 != 0)
        flag += checksix(input / 10, flag);
    if (input % 10 == 6)
        flag++;
    else if (flag < 3)
        flag = 0;
    return (flag);
}

int main(void)
{
    int counter;
    int input;
    long result;

    counter = 1;
    cin >> input;
    result = 666;
    while(counter < input)
    {
        result++;
        if(checksix(result, 0) >= 3)
        {
            //cout << result << "\n";
            counter++;
        }
    }
    cout << result << "\n";
    return (0);
}