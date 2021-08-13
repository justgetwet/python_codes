---
layout: post
---

### 1. DataFrameの生成

```python
import pandas as pd
```

- リストから生成

```python
l1 = [0, 1, 2]
l2 = [3, 4, 5]
df = pd.DataFrame([l1, l2], columns=["A", "B", "C"])
print(df)
#    A  B  C
# 0  0  1  2
# 1  3  4  5
```

- 辞書から生成

```python
d1 = {"A": 0, "B": 1, "C": 2}
d2 = {"A": 3, "B": 4, "C": 5}
df = pd.DataFrame([d1, d2])
print(df)
#    A  B  C
# 0  0  1  2
# 1  3  4  5
```

- インデックス

```python
df = pd.DataFrame([d1, d2], index=["bob", "alice"])
print(df)
#        A  B  C
# bob    0  1  2
# alice  3  4  5
```

- 転置

```python
dic = {"bob": [0, 1, 2], "alice": [3, 4, 5]}
df = pd.DataFrame(dic, index=["A", "B", "C"])
print(df)
#    bob  alice
# A    0      3
# B    1      4
# C    2      5
print(df.T)
#        A  B  C
# bob    0  1  2
# alice  3  4  5
```

- Seriesから生成

```python
idx = ["A", "B", "C"]
s1 = pd.Series([0, 1, 2], index=idx, name="bob")
s2 = pd.Series([3, 4, 5], index=idx, name="alice")
df = pd.DataFrame([s1, s2])
print(df)
#        A  B  C
# bob    0  1  2
# alice  3  4  5
```



### 2.DataFrameの変換

- 辞書へ変換

```python
print(df)
#        A  B  C
# bob    0  1  2
# alice  3  4  5
d_dict = df.to_dict(orient="dict") # {column -> {index -> value}}
print(d_dict)
# {'A': {'bob': 0, 'alice': 3},
#  'B': {'bob': 1, 'alice': 4},
#  'C': {'bob': 2, 'alice': 5}}
```

- リストへ変換

```python
d_list = df.to_dict(orient="list") # {column -> [values]}
print(d_list)
# {'A': [0, 3], 'B': [1, 4], 'C': [2, 5]}
```

- Seriesへ変換

```python
d_series = df.to_dict(orient="series") # {column -> Series(values)}
print(d_series)
# {'A': bob      0
# alice    3
# Name: A, dtype: int64, 
# 'B': bob      1
# alice    4
# Name: B, dtype: int64, 
# 'C': bob      2
# alice    5
# Name: C, dtype: int64}
```

- htmlへ変換

```python
from IPython.display import HTML # jupyter notebook

d_html = df.to_html()
HTML(d_html)
```

### 3. DataFrameとjson

- jsonへ変換

```python
print(df.to_json())
# {"A":{"bob":0,"alice":3},"B":{"bob":1,"alice":4},"C":{"bob":2,"alice":5}}
j = df.to_json(orient="columns") # orient="columns"はデフォルト
```

- Unicodeエスケープ

```python
dic = {"ボブ": [0, 1, 2], "アリス": [3, 4, 5]}
df = pd.DataFrame(dic, index=["A", "B", "C"])
print(df.to_json(force_ascii=True)) # デフォルト
# {"\u30dc\u30d6":{"A":0,"B":1,"C":2},"\u30a2\u30ea\u30b9":{"A":3,"B":4,"C":5}}
print(df.to_json(force_ascii=False)) # 全角文字（日本語）をUnicodeエスケープしない
# {"ボブ":{"A":0,"B":1,"C":2},"アリス":{"A":3,"B":4,"C":5}}
```

- jsonファイルに保存

```python
j = df.to_json(force_ascii=False)
p = "./example.json"
with open(p, "w", encoding="utf-8") as f:
  f.write(j)
```

- jsonファイルから読み込み

```python
import json

p = "./example.json"
with open(p, "r", encoding="utf-8") as f:
  read_dic = json.load(f)
print(read_dic)
# {'ボブ': {'A': 0, 'B': 1, 'C': 2}, 'アリス': {'A': 3, 'B': 4, 'C': 5}}
df = pd.DataFrame(read_dic)
print(df.T)
#       A  B  C
# ボブ   0  1  2
# アリス  3  4  5
```



