#include <iostream>
using namespace std;

int gcd(int m, int n)
{
  int r = m % n;
  if (r == 0)
  {
    return n;
  }

  while (r != 0)
  {
    m = n;
    n = r;
    r = m % n;
  }
  return n;
}

int main()
{
  int m;
  int n;
  int res;

  cout << "Please input two number" << endl;
  cin >> m >> n;
  
  res = gcd(m, n);
  cout << "The result is:" << res << endl;

  return 0;
}
