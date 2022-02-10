#include<bits/stdc++.h>
using namespace std;
int main() {
	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		int a[n], sum = 0;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
			sum += a[i]; //compute the total number of candies during input stage
		}
		if (sum%n != 0) cout << "-1" << endl; //the candies can be evenly distributed if and only if the total number of candies is divisible by the number of friends
		else {
			int avg = sum/n; //avg is the number of candies that each friend would get after evenly distributing
			int count = 0; //keeps track of those who has more candies than avg; their candies will be distributed to the 'poorer' friends
			for (int i = 0; i < n; i++) {
				if (a[i] > avg) count++;
			}
			cout << count << endl;
		}
	}
	return 0;
}
