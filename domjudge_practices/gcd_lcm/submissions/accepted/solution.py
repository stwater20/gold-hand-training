#!/usr/bin/env python3
"""
核心演算法
========
逐組讀取 a、b，使用歐幾里得算法（math.gcd）求最大公因數。
若 a、b 不同時為 0，最小公倍數可由下式求得：

    LCM(a,b) = abs(a // GCD(a,b) * b)

先做除法再乘法，可降低固定大小整數語言發生溢位的風險。
若有 m 組資料，時間複雜度為 O(m log(max(|a|,|b|)))。
"""

import math
import sys


def solve(tokens: list[str]) -> str:
    blocks = []

    # 輸入直到 EOF；每兩個 token 形成一組測試資料。
    for case_number, position in enumerate(range(0, len(tokens), 2), start=1):
        a = int(tokens[position])
        b = int(tokens[position + 1])
        lines = [f"Case {case_number}:"]

        # GCD(0,0) 與 LCM(0,0) 在本題中視為沒有定義。
        if a == 0 and b == 0:
            lines.append("no GCD")
            lines.append("no LCM")
        else:
            gcd_value = math.gcd(a, b)  # math.gcd 的結果保證非負。
            lcm_value = abs(a // gcd_value * b)
            lines.append(f"GCD({a},{b}) = {gcd_value}")
            lines.append(f"LCM({a},{b}) = {lcm_value}")

        blocks.append("\n".join(lines))

    # 每組輸出之間空一行，最後一組後面不額外加入空行。
    return "\n\n".join(blocks)


if __name__ == "__main__":
    answer = solve(sys.stdin.read().split())
    if answer:
        print(answer)
