#include <cstdio>
#include <iostream>
using namespace std;

void fib(int n)
{
  int loop = 1;
  int a = 1;
  int b = 1;

  if (n == 1 || n == 2)
  {
    cout << loop << endl;
    return ;
  }
  
  while (loop <= n)
  {
    cout << a << endl;
    int tmp = a;
    a = b;
    b = tmp + b;
    loop++;
  }
}

int main()
{

  int n;
  cout << "Please input a number to compute fib" << endl;
  cin >> n;

  fib(n);

  return 0;
}
