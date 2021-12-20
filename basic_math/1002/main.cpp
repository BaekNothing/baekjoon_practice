#include <iostream>
#include <cmath>

int main(void){

    int counter;
    int xone, yone, xtwo, ytwo, radone, radtwo;
    int xpow, ypow, distance;

    std::cin >> counter;

    while(counter > 0)
    {
        distance = 0;
        std::cin >> xone >> yone >> xtwo >> ytwo >> radone >> radtwo;
        xpow = xone - xtwo > 0 ? xone - xtwo : xtwo - xone;
        ypow = yone - ytwo > 0 ? yone - ytwo : ytwo - yone;
        distance = sqrt(xpow * xpow + ypow * ypow);

        if(radone + radtwo == distance)
            std::cout << "1" << std::endl;
        else if (radone + radtwo < distance)
            std::cout << "0" << std::endl;
        else if (radone > radtwo + distance)
            std::cout << "0" << std::endl;
        else if (radtwo > radone + distance)
            std::cout << "0" << std::endl;
        else
            std::cout << "2" << std::endl;
        counter--;
    }
    return (0);
}