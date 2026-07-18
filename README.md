# 金手培訓 Gold Hand Programming

本專案是高級中等學校技藝競賽選手（程式設計）培訓課程教材，由三重商工資料處理科林易民老師與陳勝舢博士共同製作。內容以「全國高級中等學校學生商業類技藝競賽－程式設計職種」為目標，涵蓋 Python 基礎語法、演算法與時間複雜度、常見競賽解題技巧、DOMjudge 線上評測系統使用說明與練習題，以及歷屆試題。（滾動式新增）

## 比賽用 VM

[https://inc-s3.ntub.edu.tw/share-files/judge-vm/judge-client/2026/Windows.zip](https://inc-s3.ntub.edu.tw/share-files/judge-vm/judge-client/2026/Windows.zip)

## 教材內容說明

### Python 教學筆記本（Jupyter Notebook）

依編號循序漸進，從基礎語法開始，逐步進入時間複雜度、遞迴、效能優化，以及競賽常用的內建函式：

| 編號 | 檔案 | 主題 |
| --- | --- | --- |
| 0 | [`0_python_basics.ipynb`](0_python_basics.ipynb) | 基礎語法：f-string、Packing/Unpacking、Shallow/Deep Copy |
| 0 | [`0_python_time_complexity_bubble_merge_demo.ipynb`](0_python_time_complexity_bubble_merge_demo.ipynb) | 時間複雜度入門：泡沫排序 vs 合併排序示範 |
| 1 | [`1_c_cpp_python_run_speed.ipynb`](1_c_cpp_python_run_speed.ipynb) | C/C++ 與 Python 執行速度比較 |
| 2 | [`2_python_coding_principles.ipynb`](2_python_coding_principles.ipynb) | 程式撰寫風格與原則 |
| 3 | [`3_python_recursion.ipynb`](3_python_recursion.ipynb) | 遞迴基礎 |
| 4 | [`4_sequence_and_gcd_lcm.ipynb`](4_sequence_and_gcd_lcm.ipynb) | 等差／等比數列與 GCD／LCM |
| 5 | [`5_python_fast_io_demo_v3.ipynb`](5_python_fast_io_demo_v3.ipynb) | 快速 I/O（`sys.stdin`）技巧 |
| 6 | [`6_python_performance_tips_demo.ipynb`](6_python_performance_tips_demo.ipynb) | 常見效能寫法比較 |
| 7 | [`7_python_map_demo.ipynb`](7_python_map_demo.ipynb) | `map` 內建函式 |
| 8 | [`8_python_zip_demo.ipynb`](8_python_zip_demo.ipynb) | `zip` 內建函式 |
| 9 | [`9_python_lru_cache_dp_demo.ipynb`](9_python_lru_cache_dp_demo.ipynb) | `functools.cache` / `lru_cache` 與動態規劃 |
| 10 | [`10_python_reduce_lambda_demo.ipynb`](10_python_reduce_lambda_demo.ipynb) | `reduce` + `lambda` |
| 11 | [`11_python_filter_demo.ipynb`](11_python_filter_demo.ipynb) | `filter` 內建函式 |
| 12 | [`12_python_bisect_demo.ipynb`](12_python_bisect_demo.ipynb) | `bisect` 二分搜尋模組 |
| 13 | [`13_python_defaultdict_demo.ipynb`](13_python_defaultdict_demo.ipynb) | `collections.defaultdict` |
| 14 | [`14_python_ordereddict_demo.ipynb`](14_python_ordereddict_demo.ipynb) | `collections.OrderedDict` |
| 15 | [`15_python_base_conversion.ipynb`](15_python_base_conversion.ipynb) | 進位轉換 |
| 16 | [`16_python_float_decimal.ipynb`](16_python_float_decimal.ipynb) | 浮點數精度與 `Decimal` |
| 17 | [`17_python_set_demo.ipynb`](17_python_set_demo.ipynb) | `set` 集合操作 |
| 18 | [`18_python_list_comprehension.ipynb`](18_python_list_comprehension.ipynb) | List 與 List Comprehension |
| 19 | [`19_python_prefix_sum.ipynb`](19_python_prefix_sum.ipynb) | List 插入代價與前綴和（Prefix Sum） |
| 20 | [`20_python_queue_stack_deque.ipynb`](20_python_queue_stack_deque.ipynb) | 佇列、堆疊與 `deque` |
| 21 | [`21_python_binary_tree.ipynb`](21_python_binary_tree.ipynb) | 二元樹（Binary Tree） |
| 22 | [`22_python_counter_demo.ipynb`](22_python_counter_demo.ipynb) | `collections.Counter` |
| 23 | [`23_python_sorting_demo.ipynb`](23_python_sorting_demo.ipynb) | `sorted()`、`sort()` 與自訂比較函數 |
| 24 | [`24_python_permutations_combinations.ipynb`](24_python_permutations_combinations.ipynb) | 排列、組合與位元運算 |
| 25 | [`25_python_math_prime_gcd.ipynb`](25_python_math_prime_gcd.ipynb) | `math` 模組、GCD 與質數 |
| 26 | [`26_python_product_demo.ipynb`](26_python_product_demo.ipynb) | `itertools.product` 笛卡兒積 |
| 27 | [`27_python_heapq_demo.ipynb`](27_python_heapq_demo.ipynb) | `heapq` 堆積與優先佇列 |
| 28 | [`28_python_calendar_pow.ipynb`](28_python_calendar_pow.ipynb) | `calendar.isleap` 與三參數 `pow()` |

### 演算法教學筆記本（[`algorithm/`](algorithm/)）

以常見競賽題型示範迴圈、遞迴及圖形搜尋的基本觀念：

| 編號 | 檔案 | 主題 |
| --- | --- | --- |
| 1 | [`01_factorial.ipynb`](algorithm/01_factorial.ipynb) | 階乘：使用迴圈累積答案 |
| 2 | [`02_fibonacci.ipynb`](algorithm/02_fibonacci.ipynb) | 費波那契數列：使用兩個變數迭代 |
| 3 | [`03_tower_of_hanoi.ipynb`](algorithm/03_tower_of_hanoi.ipynb) | 河內塔：使用遞迴拆解問題 |
| 4 | [`04_dfs.ipynb`](algorithm/04_dfs.ipynb) | 深度優先搜尋（DFS） |
| 5 | [`05_bfs.ipynb`](algorithm/05_bfs.ipynb) | 廣度優先搜尋（BFS） |

### 競賽程式模板（[`contest_template/`](contest_template/)）

提供可直接套用的讀檔／stdin 輸入輸出模板，方便學生在本地測試與正式上場提交間快速切換。

### DOMjudge 說明文件（[`domjudge_manual/`](domjudge_manual/)）

說明 DOMjudge v8 線上評測系統的登入、提交、積分板等使用方式，以及 Python 在 DOMjudge 上處理標準輸入輸出的常見寫法。

### DOMjudge 練習題（[`domjudge_practices/`](domjudge_practices/)）

每題包含題目 PDF、範例與秘密測資、DOMjudge 設定，以及參考解答；同名 `.zip` 檔可直接匯入 DOMjudge。

| 題目 | 練習重點 |
| --- | --- |
| [等差數列或等比數列](<domjudge_practices/Arithmetic or geometric sequence/>) | 數列判斷與浮點數處理 |
| [階乘變化：下降階乘](domjudge_practices/falling_factorial/) | 階乘與迴圈 |
| [Fibonacci 變化：第一個達標數](domjudge_practices/fibonacci_threshold/) | Fibonacci 數列與門檻搜尋 |
| [GCD 與 LCM](domjudge_practices/gcd_lcm/) | 最大公因數與最小公倍數 |
| [河內塔變化：查詢第 k 步](domjudge_practices/hanoi_kth_move/) | 遞迴與步驟定位 |

### 競賽官方文件（[`competition_documents/`](competition_documents/)）

收錄全國高級中等學校學生商業類技藝競賽「程式設計」職種的簡章、競賽規則說明會議紀錄，以及 110～114 學年度歷屆學科與術科正式試卷。（請依官方資料為主）

## 使用方式

各 `.ipynb` 檔案可直接以 Jupyter Notebook、JupyterLab 或 VS Code 開啟閱讀與執行；建議先依根目錄檔名編號學習 Python，再進入 `algorithm/` 練習演算法，最後使用 `domjudge_practices/` 進行題目實作與評測。

## 授權 License

本專案採用 [創用 CC 姓名標示-非商業性-相同方式分享 4.0 國際 (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-Hant) 授權條款，詳見 [LICENSE](LICENSE)。


> 註：`competition_documents/` 內之競賽官方文件（簡章、規則說明會議紀錄、歷屆試卷等）著作權歸主辦單位所有，不適用上述授權條款；本專案僅收錄供學習參考。
