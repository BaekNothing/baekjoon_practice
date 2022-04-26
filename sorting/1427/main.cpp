#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
  long long input;
  int ary[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

  cin >> input;
  while(input != 0)
  {
    ary[input % 10]++;
    input /= 10;
  }

  for(int i = 9; i >= 0 ; i--)
    while(ary[i]-- > 0)
      cout << i;
  return 0;
}
