#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int a;

    cin >> a;

    if ((a <= 100) && (a >= 90)) {
        cout << "A\n";
    } else if ((a>=80) && (a<= 89)) {
        cout << "B\n";
    } else if ((a>=70) && (a<= 79)) {
        cout << "C\n";
    } else if ((a>=60) && (a<= 69)) {
        cout << "D\n";
    } else {
        cout << "F\n";
    }

    return 0;
}