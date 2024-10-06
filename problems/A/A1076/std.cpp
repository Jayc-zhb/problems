#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
const int maxn = 1e5+5;
bool cmp(pair<int, int> a, pair<int, int> b){
    if(a.first == b.first){
        return a.second < b.second;
    }
    else {
        return a.first < b.first;
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    std::vector<pair<int, int>> a(n);
    for(int i = 0;i  < n;i++){
        cin >> a[i].first >> a[i].second;
    }
    sort(a.begin(), a.end(), cmp);
    long long ans1 = 0, ans2 = 0;
    for(int i = 0;i < n - m;i++){
        ans1+=a[i].first;
        ans2+=a[i].second;
    }
    cout << ans1 << ' ' << ans2 << endl;
    return 0;
}
