/**
 * Multiple Template Variations for Different Problem Types
 */

// =============== TEMPLATE 1: STANDARD MULTIPLE TEST CASES ===============
#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define rep(i, a, b) for (int i = (a); i < (b); ++i)

void solve() {
    // Single test case solution
    int n;
    cin >> n;
    vector<int> arr(n);
    rep(i, 0, n) cin >> arr[i];

    // Your logic here
    cout << accumulate(arr.begin(), arr.end(), 0LL) << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}

// =============== TEMPLATE 2: INTERACTIVE PROBLEMS ===============
/*
#include <bits/stdc++.h>
using namespace std;

int query(int x, int y) {
    cout << "? " << x << " " << y << endl;
    int response;
    cin >> response;
    return response;
}

void answer(int x) {
    cout << "! " << x << endl;
}

void solve_interactive() {
    int n;
    cin >> n;

    // Interactive logic
    int left = 1, right = n;
    while (left < right) {
        int mid = (left + right) / 2;
        int resp = query(left, mid);
        // Process response and update bounds
    }

    answer(left);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve_interactive();
    }
    return 0;
}
*/

// =============== TEMPLATE 3: OUTPUT FORMAT WITH PRECISION ===============
/*
#include <bits/stdc++.h>
using namespace std;

void solve_with_precision() {
    double a, b;
    cin >> a >> b;

    cout << fixed << setprecision(10) << a + b << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout << fixed << setprecision(10);

    int t;
    cin >> t;
    while (t--) {
        solve_with_precision();
    }

    return 0;
}
*/

// =============== TEMPLATE 4: FIXED NUMBER OF TEST CASES ===============
/*
#include <bits/stdc++.h>
using namespace std;

void solve_fixed_cases() {
    int n;
    cin >> n;
    // Solution logic
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    // cin >> t;  // Uncomment if number of test cases is variable

    for (int tc = 1; tc <= t; tc++) {
        // cout << "Case #" << tc << ": ";
        solve_fixed_cases();
    }

    return 0;
}
*/
