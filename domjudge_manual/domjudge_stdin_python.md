# 程式輸入輸出範例

## DOMjudge 與本地 stdin 測試方式

DOMjudge 執行程式時，會把測試資料送到程式的標準輸入（stdin）。在 DOMjudge 介面上通常只需要上傳 source code 檔案，不需要在程式中開啟 `in.txt` 或其他固定檔名。

本地環境可以先把範例測資存成 `in.txt`，再用重新導向模擬 DOMjudge 的輸入方式：

```bash
python3 main.py < in.txt
```

Online Judge 的輸出必須和題目要求完全一致，請不要多印提示文字，例如 `請輸入數字:`。

## Online Judge 常見輸入格式

常見的輸入格式大致可分為：

- 固定行數：題目明確指定輸入格式與行數。
- 不定行數：題目要求讀到特定條件，或一直讀到 EOF（End of File，檔案結束）。

以下範例只保留 Python 3.9 寫法。片段重點是讀取 stdin 與輸出 stdout，可依題目邏輯替換中間的計算。

### 固定行數：單行單值

讀入一個整數 `year`，輸出 `year - 1911`。

範例輸入：

```text
2008
```

範例輸出：

```text
97
```

Python 3.9：

```python
year = int(input())
print(year - 1911)
```

### 固定行數：單行多值

讀入同一行的多個整數，輸出總和。

範例輸入：

```text
2 3 4
```

範例輸出：

```text
9
```

Python 3.9：

```python
nums = list(map(int, input().split()))
print(sum(nums))
```

### 固定行數：第一行指定資料筆數

第一行讀入 `n`，接著讀取 `n` 筆資料。

範例輸入：

```text
3
1 2
10 20
-3 4
```

範例輸出：

```text
3
30
1
```

Python 3.9：

```python
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)
```

### 不定行數：讀到特定條件結束

每行讀入兩個整數，直到讀到 `0 0` 結束，不處理結束那一行。

範例輸入：

```text
1 2
10 20
0 0
```

範例輸出：

```text
3
30
```

Python 3.9：

```python
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)
```

### 不定行數：讀到 EOF

測資沒有先給行數，也沒有結束符號時，就持續讀到 EOF。

範例輸入：

```text
22 1
23 1
24 1
```

範例輸出：

```text
23
24
25
```

Python 3.9：

```python
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)
```

### 資料型態轉換與逗號分隔

從 stdin 讀進來的資料一開始通常都是字串；題目要求整數、小數或其他型態時，要先轉型。若資料使用逗號分隔，就不能只用空白分隔的寫法。

範例輸入：

```text
1,2,3
```

範例輸出：

```text
6
```

Python 3.9：

```python
line = input()
a, b, c = map(int, line.split(","))
print(a + b + c)

nums = [int(x) for x in line.split(",")]
```

---

## 範例輸入資料

```text
# in.txt
22 1
23 1
24 1
```

## 範例輸出資料

```text
23
24
25
```

---

## 完整範例程式碼

### Python 程式碼

danger
Windows 上 Python 會有些功能無法與其他 OS 產生相同結果，請勿使用字串檔案路徑，請使用例如 `os` 等內建函式庫。


`main.py`

```python
import sys

for line in sys.stdin.read().splitlines():  # splitlines 會去除不同 OS 的換行符號
    nums = [int(num) for num in line.split()]
    # nums = map(int, line.split())
    print(sum(nums))
```

執行方式：

```bash
python main.py < in.txt
```
