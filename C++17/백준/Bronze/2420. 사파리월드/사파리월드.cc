#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long a, b, result;

    cin >> a >> b;

    result = a - b;

    if (result>=0) {
        cout << result << endl;
    } else {
        cout << (-1)*result <<endl;
    }

    return 0;
}