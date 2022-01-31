#include <iostream>
#include <cstdlib>

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
    for (int i = 0; i < length - 1; i++)
    {
        for (int k = 0; k < length - 1 - i; k++)
        {
            if (intAry[k] > intAry[k + 1])
            {
                temp = intAry[k];
                intAry[k] = intAry[k + 1];
                intAry[k + 1] = temp;
            }
            // for (int i = 0; i < length; i++)
            //     cout << intAry[i] << " ";
            // cout << "\n";
        }
    }
    for (int i = 0; i < length; i++)
        cout << intAry[i] << "\n";
    free(intAry);
    return (0);
}