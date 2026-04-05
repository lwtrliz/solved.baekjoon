#include <iostream>
#include <ctime>

using namespace std;

int main() {
    time_t t = time(nullptr);
    tm*now = localtime(&t);
    printf("%04d-%02d-%02d\n", now->tm_year + 1900, now->tm_mon + 1, now -> tm_mday);

    return 0;
}