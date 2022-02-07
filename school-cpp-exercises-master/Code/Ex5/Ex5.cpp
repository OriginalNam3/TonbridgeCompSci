/* CPP Ex 5 (2020-04-24) */
#include <iostream>
using namespace std;

int main ()
{
  int one, two, three, temp;
  cout << "Enter three marks : ";
  cin >> one >> two >> three;
  if (one < 0 || two < 0 || three < 0)
    {
      cout << "Mark less than zero is not accepted.";
    }
  else if (one > 100 || two > 100 || three > 100)
    {
      cout << "Mark larger than 100 is not accepted.";
    }
  else
    {
      if (two > one)
	{
	  temp = one;
	  one = two;
	  two = temp;
	}
      if (three > two)
	{
	  temp = two;
	  two = three;
	  three = temp;
	}
      if (two > one)
	{
	  temp = one;
	  one = two;
	  two = temp;
	}
      if (one == two == three)
	{
	  cout << "Rank 1: " << one;
	}
      else if (one == two)
	{
	  cout << "Rank 1: " << one << "\n";
	  cout << "Rank 2: " << three;
	}
      else if (two == three)
	{
	  cout << "Rank 1: " << one << "\n";
	  cout << "Rank 2: " << two;
	}
      else
	{
	  cout << "Rank 1: " << one << "\n";
	  cout << "Rank 2: " << two << "\n";
	  cout << "Rank 3: " << three;
	}
    }
  return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.
