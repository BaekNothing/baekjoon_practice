#include <iostream>
#include <cstdio>

int main(void){

    int width, height, xpos, ypos, result;

    result = 0;
    std::cin >> xpos >> ypos >> width >> height;

    xpos = width - xpos > xpos ? xpos : width - xpos;
    ypos = height - ypos > ypos ? ypos : height - ypos;
    result = xpos < ypos ? xpos : ypos;

    std::cout << result << std::endl;

    return (0);
}