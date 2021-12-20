#include <iostream>

int main(void)
{
    int first, second, third;

    
    while (std::cin >> first >> second >> third)
    {
        if (first == 0 && second == 0 && third == 0)
            break;

        if(third * third == first * first + second * second)
            std::cout << "right" << std::endl;
        else if(first * first == second * second + third * third)
            std::cout << "right" << std::endl;
        else if(second * second == first * first + third * third)
            std::cout << "right" << std::endl;
        else
            std::cout << "wrong" << std::endl;
    }
    return (0);
}