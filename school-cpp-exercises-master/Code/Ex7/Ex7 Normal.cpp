/* CPP Ex 7 Normal Ver. (2020-05-22) */
#include <iostream>
#include <time.h>
#include <random>
using namespace std;

int main ()
{
  int answer, guess;
  srand (time (NULL));
  answer = rand () % 100 + 1;
  do {
  cout << "Enter a number (1-100): ";
    cin >> guess;
    if (guess < 1 || guess > 100) continue;
    if (guess < answer) {
        cout << "Your guess is too small, try a larger one.\n";
    } 
    else if (guess > answer) {
        cout << "Your guess is too large, try a smaller one.\n";
    } else {
        cout << "Bingo!\n";
    }
  } while (guess != answer);
  return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.  
