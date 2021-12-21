#include <iostream>
#include <cmath>

int main(void){

    int counter;
    int xone, yone, xtwo, ytwo, radone, radtwo;
    int xpow, ypow, distance;

    int radsum;

    std::cin >> counter;

    while(counter > 0)
    {
        distance = 0;
        std::cin >> xone >> yone >> radone >> xtwo >> ytwo >> radtwo;
        xpow = xone - xtwo;
        if(xpow < 0)
            xpow *= -1;
        ypow = yone - ytwo;
        if(ypow < 0)
            ypow *= -1;
            
        radsum = radone + radtwo;
        distance = xpow * xpow + ypow * ypow;
        if(distance != 0)
        {
            if(radsum * radsum == distance)
                std::cout << 1 << std::endl;
            else if (radsum * radsum < distance)
                std::cout << 0 << std::endl;
            else if (radone > radtwo + distance)
                std::cout << 0 << std::endl;
            else if (radtwo > radone + distance)
                std::cout << 0 << std::endl;
            else
                std::cout << 2 << std::endl;
        }
        else
        {
            if(radone == radtwo)
                std::cout << -1 << std::endl;
            else
                std::cout << 0 << std::endl;
        }
        counter--;
    }
    return (0);
}