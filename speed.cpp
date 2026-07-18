#include <iostream>
#include <iomanip>
#include <ctime>
using namespace std;

int main() {
    int k = 0;
    int n = 10000000;

    clock_t start, end;
    start = clock();

    for (int i = 0; i < n; i++) {
        k++;
    }

    end = clock();

    cout << "k = " << k << "\n";
    cout << "C++ 執行時間: " << fixed << setprecision(6)
         << (double)(end - start) / CLOCKS_PER_SEC << " 秒\n";

    return 0;
}
