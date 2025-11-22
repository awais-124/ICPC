// ============ ICPC C++ TEMPLATE WITH MACROS & OPTIMIZATIONS ============

#include<bits/stdc++.h>
using namespace std;

// ============ MACROS FOR FASTER CODING ============

#define ll long long
#define ld long double
#define pii pair<int,int>
#define pll pair<ll,ll>
#define vi vector<int>
#define vll vector<ll>
#define vvi vector<vector<int>>
#define vvll vector<vector<ll>>
#define si set<int>
#define sll set<ll>
#define mii map<int,int>
#define mll map<ll,ll>

// ============ INPUT/OUTPUT MACROS ============

#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define fi first
#define se second

// ============ LOOP MACROS ============

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(x,v) for(auto x: v)
#define REP(i,n) for(int i=0;i<(n);i++)

// ============ FAST I/O ============

#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);

// ============ DEBUGGING & CONSTANTS ============

const ll MOD = 1e9 + 7;
const ll INF = 1e18;
const int NINF = -2e9;
const ld PI = acos(-1.0);
const ld EPS = 1e-9;

#ifdef DEBUG
  #define debug(x) cout << #x << " = " << x << "\n"
  #define debug2(x,y) cout << #x << " = " << x << ", " << #y << " = " << y << "\n"
#else
  #define debug(x)
  #define debug2(x,y)
#endif

// ============ UTILITY FUNCTIONS ============

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return (a / gcd(a, b)) * b; }
ll power(ll a, ll b, ll mod) {
    ll res = 1;
    a %= mod;
    while(b > 0) {
        if(b & 1) res = (res * a) % mod;
        a = (a * a) % mod;
        b >>= 1;
    }
    return res;
}

bool isPrime(ll n) {
    if(n < 2) return false;
    if(n == 2) return true;
    if(n % 2 == 0) return false;
    for(ll i = 3; i * i <= n; i += 2)
        if(n % i == 0) return false;
    return true;
}

int popcount(ll x) { return __builtin_popcountll(x); }
int ctz(ll x) { return __builtin_ctzll(x); }  // Count trailing zeros
int clz(ll x) { return __builtin_clzll(x); }  // Count leading zeros

// ============ SORTING COMPARATOR ============

// Sort vector of pairs by first element ascending, second descending
bool cmp(pii a, pii b) {
    if(a.fi != b.fi) return a.fi < b.fi;
    return a.se > b.se;
}

// ============ GRAPH UTILITIES ============

const int MAXN = 1e5 + 5;
vector<int> adj[MAXN];
bool visited[MAXN];
int parent[MAXN];
int dist[MAXN];

// BFS
void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()) {
        int u = q.front();
        q.pop();
        for(int v : adj[u]) {
            if(!visited[v]) {
                visited[v] = true;
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
}

// DFS
void dfs(int u) {
    visited[u] = true;
    for(int v : adj[u]) {
        if(!visited[v]) {
            parent[v] = u;
            dfs(v);
        }
    }
}

// ============ MAIN SOLUTION ============

int main() {
    FAST;

    int t;
    cin >> t;

    while(t--) {
        // ---- CLEAR FOR EACH TEST CASE ----
        FOR(i, 0, MAXN) {
            adj[i].clear();
            visited[i] = false;
            dist[i] = 0;
        }

        // ---- READ INPUT ----
        int n;
        cin >> n;

        // ---- SOLVE ----
        // Your solution here

        // ---- OUTPUT ----
        cout << "\n";
    }

    return 0;
}

// ============ TEMPLATE NOTES ============
/*
1. For single test case: remove while(t--) loop, just read directly
2. Use ll for large numbers to avoid overflow
3. MOD is 1e9+7, change if needed
4. MAXN depends on constraints, adjust accordingly
5. bits/stdc++.h includes everything (vector, map, queue, etc)
6. __builtin functions are GCC built-ins (faster than manual)
7. For tight time limits: disable sync_with_stdio, use FAST macro
8. Always check: integer overflow, array bounds, MOD operations
*/
