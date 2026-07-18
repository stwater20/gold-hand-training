#include <stdio.h>
#include <time.h>

int main() {
    int k = 0;
    int n = 10000000;

    clock_t start, end;
    start = clock();

    for (int i = 0; i < n; i++) {
        k++;
    }

    end = clock();

    printf("k = %d\n", k);
    printf("C 執行時間: %.6f 秒\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}
