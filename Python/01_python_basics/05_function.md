---
title: "[Python] Ch1: Python Basics - 05 Function"
date: 2020-06-10
series: [Python]
categories: [Python]
---

# Function 函式

```python
def 函式名稱(參數):
    程式碼
```

```python
def printf(text):
    print("[Out]: {}".format(text))
```

```python
printf('Hello world!')
```

    [Out]: Hello world!

## 閏年

根據維基百科，分辨平閏年的方法為：
1. 公元年份除以4不可整除，為平年。
2. 公元年份除以4可整除但除以100不可整除，為閏年。
3. 公元年份除以100可整除但除以400不可整除，為平年。
4. 公元年份除以400可以整除為閏年

```python
def check_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print("閏年")
        return 1
    else:
        print("平年")

    return 0
```

```python
year = int(input())
print(check_leap_year(1377))
```

    1344
    平年
    0
