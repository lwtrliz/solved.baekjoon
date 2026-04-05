#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int a, b;
    cin >> a >> b;

    // 삼항연산자
    // (조건식 1) ? [실행코드 A] : ((조건식 2) ? [실행코드 B] : [실행코드 C])
    // 조건식 1이 참이면 실행 코드 A
    // 외, 조건식 2 ~~~

    cout << ((a>b) ? ">" : ((a<b) ? "<" : "=="));

    return 0;
}