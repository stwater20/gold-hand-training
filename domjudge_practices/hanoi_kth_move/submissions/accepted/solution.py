#!/usr/bin/env python3
"""
核心演算法
========
n 層河內塔的完整解可拆成：

1. 前 2^(n-1)-1 步：把上方 n-1 個圓盤從 source 移到 auxiliary。
2. 第 2^(n-1) 步：把第 n 號圓盤從 source 移到 target。
3. 剩餘步驟：把 n-1 個圓盤從 auxiliary 移到 target。

比較 k 與中間步 mid=2^(n-1)，只遞迴進入包含第 k 步的那一半，
不必產生完整的 2^n-1 個步驟。每筆查詢時間 O(n)、遞迴空間 O(n)。
"""

import sys


def kth_move(
    n: int, k: int, source: str = "A", auxiliary: str = "B", target: str = "C"
) -> tuple[int, str, str]:
    mid = 1 << (n - 1)  # 2^(n-1)，也是最大圓盤被移動的步數。

    if k < mid:
        # 第 k 步位於第一個 n-1 層子問題。
        return kth_move(n - 1, k, source, target, auxiliary)

    if k == mid:
        # 正好是把最大的第 n 號圓盤移到目標柱。
        return n, source, target

    # 第 k 步位於第二個 n-1 層子問題；先扣掉前半段與中間那一步。
    return kth_move(n - 1, k - mid, auxiliary, source, target)


def solve(tokens: list[str]) -> str:
    test_count = int(tokens[0])
    position = 1
    answers = []

    for case_number in range(1, test_count + 1):
        n = int(tokens[position])
        k = int(tokens[position + 1])
        position += 2
        disk, source, target = kth_move(n, k)
        answers.append(f"Case {case_number}: {disk} {source} {target}")

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read().split()))
