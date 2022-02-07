/* CPP Ex 9 and Quiz 1 (2020-06-09) */
#include<iostream>
using namespace std;
int main () {
	float principal, rate;
	int year;
	cout << "Principal value: ";
	cin >> principal;
	cout << "Annual interest rate (in %): ";
	cin >> rate;
	year = 1;
	while (year <= 5) {
		principal = principal * (1+rate/100);
		cout << "At the end of year " << year << ": " << principal << "\n";
		year++;
	}
	return 0;
}

// This file serves as a reference only. You should never copy your assignments directly.  
