#!/usr/bin/env python3
"""
核心演算法
========
維持兩個相鄰的 Fibonacci 數：current=F_n、next_value=F_(n+1)。
只要 current 還小於門檻 x，就同步更新：

    current, next_value = next_value, current + next_value

迴圈第一次停止時，current 就是第一個大於或等於 x 的 Fibonacci 數。
因 Fibonacci 數呈指數成長，每筆查詢只需 O(log x) 次迴圈，空間 O(1)。
"""

import sys


def first_fibonacci_at_least(x: int) -> tuple[int, int]:
    index = 0
    current, next_value = 0, 1

    while current < x:
        current, next_value = next_value, current + next_value
        index += 1

    return index, current


def solve(tokens: list[str]) -> str:
    test_count = int(tokens[0])
    answers = []

    for case_number in range(1, test_count + 1):
        x = int(tokens[case_number])
        index, value = first_fibonacci_at_least(x)
        answers.append(f"Case {case_number}: {index} {value}")

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read().split()))
