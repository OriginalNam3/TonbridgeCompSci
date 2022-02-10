#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--) {
        int n, l, r;
        cin >> n >> l >> r;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        sort(a.begin(), a.end());  // in order to take advantage of binary search
        long long tot = 0;
        for (int i = 0; i < n; i++) {
            // this is the idx of the first value x such that, when added to a[i], satisfies l <= x + a[i]
            int first = lower_bound(a.begin(), a.end(), l-a[i]) - a.begin();

            // this is the idx of the first value x such that, when added to a[i], NO LONGER satisfies x + a[i] <= r
            // hence first - last gives the number of x's that can be added to a[i] s.t. l <= x + a[i] <= r
            int last = upper_bound(a.begin(), a.end(), r-a[i]) - a.begin();

            // max(first, i) because, if i is within first~last, we would have already counted the pairs
            // (a[i] is now simply the second element in the pair)
            int cnts = last - max(first, i);

            // if i is within first~last, we obviously don't want to count itself
            if (first <= i && i <= last) cnts--;

            // accounting for possible -ve solution
            cnts = max(0, cnts);
            tot += cnts;
        }
        cout << tot << '\n';
    }
    return 0;
}
