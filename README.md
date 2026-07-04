# 金手培訓 Gold Hand Programming

本專案是高級中等學校技藝競賽選手（程式設計）培訓課程教材，由三重商工資料處理科林易民老師與陳勝舢博士共同製作。內容以「全國高級中等學校學生商業類技藝競賽－程式設計職種」為目標，涵蓋 Python 基礎語法、演算法與時間複雜度、常見競賽解題技巧，以及 DOMjudge 線上評測系統使用說明與歷屆試題。（滾動式新增）

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
| 4 | [`4_merge_sort_recursion_time_complexity.ipynb`](4_merge_sort_recursion_time_complexity.ipynb) | 合併排序、遞迴與時間複雜度 |
| 5 | [`5_python_fast_io_demo_v3.ipynb`](5_python_fast_io_demo_v3.ipynb) | 快速 I/O（`sys.stdin`）技巧 |
| 6 | [`6_python_performance_tips_demo.ipynb`](6_python_performance_tips_demo.ipynb) | 常見效能寫法比較 |
| 7 | [`7_python_map_demo.ipynb`](7_python_map_demo.ipynb) | `map` 內建函式 |
| 8 | [`8_python_zip_demo.ipynb`](8_python_zip_demo.ipynb) | `zip` 內建函式 |
| 9 | [`9_python_lru_cache_dp_demo.ipynb`](9_python_lru_cache_dp_demo.ipynb) | `functools.cache` / `lru_cache` 與動態規劃 |
| 10 | [`10_python_reduce_lambda_demo.ipynb`](10_python_reduce_lambda_demo.ipynb) | `reduce` + `lambda` |
| 11 | [`11_python_filter_demo.ipynb`](11_python_filter_demo.ipynb) | `filter` 內建函式 |
| 12 | [`12_python_bisect_demo.ipynb`](12_python_bisect_demo.ipynb) | `bisect` 二分搜尋模組 |

### 競賽程式模板（[`contest_template/`](contest_template/)）

提供可直接套用的讀檔／stdin 輸入輸出模板，方便學生在本地測試與正式上場提交間快速切換。

### DOMjudge 說明文件（[`domjudge_manual/`](domjudge_manual/)）

說明 DOMjudge v8 線上評測系統的登入、提交、積分板等使用方式，以及 Python 在 DOMjudge 上處理標準輸入輸出的常見寫法。

### 競賽官方文件（[`competition_documents/`](competition_documents/)）

收錄全國高級中等學校學生商業類技藝競賽「程式設計」職種的簡章、競賽規則說明會議紀錄，以及 110～114 學年度歷屆學科與術科正式試卷。（請依官方資料為主）

## 使用方式

各 `.ipynb` 檔案可直接以 Jupyter Notebook / JupyterLab 或 VS Code 開啟閱讀與執行；建議依檔名編號順序學習。

## 授權 License

本專案採用 [創用 CC 姓名標示-非商業性-相同方式分享 4.0 國際 (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-Hant) 授權條款，詳見 [LICENSE](LICENSE)。


> 註：`competition_documents/` 內之競賽官方文件（簡章、規則說明會議紀錄、歷屆試卷等）著作權歸主辦單位所有，不適用上述授權條款；本專案僅收錄供學習參考。
