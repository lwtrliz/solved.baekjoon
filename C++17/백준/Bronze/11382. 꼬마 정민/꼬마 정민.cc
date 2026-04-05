#include <iostream>

using namespace std;

int main()
{
    long long a, b, c; 
    // 10^12 * 3 일 경우 int 자료형의 범위를 초과
    // int 보다 더 큰 범위인 long long으로 변수 선언

    cin >> a >> b >> c;
    
    cout << a + b + c<< endl;

    return 0;
}