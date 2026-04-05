#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;

    cin >> n >> m;

    int total = n*100;

    if (total>=m) {
        cout << "Yes" << "\n";
    } else {
        cout << "No" << "\n";
    }

    return 0;

}