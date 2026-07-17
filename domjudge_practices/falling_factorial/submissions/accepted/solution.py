#!/usr/bin/env python3
"""
核心演算法
========
下降階乘 P(n,k) 是從 n 開始連乘 k 個整數：

    P(n,k) = n * (n-1) * ... * (n-k+1)

使用迴圈逐項相乘，每乘一次就對 MOD 取餘數，避免數字無限制成長。
k=0 時沒有任何乘數，依空乘積定義答案為 1。
若所有查詢的 k 總和為 K，時間複雜度為 O(K)，額外空間為 O(1)。
"""

import sys


MOD = 1_000_000_007


def falling_factorial(n: int, k: int) -> int:
    result = 1

    # offset 依序為 0、1、...、k-1，所以乘數為 n-offset。
    for offset in range(k):
        result = result * (n - offset) % MOD

    return result


def solve(tokens: list[str]) -> str:
    test_count = int(tokens[0])
    position = 1
    answers = []

    for case_number in range(1, test_count + 1):
        n = int(tokens[position])
        k = int(tokens[position + 1])
        position += 2
        value = falling_factorial(n, k)
        answers.append(f"Case {case_number}: {value}")

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read().split()))
