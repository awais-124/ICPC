/**
 * Useful Macros for Competitive Programming
 * Include this file or copy macros to your template
 */

#pragma once

// =============== BASIC MACROS ===============
#define ll long long
#define ull unsigned long long
#define ld long double
#define int ll  // Use when you want all integers to be long long

// =============== LOOP MACROS ===============
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define repr(i, a, b) for (int i = (a); i >= (b); --i)
#define repn(i, n) rep(i, 0, n)
#define reprn(i, n) repr(i, (n)-1, 0)

// Iterate through containers
#define trav(a, x) for (auto& a : x)
#define tr(it, x) for (auto it = (x).begin(); it != (x).end(); ++it)

// =============== ARRAY OPERATIONS ===============
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz(x) ((int)(x).size())
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define fi first
#define se second

// =============== SHORTHAND MACROS ===============
#define yes cout << "YES\n"
#define no cout << "NO\n"
#define yesno(x) cout << ((x) ? "YES\n" : "NO\n")

// =============== DEBUG MACROS ===============
#ifdef LOCAL
#define dbg(x) cerr << #x << " = " << x << endl
#define dbg2(x, y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl
#define dbg3(x, y, z) cerr << #x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl
#define dbg_vec(v) cerr << #v << " = ["; for (auto& x : v) cerr << x << " "; cerr << "]\n"
#define dbg_map(m) cerr << #m << " = { "; for (auto& [k, v] : m) cerr << k << ":" << v << " "; cerr << "}\n"
#define dbg_set(s) cerr << #s << " = { "; for (auto& x : s) cerr << x << " "; cerr << "}\n"
#else
#define dbg(x)
#define dbg2(x, y)
#define dbg3(x, y, z)
#define dbg_vec(v)
#define dbg_map(m)
#define dbg_set(s)
#endif

// =============== BIT OPERATION MACROS ===============
#define set_bit(x, i) ((x) |= (1LL << (i)))
#define clear_bit(x, i) ((x) &= ~(1LL << (i)))
#define toggle_bit(x, i) ((x) ^= (1LL << (i)))
#define get_bit(x, i) (((x) >> (i)) & 1LL)
#define is_power_of_two(x) ((x) && !((x) & ((x) - 1)))

// =============== MATH MACROS ===============
#define min3(a, b, c) min(a, min(b, c))
#define max3(a, b, c) max(a, max(b, c))
#define min4(a, b, c, d) min(a, min(b, min(c, d)))
#define max4(a, b, c, d) max(a, max(b, max(c, d)))

// =============== CONSTANTS ===============
const int INF = 1e9;
const ll LINF = 1e18;
const int MOD = 1e9 + 7;
const int MOD2 = 998244353;
const double PI = acos(-1.0);
const double EPS = 1e-9;
