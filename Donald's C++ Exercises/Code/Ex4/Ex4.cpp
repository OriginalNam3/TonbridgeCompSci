/* CPP Ex 3 (2020-04-23) */
#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
  cout << "**************************** \n";
  cout << "Roots of quadratic equation: \n";
  cout << "ax^2 + bx + c = 0 \n";
  cout << "**************************** \n";

  double a, b, c, discrim, root1, root2;
  cout << "Values of a, b and c: ";
  cin >> a >> b >> c;
discrim = b*b - 4*a*c;
if (discrim < 0) { 
    cout << "No Real Root";
}
 else {
    root1 = (- b - sqrt(discrim))/2/a;
    root2 = (- b + sqrt(discrim))/2/a;
    cout << "Root 1 is " << root1 << "\n";
    cout << "Root 2 is " << root2;
 }
  return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.
