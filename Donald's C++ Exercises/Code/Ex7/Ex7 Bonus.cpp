/* CPP Ex 7 Bonus Ver. (2020-05-22) */
#include <iostream>
#include <time.h>
#include <random>
using namespace std;

int main ()
{
  int answer, guess;
  srand (time (NULL));
  answer = rand () % 100 + 1;
  int attempts = 0;
  int lowerlimit = 1;
  int upperlimit = 100;
  do {
  cout << "Enter a number (" << lowerlimit << "-" << upperlimit << "): ";
    cin >> guess;
    if (guess < lowerlimit || guess > upperlimit) continue;
    if (guess < answer) {
        attempts++;
        cout << "Your guess is too small, try a larger one.\n";
        lowerlimit = guess + 1; 
    } 
    else if (guess > answer) {
        attempts++;
        cout << "Your guess is too large, try a smaller one.\n";
        upperlimit = guess - 1;
    } else {
        attempts++;
        cout << "Bingo!\n";
        cout << "You got it in " << attempts << " times.";
    }
  } while (guess != answer);
  return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.  
