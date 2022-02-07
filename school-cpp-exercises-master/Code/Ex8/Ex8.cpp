/* CPP Ex 8 (2020-05-24) */
#include <iostream>
using namespace std;

int main ()
{
  int number, i, j, space;
  do {
    cout << "Length of triangle (1-10)? ";
    cin >> number;
  } while (number < 1||number > 10);
  for (i = 1; i <= number; i++) {
      space = number - i;
      for (j = 0; j < space; j++) {
          cout << " ";
      }  for (j = 0; j < i; j++) {
          cout << "*";
      }
      cout << "\n";
  }
  return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.  
