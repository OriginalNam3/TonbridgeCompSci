/* CPP Ex 3 (2020-04-23) */
#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
  int one, two, three;
  cout << "Length of first side: ";
  cin >> one;
  cout << "Length of second side: ";
  cin >> two;
  three = sqrt (one * one + two * two);
  cout << "Length of hypotenuse is " << three;
  return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.
