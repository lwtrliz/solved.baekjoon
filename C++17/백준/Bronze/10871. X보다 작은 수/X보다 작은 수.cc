#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, x;
    int arr[10000];
    cin >> n >> x;
    
    for (int i = 0; i<n;i++)
    {
        cin >> arr[i];
    }

    for (int j = 0; j < n; j++)
    {
        if (arr[j] < x)
        {
            cout << arr[j] << " ";
        }
    }
    cout << "\n";
    return 0;
}