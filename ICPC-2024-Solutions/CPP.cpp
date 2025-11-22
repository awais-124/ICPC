// ============ ICPC 2024 ASIA TOPI - C++ SOLUTIONS ============

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;

const ll MOD = 1e9 + 7;
const ll INF = 2147483647;
const int MAXN = 1e5 + 5;

// ============ PROBLEM 01: CIRCUIT DESIGN ============

ll count_triangles(int n, vector<pair<int,int>>& edges) {
    vector<set<int>> adj(n);
    for(auto [u, v] : edges) {
        adj[u].insert(v);
        adj[v].insert(u);
    }

    ll count = 0;
    for(int u = 0; u < n; u++) {
        for(int v : adj[u]) {
            if(u < v) {
                for(int w : adj[u]) {
                    if(adj[v].count(w) && v < w) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}

void problem01() {
    int n, m;
    cin >> n >> m;

    vector<pair<int,int>> edges;
    for(int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }

    cout << count_triangles(n, edges) << "\n";
}

// ============ PROBLEM 02: CAR WASHING ============

ll car_washing(int n, int e1, int e2, vi& w1, vi& w2, vi& s1, vi& s2, int x1, int x2) {
    vector<vector<ll>> dp(n, vector<ll>(2));

    dp[0][0] = e1 + w1[0];
    dp[0][1] = e2 + w2[0];

    for(int i = 1; i < n; i++) {
        dp[i][0] = min(dp[i-1][0] + w1[i], dp[i-1][1] + s2[i-1] + w1[i]);
        dp[i][1] = min(dp[i-1][1] + w2[i], dp[i-1][0] + s1[i-1] + w2[i]);
    }

    return min(dp[n-1][0] + x1, dp[n-1][1] + x2);
}

void problem02() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;

        int e1, e2;
        cin >> e1 >> e2;

        vi w1(n), w2(n), s1(n-1), s2(n-1);

        for(int i = 0; i < n; i++) cin >> w1[i];
        for(int i = 0; i < n; i++) cin >> w2[i];
        for(int i = 0; i < n-1; i++) cin >> s1[i];
        for(int i = 0; i < n-1; i++) cin >> s2[i];

        int x1, x2;
        cin >> x1 >> x2;

        cout << car_washing(n, e1, e2, w1, w2, s1, s2, x1, x2) << "\n";
    }
}

// ============ PROBLEM 03: STOCK TRADER ============

ll max_profit(vi& prices, int k) {
    int n = prices.size();
    if(k == 0 || n < 2) return 0;

    if(k >= n/2) {
        ll profit = 0;
        for(int i = 1; i < n; i++) {
            profit += max(0, prices[i] - prices[i-1]);
        }
        return profit;
    }

    vector<ll> buy(k+1, -prices[0]);
    vector<ll> sell(k+1, 0);

    for(int i = 1; i < n; i++) {
        for(int j = k; j >= 1; j--) {
            sell[j] = max(sell[j], buy[j] + prices[i]);
            buy[j] = max(buy[j], sell[j-1] - prices[i]);
        }
    }

    return sell[k];
}

void problem03() {
    int t;
    cin >> t;
    while(t--) {
        int k, n;
        cin >> k >> n;

        vi prices(n);
        for(int i = 0; i < n; i++) {
            cin >> prices[i];
        }

        cout << max_profit(prices, k) << "\n";
    }
}

// ============ PROBLEM 04: CALLIGRAPHY CRISIS ============

void problem04() {
    int n;
    cin >> n;

    vector<string> calligraphies(n);
    for(int i = 0; i < n; i++) {
        cin >> calligraphies[i];
    }

    int q;
    cin >> q;

    while(q--) {
        string query;
        cin >> query;

        int count = 0;
        string query_sorted = query;
        sort(query_sorted.begin(), query_sorted.end());
        int qlen = query.length();

        for(auto& calli : calligraphies) {
            bool found = false;
            for(int end = qlen; end <= (int)calli.length() && !found; end++) {
                string prefix = calli.substr(0, end);
                sort(prefix.begin(), prefix.end());
                if(prefix == query_sorted) {
                    count++;
                    found = true;
                }
            }
        }

        cout << (count > 0 ? count : -1) << "\n";
    }
}

// ============ PROBLEM 05: BIODIVERSITY SCAN ============

ll nCr(int n, int r) {
    if(r > n) return 0;
    if(r == 0 || r == n) return 1;

    vector<vector<ll>> dp(n+1, vector<ll>(r+1, 0));
    for(int i = 0; i <= n; i++) {
        dp[i][0] = 1;
        if(i <= r) dp[i][i] = 1;
    }

    for(int i = 2; i <= n; i++) {
        for(int j = 1; j < i && j <= r; j++) {
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
        }
    }

    return dp[n][r];
}

ll count_partitions(int n, int t, int m) {
    if(n == 0) return (t == 0) ? 1 : 0;
    if(t < n * m) return 0;

    int new_t = t - n * m;
    return nCr(new_t + n - 1, n - 1);
}

void problem05() {
    int k;
    cin >> k;
    while(k--) {
        int n, t, m;
        cin >> n >> t >> m;
        cout << count_partitions(n, t, m) << "\n";
    }
}

// ============ PROBLEM 06: EVENT MANAGEMENT ============

bool is_valid_code(string code) {
    if(code.length() != 3) return false;
    if(code[0] < 'A' || code[0] > 'G') return false;
    if(code[1] < '0' || code[1] > '9') return false;
    if(code[2] < '0' || code[2] > '9') return false;
    return true;
}

void problem06() {
    int t;
    cin >> t;
    while(t--) {
        string s;
        cin >> s;

        vector<string> codes;
        string invalid = "";

        for(int i = 0; i < (int)s.length(); i += 3) {
            string code = s.substr(i, 3);
            if(!is_valid_code(code)) {
                invalid = code;
                break;
            }
            codes.push_back(code);
        }

        if(!invalid.empty()) {
            cout << "-1 " << invalid << "\n";
            continue;
        }

        // Find longest unique sequence
        int max_len = 0;
        vector<string> best_seq;

        for(int start = 0; start < (int)codes.size(); start++) {
            set<string> seen;
            vector<string> seq;

            for(int i = start; i < (int)codes.size(); i++) {
                if(seen.count(codes[i])) break;
                seen.insert(codes[i]);
                seq.push_back(codes[i]);
            }

            if((int)seq.size() > max_len ||
               ((int)seq.size() == max_len && (!best_seq.empty() && seq[0] < best_seq[0]))) {
                max_len = seq.size();
                best_seq = seq;
            }
        }

        // Count categories
        map<char, int> cat_count;
        map<char, string> cat_name = {
            {'A', "Competitions"}, {'B', "Entertainment"},
            {'C', "Social Gatherings"}, {'D', "Dinners"},
            {'E', "Processions"}, {'F', "Training Workshops"}, {'G', "Exams"}
        };

        for(auto& code : best_seq) {
            cat_count[code[0]]++;
        }

        cout << max_len << " ";
        for(int i = 0; i < (int)best_seq.size(); i++) {
            if(i > 0) cout << " ";
            cout << best_seq[i];
        }
        cout << " ";

        int idx = 0;
        for(auto [cat, cnt] : cat_count) {
            if(idx > 0) cout << " ";
            cout << cnt << " " << cat_name[cat];
            idx++;
        }
        cout << "\n";
    }
}

// ============ PROBLEM 07: ELECTORAL BOUNDARIES ============

int max_districts(int n, vector<pair<int,int>>& edges) {
    vector<vi> adj(n+1);
    for(auto [u, v] : edges) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> color(n+1, -1);
    bool bipartite = true;
    int max_color = 0;

    for(int start = 1; start <= n; start++) {
        if(color[start] != -1) continue;

        queue<int> q;
        q.push(start);
        color[start] = 0;

        while(!q.empty()) {
            int u = q.front();
            q.pop();

            for(int v : adj[u]) {
                if(color[v] == -1) {
                    color[v] = 1 - color[u];
                    q.push(v);
                } else if(color[v] == color[u]) {
                    bipartite = false;
                }
            }
        }

        for(int i = 1; i <= n; i++) {
            if(color[i] != -1) max_color = max(max_color, color[i]);
        }
    }

    if(!bipartite) return -1;
    return max_color + 1;
}

void problem07() {
    int t;
    cin >> t;
    while(t--) {
        int n, w;
        cin >> n >> w;

        vector<pair<int,int>> edges;
        for(int i = 0; i < w; i++) {
            int u, v;
            cin >> u >> v;
            edges.push_back({u, v});
        }

        cout << max_districts(n, edges) << "\n";
    }
}

// ============ PROBLEM 08: OPTIMIZED PATH ============

ll dijkstra(int n, vector<vector<pair<int,ll>>>& adj, int start, int end) {
    vector<ll> dist(n+1, INF);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while(!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if(d > dist[u]) continue;

        for(auto [v, w] : adj[u]) {
            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    return dist[end];
}

bool is_prime(ll x) {
    if(x < 2) return false;
    if(x == 2) return true;
    if(x % 2 == 0) return false;
    for(ll i = 3; i*i <= x; i += 2) {
        if(x % i == 0) return false;
    }
    return true;
}

ll sum_three_largest_primes(ll n) {
    ll sum = 0;
    int count = 0;
    for(ll i = n-1; i >= 2 && count < 3; i--) {
        if(is_prime(i)) {
            sum += i;
            count++;
        }
    }
    return sum;
}

void problem08() {
    int n, r, e;
    ll t;
    cin >> n >> r >> e >> t;

    vector<vector<pair<int,ll>>> adj(n+1);

    for(int i = 0; i < r; i++) {
        int u, v;
        ll d;
        cin >> u >> v >> d;
        adj[u].push_back({v, d});
        adj[v].push_back({u, d});
    }

    ll distance = dijkstra(n, adj, 1, e);
    ll token_val = sum_three_largest_primes(t);

    cout << distance << " " << token_val << "\n";
}

// ============ PROBLEM 09: ANCESTRAL QUERIES ============

const int LOG = 20;
int lift[1005][LOG];
int depth[1005];

void dfs(int u, int p, vector<vector<int>>& children) {
    lift[u][0] = p;
    for(int v : children[u]) {
        depth[v] = depth[u] + 1;
        dfs(v, u, children);
    }
}

void problem09() {
    int t;
    cin >> t;
    while(t--) {
        int n, q, r;
        cin >> n >> q >> r;

        vector<vector<int>> children(n+1);
        for(int i = 0; i < n-1; i++) {
            int p, c;
            cin >> p >> c;
            children[p].push_back(c);
        }

        // Build tree
        memset(lift, 0, sizeof(lift));
        memset(depth, 0, sizeof(depth));
        dfs(r, 0, children);

        // Binary lifting
        for(int j = 1; j < LOG; j++) {
            for(int i = 1; i <= n; i++) {
                if(lift[i][j-1] != 0) {
                    lift[i][j] = lift[lift[i][j-1]][j-1];
                }
            }
        }

        // Answer queries
        for(int i = 0; i < q; i++) {
            int u;
            ll k;
            cin >> u >> k;

            int curr = u;
            for(int j = 0; j < LOG; j++) {
                if((k >> j) & 1) {
                    curr = lift[curr][j];
                    if(curr == 0) break;
                }
            }

            cout << (curr == 0 ? -1 : curr) << "\n";
        }
    }
}

// ============ MAIN ============

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Uncomment problem to test
    // problem01();
    // problem02();
    // problem03();
    // problem04();
    // problem05();
    // problem06();
    // problem07();
    // problem08();
    // problem09();

    return 0;
}
