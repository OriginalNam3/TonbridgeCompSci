// CPP Ex 10 and Quiz 2 (17-06-2020)
#include<iostream>
using namespace std;

int main () {
	int i, last, sum;
	cout << "Enter the last integer: ";
	cin >> last;
	sum = last;
	cout << last;
	for (i = last-1; i >= 1; i--) {
		cout << "+" << i;
		sum = sum + i;
	}
	cout << "=" << sum;
	return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.  
