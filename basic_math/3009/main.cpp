#include <iostream>

int main(void){

    int xpos, ypos, xone, yone, xtwo, ytwo;

    std::cin >> xone >> yone;
    std::cin >> xtwo >> ytwo;
    std::cin >> xpos >> ypos;

    // 다른 둘과 같지 않은 하나 xpos에 집어넣기
    xpos = xone == xpos ? xtwo : xpos == xtwo ? xone : xpos;
    ypos = yone == ypos ? ytwo : ypos == ytwo ? yone : ypos;

    std::cout << xpos << " " << ypos << std::endl;

    return (0);
}