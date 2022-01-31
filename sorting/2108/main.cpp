#include <iostream>
#include <cstdio>

using namespace std;
// 산술평균 : N개의 수들의 합을 N으로 나눈 값
// 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
// 최빈값 : N개의 수들 중 가장 많이 나타나는 값
// 범위 : N개의 수들 중 최댓값과 최솟값의 차이
int main(void)
{
    int countAry[10042];
    int length;
    int temp;
    int counter;
 
    cin >> length;
    counter = 0;
    while (counter < 10042)
    {
        countAry[counter] = 0;
        counter++;        
    }

    counter = 0;
    while (counter < length)
    {
        scanf("%d", &temp);
        temp += 4000;
        //cin >> temp;
        countAry[temp]++;
        counter++;
    }
    
    counter = 0;
    while (counter <= 10000)
    {
        temp = 0;
        while (temp < countAry[counter])
        {
            printf("%d\n", counter - 4000);
            //cout << counter << "\n";
            temp++;
        }
        counter++;
    }
    return (0);
}