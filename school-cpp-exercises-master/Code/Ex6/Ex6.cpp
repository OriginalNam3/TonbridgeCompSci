/* CPP Ex 6 (2020-04-28) */
#include <iostream>
#include <time.h>
#include <random>
using namespace std;

int main ()
{
  int greet, object1, object2, verb;
  srand (time (NULL));
  const string greetArray[4] = { "Hi!", "Hello, how are you?", "Nice to meet you here!", "How are you doing?" };
  greet = rand () % 4;
  const string objectArray[5] = { "a cat", "a dog", "a fish", "a bird", "a flower" };
  object1 = rand () % 5;
  object2 = rand () % 5;
  const string verbArray[3] = { "biting", "playing with", "watching at" };
  verb = rand () % 3;
  cout << greetArray[greet] << "\n";
  cout << "Yesterday, I saw " << objectArray[object1] << " " << verbArray[verb] << " " << objectArray[object2] << ".";
  return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.
