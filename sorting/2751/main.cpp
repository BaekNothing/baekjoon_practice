#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
    int *intAry;
    int length;
    int temp;

    cin >> length;
    intAry = (int *)malloc(sizeof(int) * (length + 1));
    for (int i = 0; i < length; i++)
        cin >> intAry[i];
    sort(intAry, intAry + length);
    for (int i = 0; i < length; i++)
        cout << intAry[i] << "\n";
    return (0);
}