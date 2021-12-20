#include <iostream>

int main(void)
{
    double radius;
    double pi = 3.141592653;

    radius = 0;
    std::cin >> radius;
    std::cout.precision(8);
    printf("%.10lf\n", radius * radius * pi);
    printf("%.10lf\n", 2 * radius * radius);
    // std::cout << radius * radius * pi << std::endl;
    // std::cout << 2 * radius * radius << std::endl;

    return (0);    
}