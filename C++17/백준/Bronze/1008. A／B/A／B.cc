#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    double a, b;

    cin >> a >> b;
    
    cout.precision(12); // 정수부 + 실수부 = 12
    
    cout << fixed; // 실수부 -> 12
    cout << a/b << endl;
    
    return 0;
}