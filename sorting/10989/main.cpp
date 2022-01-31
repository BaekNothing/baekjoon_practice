#include <iostream>
#include <cstdio>

using namespace std;

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
            printf("%d\n", counter);
            //cout << counter << "\n";
            temp++;
        }
        counter++;
    }
    return (0);
}