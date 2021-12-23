#include <iostream>

long long recursion(long long n){
    if(n <= 1)
        return 1;
    return n * recursion(n - 1);
}

int main(void)
{
    long long input;

    std::cin >> input;
    std::cout << recursion(input) << std::endl;

    return 0;
}