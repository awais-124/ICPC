// ============ C++ OPTIMIZED APPROACHES FOR ICPC ============
// These are faster/more efficient when implemented in C++ vs Python

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;

const ll MOD = 1e9 + 7;
const ll INF = 1e18;

// ============ 1. SEGMENT TREE (Range Query & Point Update) ============
// Much faster than Python for competitive programming

class SegmentTree {
private:
    vector<ll> tree;
    int n;

    void build(vector<ll>& arr, int node, int start, int end) {
        if(start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2*node, start, mid);
            build(arr, 2*node+1, mid+1, end);
            tree[node] = tree[2*node] + tree[2*node+1];
        }
    }

    void update(int node, int start, int end, int idx, ll val) {
        if(start == end) {
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if(idx <= mid)
                update(2*node, start, mid, idx, val);
            else
                update(2*node+1, mid+1, end, idx, val);
            tree[node] = tree[2*node] + tree[2*node+1];
        }
    }

    ll query(int node, int start, int end, int l, int r) {
        if(r < start || end < l) return 0;
        if(l <= start && end <= r) return tree[node];

        int mid = (start + end) / 2;
        ll p1 = query(2*node, start, mid, l, r);
        ll p2 = query(2*node+1, mid+1, end, l, r);
        return p1 + p2;
    }

public:
    SegmentTree(vector<ll>& arr) {
        n = arr.size();
        tree.assign(4*n, 0);
        build(arr, 1, 0, n-1);
    }

    void update(int idx, ll val) {
        update(1, 0, n-1, idx, val);
    }

    ll query(int l, int r) {
        return query(1, 0, n-1, l, r);
    }
};


// ============ 2. FENWICK TREE / BIT (Binary Indexed Tree) ============
// Faster & simpler than Segment Tree for basic range queries

class FenwickTree {
private:
    vector<ll> tree;
    int n;

public:
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, ll delta) {
        for(++i; i <= n; i += i & -i)
            tree[i] += delta;
    }

    ll query(int i) {
        ll sum = 0;
        for(++i; i > 0; i -= i & -i)
            sum += tree[i];
        return sum;
    }

    ll range_query(int l, int r) {
        return query(r) - query(l - 1);
    }
};


// ============ 3. UNION-FIND (DSU) - Path Compression & Union by Rank ============
// Essential for connectivity problems

class DSU {
public:
    vector<int> parent, rank;

    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for(int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        if(parent[x] != x)
            parent[x] = find(parent[x]);  // Path compression
        return parent[x];
    }

    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if(px == py) return false;

        // Union by rank
        if(rank[px] < rank[py]) swap(px, py);
        parent[py] = px;
        if(rank[px] == rank[py]) rank[px]++;
        return true;
    }
};


// ============ 4. SPARSE TABLE (Static Range Minimum Query) ============
// O(n log n) preprocessing, O(1) query

class SparseTable {
private:
    vector<vector<int>> table;
    vector<int> Log;
    int n;

public:
    SparseTable(vector<int>& arr) {
        n = arr.size();
        int logn = 0;
        while((1 << logn) <= n) logn++;

        table.assign(n, vector<int>(logn));
        Log.assign(n + 1, 0);

        for(int i = 2; i <= n; i++)
            Log[i] = Log[i/2] + 1;

        for(int i = 0; i < n; i++)
            table[i][0] = arr[i];

        for(int j = 1; j < logn; j++)
            for(int i = 0; i + (1 << j) <= n; i++)
                table[i][j] = min(table[i][j-1], table[i + (1 << (j-1))][j-1]);
    }

    int query(int l, int r) {
        int len = r - l + 1;
        int k = Log[len];
        return min(table[l][k], table[r - (1 << k) + 1][k]);
    }
};


// ============ 5. FAST EXPONENTIATION ============

ll power_mod(ll a, ll b, ll mod) {
    ll res = 1;
    a %= mod;
    while(b > 0) {
        if(b & 1) res = (res * a) % mod;
        a = (a * a) % mod;
        b >>= 1;
    }
    return res;
}


// ============ 6. SIEVE OF ERATOSTHENES (All primes up to N) ============

vector<bool> sieve(int n) {
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;

    for(int i = 2; i * i <= n; i++) {
        if(is_prime[i]) {
            for(int j = i * i; j <= n; j += i)
                is_prime[j] = false;
        }
    }
    return is_prime;
}


// ============ 7. PRIME FACTORIZATION (All factors up to N) ============

vector<int> smallest_prime_factor(int n) {
    vector<int> spf(n + 1);
    for(int i = 1; i <= n; i++) spf[i] = i;

    for(int i = 2; i * i <= n; i++) {
        if(spf[i] == i) {  // i is prime
            for(int j = i * i; j <= n; j += i)
                if(spf[j] == j) spf[j] = i;
        }
    }
    return spf;
}


// ============ 8. SUFFIX ARRAY & LCP (String Matching) ============
// For fast string searching

vector<int> build_suffix_array(string s) {
    int n = s.size();
    vector<int> sa(n), rank(n), tmp(n);

    for(int i = 0; i < n; i++) {
        sa[i] = i;
        rank[i] = s[i];
    }

    for(int k = 1; k < n; k *= 2) {
        auto cmp = [&](int i, int j) {
            if(rank[i] != rank[j]) return rank[i] < rank[j];
            int ri = (i + k < n) ? rank[i + k] : -1;
            int rj = (j + k < n) ? rank[j + k] : -1;
            return ri < rj;
        };

        sort(sa.begin(), sa.end(), cmp);

        tmp[sa[0]] = 0;
        for(int i = 1; i < n; i++) {
            tmp[sa[i]] = tmp[sa[i-1]] + (cmp(sa[i-1], sa[i]) ? 1 : 0);
        }
        rank = tmp;
    }
    return sa;
}


// ============ 9. TRIE (Fast String Search/Prefix Matching) ============

struct TrieNode {
    map<char, TrieNode*> children;
    bool isEnd = false;
};

class Trie {
public:
    TrieNode* root;

    Trie() { root = new TrieNode(); }

    void insert(string& word) {
        TrieNode* node = root;
        for(char c : word) {
            if(!node->children[c]) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

    bool search(string& word) {
        TrieNode* node = root;
        for(char c : word) {
            if(!node->children[c]) return false;
            node = node->children[c];
        }
        return node->isEnd;
    }

    bool startsWith(string& prefix) {
        TrieNode* node = root;
        for(char c : prefix) {
            if(!node->children[c]) return false;
            node = node->children[c];
        }
        return true;
    }
};


// ============ 10. KRUSKAL'S ALGORITHM (MST) ============

struct Edge {
    int u, v;
    ll w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

ll kruskal(int n, vector<Edge>& edges) {
    DSU dsu(n);
    sort(edges.begin(), edges.end());

    ll mst_weight = 0;
    for(auto& e : edges) {
        if(dsu.unite(e.u, e.v)) {
            mst_weight += e.w;
        }
    }
    return mst_weight;
}


// ============ 11. TWO POINTER / SLIDING WINDOW ============

// Find max sum subarray of size k
ll max_sum_subarray(vector<int>& arr, int k) {
    ll max_sum = 0, current_sum = 0;

    for(int i = 0; i < k; i++)
        current_sum += arr[i];
    max_sum = current_sum;

    for(int i = k; i < arr.size(); i++) {
        current_sum += arr[i] - arr[i - k];
        max_sum = max(max_sum, current_sum);
    }
    return max_sum;
}


// ============ 12. MATRIX EXPONENTIATION ============
// For Fibonacci, linear recurrence relations

typedef vector<vector<ll>> matrix;

matrix multiply(matrix& a, matrix& b) {
    int n = a.size();
    matrix c(n, vector<ll>(n, 0));
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            for(int k = 0; k < n; k++)
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
    return c;
}

matrix matrix_power(matrix a, ll p) {
    int n = a.size();
    matrix res(n, vector<ll>(n, 0));
    for(int i = 0; i < n; i++) res[i][i] = 1;

    while(p > 0) {
        if(p & 1) res = multiply(res, a);
        a = multiply(a, a);
        p >>= 1;
    }
    return res;
}
