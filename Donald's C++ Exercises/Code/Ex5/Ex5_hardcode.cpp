/* CPP Ex 5 Hard Code (2020-04-24) */
#include <iostream>
using namespace std;

int main ()
{
  int one, two, three;
  cout << "Enter three marks : ";
  cin >> one >> two >> three;
  if (one < 0 || two < 0 || three < 0)
    {
    cout << "Mark less than zero is not accepted.";}
  else if (one > 100 || two > 100 || three > 100)
    {
    cout << "Mark larger than 100 is not accepted.";}
  else if (one > two && two > three)
    {
      cout << "Rank 1: " << one << "\n";
      cout << "Rank 2: " << two << "\n";
      cout << "Rank 3: " << three << "\n";
    }
  else if (one > three && three > two)
    {
      cout << "Rank 1: " << one << "\n";
      cout << "Rank 2: " << three << "\n";
      cout << "Rank 3: " << two << "\n";
    }
  else if (two > one && one > three)
    {
      cout << "Rank 1: " << two << "\n";
      cout << "Rank 2: " << one << "\n";
      cout << "Rank 3: " << three << "\n";
    }
  else if (two > three && three > one)
    {
      cout << "Rank 1: " << two << "\n";
      cout << "Rank 2: " << three << "\n";
      cout << "Rank 3: " << one << "\n";
    }
  else if (three > one && one > two)
    {
      cout << "Rank 1: " << three << "\n";
      cout << "Rank 2: " << one << "\n";
      cout << "Rank 3: " << two << "\n";
    }
  else if (three > two && two > one)
    {
      cout << "Rank 1: " << three << "\n";
      cout << "Rank 2: " << two << "\n";
      cout << "Rank 3: " << one << "\n";
    }
  else if (one == two && two > three)
    {
      cout << "Rank 1: " << one << "\n";
      cout << "Rank 2: " << three << "\n";
    }
  else if (one == two && two < three)
    {
      cout << "Rank 1: " << three << "\n";
      cout << "Rank 2: " << one << "\n";
    }
  else if (one == three && one > two)
    {
      cout << "Rank 1: " << one << "\n";
      cout << "Rank 2: " << two << "\n";
    }
  else if (one == three && one < two)
    {
      cout << "Rank 1: " << two << "\n";
      cout << "Rank 2: " << one << "\n";
    }
  else if (two == three && two > one)
    {
      cout << "Rank 1: " << two << "\n";
      cout << "Rank 2: " << one << "\n";
    }
  else if (two == three && two < one)
    {
      cout << "Rank 1: " << one << "\n";
      cout << "Rank 2: " << two << "\n";
    }
  else if (one == two == three)
    {
      cout << "Rank 1: " << one;
    }
return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.
// Hard codes like this one are not accepted in school assignments.
