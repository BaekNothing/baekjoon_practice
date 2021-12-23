#include <iostream>

long long fibbonachi(long long input)
{
    if (input <= 1)
        return 1;
    return fibbonachi(input - 1) + fibbonachi(input - 2);
}

int main(void)
{
    long long input;

    std::cin >> input;
    if(input == 0)
        std::cout << 0 << std::endl;
    else
        std::cout << fibbonachi(input - 1) << std::endl;
    return 0;
}