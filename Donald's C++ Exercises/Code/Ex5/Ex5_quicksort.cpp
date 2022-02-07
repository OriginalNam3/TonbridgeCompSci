/* CPP Ex 5 Quick Sort (2020-06-10)*/
#include <iostream>
#include <algorithm>
using namespace std;
int main ()
{
  int a[2];
  cout << "Enter three marks : ";
  for (int i = 0; i < 3; i++) {
  	cin >> a[i];
  }
  sort (a, a+3);
  if (a[0] < 0)
    {
      cout << "Mark less than zero is not accepted.";
      return 0;
    }
  else if (a[2] > 100)
    {
      cout << "Mark larger than 100 is not accepted.";
      return 0;
    }
      if (a[0] == a[2])
	{
	  cout << "Rank 1: " << a[2];
	}
      else if (a[0] == a[1] || a[1] == a[2])
	{
	  cout << "Rank 1: " << a[2] << "\n";
	  cout << "Rank 2: " << a[0];
	}
      else
	{
	  cout << "Rank 1: " << a[2] << "\n";
	  cout << "Rank 2: " << a[1] << "\n";
	  cout << "Rank 3: " << a[0];
	}
	  return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.
