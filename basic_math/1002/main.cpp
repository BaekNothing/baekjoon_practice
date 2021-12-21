#include <iostream>
#include <cmath>

int main(void){

    int counter;
    int xone, yone, xtwo, ytwo, radone, radtwo;
    int xpow, ypow, distance;

    int radsum, raddif;

    std::cin >> counter;

    while(counter > 0)
    {
        distance = 0;
        std::cin >> xone >> yone >> radone >> xtwo >> ytwo >> radtwo;

        radsum = (radone + radtwo) * (radone + radtwo);
        raddif = (radone - radtwo) * (radone - radtwo);
        distance = (xone - xtwo) * (xone - xtwo) +  (yone - ytwo) * (yone - ytwo);
        if(distance != 0)
        {
            if(radsum == distance || raddif == distance)
                std::cout << 1 << std::endl;
            else if (raddif < distance && radsum > distance)
                std::cout << 2 << std::endl;
            else
                std::cout << 0 << std::endl;
        }
        else
        {
            if(raddif == 0)
                std::cout << -1 << std::endl;
            else
                std::cout << 0 << std::endl;
        }
        counter--;
    }
    return (0);
}