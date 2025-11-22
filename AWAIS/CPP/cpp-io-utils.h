/**
 * Fast I/O Utilities for Competitive Programming
 */

#pragma once

#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Fast input for integers
inline int read_int() {
    int x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9') {
        if (ch == '-') f = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9') {
        x = x * 10 + ch - '0';
        ch = getchar();
    }
    return x * f;
}

inline long long read_ll() {
    long long x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9') {
        if (ch == '-') f = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9') {
        x = x * 10 + ch - '0';
        ch = getchar();
    }
    return x * f;
}

// Fast output for integers
inline void write_int(int x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    if (x > 9) write_int(x / 10);
    putchar(x % 10 + '0');
}

inline void write_ll(long long x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    if (x > 9) write_ll(x / 10);
    putchar(x % 10 + '0');
}

// Read vector of integers
template<typename T>
vector<T> read_vector(int n) {
    vector<T> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }
    return v;
}

// Print vector with separator
template<typename T>
void print_vector(const vector<T>& v, string separator = " ") {
    for (int i = 0; i < v.size(); ++i) {
        cout << v[i];
        if (i < v.size() - 1) cout << separator;
    }
    cout << "\n";
}

// Print 2D vector
template<typename T>
void print_2d_vector(const vector<vector<T>>& v, string row_sep = "\n", string col_sep = " ") {
    for (const auto& row : v) {
        for (int i = 0; i < row.size(); ++i) {
            cout << row[i];
            if (i < row.size() - 1) cout << col_sep;
        }
        cout << row_sep;
    }
}

// Setup fast I/O
void setup_fast_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    // For faster I/O with scanf/printf (choose one approach)
    // ios::sync_with_stdio(false); cin.tie(0);  // Use with cin/cout
}
