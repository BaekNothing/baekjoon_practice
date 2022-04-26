#include <iostream>
#include <cstdio>

using namespace std;
int main(void)
{

    int countAry[10042];
    int length;
    int temp;
    int counter;
    long long arithmeticMean = 0;
    int max = -4000;
    int min = 4000;

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
        arithmeticMean += temp;
        if(max < temp)
          max = temp;
        if(min > temp)
          min = temp;
        temp += 4000;
        countAry[temp]++;
        counter++;
    }

    int middleIndex = 0;
    int middleValue = 0;
    int middleFlag = 0;

    int frequencyIndex = 0;
    int frequencyValue = 0;

    for(int i = 0; i < 10042; i++)
    {
      if (middleFlag == 0)
        middleValue += countAry[i];
      if (middleFlag == 0 && middleValue > length / 2)
      {
        middleFlag = 1;
        middleIndex = i;
      }
      if (frequencyValue < countAry[i])
      {
        frequencyValue = countAry[i];
        frequencyIndex = i;
      }
    }

    for (int i = 0; i < 10042; i++)
    {
      if(frequencyValue == countAry[i] && frequencyIndex != i)
      {
        frequencyIndex = i;
        break;
      }
    }

    printf("%.01f\n%d\n%d\n%d", (float)arithmeticMean / (float)length, middleIndex - 4000, frequencyIndex - 4000, max - min);

    return (0);
}
