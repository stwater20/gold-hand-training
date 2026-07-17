import sys
import time

def process(data):
    for line in data:
        line = line.strip()

        if line == "":
            continue

        n = int(line)

        if 1 <= n <= 999:
            hundred = n // 100
            ten = (n // 10) % 10
            one = n % 10
            sys.stdout.write(f"{hundred} {ten} {one}\n")
        else:
            sys.stdout.write("Wrong\n")


filename = ""
start = time.perf_counter()

if filename:
    with open(filename, "r", encoding="utf-8") as f:
        data_source = f.read().splitlines()
else:
    data_source = sys.stdin.read().splitlines()

process(data_source)

if filename:
    end = time.perf_counter()
    print(f"執行時間:{end - start:.7f}秒")