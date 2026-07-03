import sys
import time

# 主要程式開始
def process(data): # 主要的解題邏輯放在這裡
    for line in data:
        # 讀取每一行，並將其拆分為兩個整數 a 和 b
        a, b = map(int, line.split())
        sys.stdout.write(f"{a + b}\n")

filename = "sample.in"  # 設定檔案名稱
start = time.perf_counter()  # 開始計時

if filename:
    with open(filename, 'r', encoding='utf-8') as f:  # 自動關閉檔案
        data_source = f.read().splitlines()  # 使用 splitlines 處理換行
else:
    data_source = sys.stdin.read().splitlines()  # 一次性讀取 stdin

process(data_source)

if filename:
    end = time.perf_counter()  # 結束計時
    print(f"執行時間:{end - start:.7f}秒") # 輸出執行時間
