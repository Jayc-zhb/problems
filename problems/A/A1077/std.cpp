#include <iostream>
#include <string>
using namespace std;
const int maxn = 1e5+5;
int main()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    bool b1 = 0, b2 = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == 'a' || s[i] == 'A') b1 = 1;
        if (s[i] == 'c' || s[i] == 'C') b2 = 1;
    }
    if (b1 && b2) cout << "good\n";
    else cout << "bad\n";
    return 0;
}
