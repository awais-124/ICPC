/**
 * Competitive Programming Template for C++
 * Author: Your Name
 * Created: 2024
 */

#include <bits/stdc++.h>
using namespace std;

// =============== MACROS ===============
#define ll long long
#define ull unsigned long long
#define ld long double

// Loop macros
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define repr(i, a, b) for (int i = (a); i >= (b); --i)
#define repn(i, n) rep(i, 0, n)
#define reprn(i, n) repr(i, n-1, 0)

// Array macros
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz(x) ((int)(x).size())
#define mp make_pair
#define pb push_back
#define eb emplace_back

// Debug macros (remove in final submission)
#ifdef LOCAL
#define debug(x) cerr << #x << " = " << x << endl
#define debug_vec(v) cerr << #v << " = "; for(auto& i: v) cerr << i << " "; cerr << endl
#define debug_map(m) cerr << #m << " = "; for(auto& [k,v]: m) cerr << k << ":" << v << " "; cerr << endl
#else
#define debug(x)
#define debug_vec(v)
#define debug_map(m)
#endif

// Type aliases
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;

// Constants
const int INF = 1e9;
const ll LINF = 1e18;
const int MOD = 1e9 + 7;
const double EPS = 1e-9;

// =============== FAST I/O ===============
void setup_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    #ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
}

// =============== SOLUTION ===============
void solve() {
    // Your solution for single test case goes here
    int n;
    cin >> n;
    vi arr(n);
    repn(i, n) cin >> arr[i];

    // Example solution
    ll sum = 0;
    repn(i, n) sum += arr[i];
    cout << sum << "\n";
}

void solve_multiple_tests() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}

// =============== MAIN ===============
int main() {
    setup_io();

    // Uncomment based on problem type:

    // Single test case:
    // solve();

    // Multiple test cases:
    solve_multiple_tests();

    // Interactive problems:
    // while (true) {
    //     if (!solve_interactive()) break;
    // }

    return 0;
}
