#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;

    cin >> n >> m;
    if (n-1 < m)
    {
        cout << 2*n - 1;
    } else {
        cout << 2*m + 1;
    }

    return 0;
}