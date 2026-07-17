#!/usr/bin/env python3
"""
核心演算法
========
對每個數列的四項 a、b、c、d：

1. 計算三個相鄰差值：b-a、c-b、d-c。
2. 若三個差值完全相等，數列為等差數列，輸出「A」與公差 b-a。
3. 否則依題目保證，數列必為等比數列，輸出「G」與公比 b/a。

程式使用 Fraction 儲存所有數值，不使用 float，因此像 2.4 之類的小數
在相減、相除及比較時都不會產生浮點誤差。

若共有 t 個數列：
- 時間複雜度：O(t)
- 額外空間複雜度：O(t)（用來保存最後輸出的 t 行答案）
"""

from fractions import Fraction
import sys


def format_number(value: Fraction) -> str:
    """將 Fraction 轉成題目要求的整數或有限小數格式。"""
    # 分母為 1 代表答案是整數，直接輸出分子即可。
    if value.denominator == 1:
        return str(value.numerator)

    # 有限小數的最簡分母只會包含質因數 2 與 5。
    # 記錄兩者的次方，便能算出需要保留幾位小數。
    denominator = value.denominator
    twos = fives = 0
    while denominator % 2 == 0:
        denominator //= 2
        twos += 1
    while denominator % 5 == 0:
        denominator //= 5
        fives += 1

    # 題目保證答案可用有限小數表示；保留此分支可提高程式完整性。
    if denominator != 1:
        return f"{value.numerator}/{value.denominator}"

    # 將分數放大成整數，再自行插入小數點，可避免浮點數誤差。
    places = max(twos, fives)
    scaled = abs(value.numerator) * (10 ** places) // value.denominator
    digits = str(scaled).rjust(places + 1, "0")
    if places:
        result = digits[:-places] + "." + digits[-places:]
        # 移除小數末尾多餘的 0，例如將 2.400 轉成 2.4。
        result = result.rstrip("0").rstrip(".")
    else:
        result = digits
    if value < 0:
        result = "-" + result
    return result


def solve(tokens: list[str]) -> str:
    """依序判斷每個數列，回傳所有輸出行。"""
    if not tokens:
        return ""

    count = int(tokens[0])
    pos = 1
    answers = []

    for _ in range(count):
        # 使用 Fraction 讀取整數或小數，讓所有比較都是精確運算。
        values = [Fraction(token) for token in tokens[pos:pos + 4]]
        pos += 4
        a, b, c, d = values

        # 三組相鄰項的差都相等時，這是一個等差數列。
        if b - a == c - b == d - c:
            answers.append("A " + format_number(b - a))
        else:
            # 題目保證數列必為兩種類型之一，因此其餘情況為等比數列。
            # 公比等於第二項除以第一項。
            answers.append("G " + format_number(b / a))

    return "\n".join(answers)


if __name__ == "__main__":
    # 一次讀入所有以空白分隔的資料，最後一次輸出答案。
    output = solve(sys.stdin.read().split())
    if output:
        print(output)
