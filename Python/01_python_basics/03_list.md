---
title: "[Python] Ch1: Python Basics - 03 List"
date: 2020-06-10
series: [Python]
categories: [Python]
---

# List 串列

`List` 用來儲存一連串有順序的資料，如：

```python
countries = ['Taiwan', 'Janpan', 'America']
print(countries)
```

    ['Taiwan', 'Janpan', 'America']

## 取得 List 裡有幾個元素: len()

```python
length = len(countries)
length
```

    [Out]: 3

## 取得List 裡的元素

```python
list_name[index]
```

```python
countries[0]
```

    [Out]: 'Taiwan'

### 取得最後一個元素

```python
list[-1]
```

```python
print(countries[-1])
```

    [Out]: America

```python
list.index(x[, start[, end]])
```

### 範圍取值: list slicing

```python
list[start_index:end_index:sep]
```

```python
countries[0:1]
```

    [Out]: ['Taiwan']

```python
countries[::3]
```

    [Out]: ['Taiwan']

## 增加 List 裡面的元素

### append method

```python
list.append(object)
```

將一個新的元素加到 list 的尾端。

```python
countries.append('Korea')
countries
```

    ['Taiwan', 'Janpan', 'America', 'Korea']

### insert method

```python
list.insert(position, object)
```

將一個新的元素加到指定的 list 位置。

```python
countries.insert(-1, 'China')
countries
```

    ['Taiwan', 'Janpan', 'America', 'China', 'Korea']

### extend method

```python
list_1 = [object1, object2, object3, ...]
list_2 = [object0]
list_2.extend(list_1)
```

```python
countries_2 = ['Malaysia', 'Singapore']
countries.extend(countries_2)
countries
```

    ['Taiwan', 'Janpan', 'America', 'China', 'Korea', 'Malaysia', 'Singapore']

## 移除 List 裡的元素

### remove method

```python
list.remove(object)
```

```python
countries.remove('China')
countries
```

    ['Taiwan', 'Janpan', 'America', 'Korea', 'Malaysia', 'Singapore']

### pop method

```python
list.pop(index)
```

如果括號內不指定index, 預設是最後一個元素(-1)

```python
countries.pop()
countries
```

    ['Taiwan', 'Janpan', 'America', 'Korea', 'Malaysia']

## List 與 for-loop

```python
for item in list:
    print(item)
```

```python
for country in countries:
    print(country, end=', ')
```

    Taiwan, Janpan, America, Korea, Malaysia,

### 用 for-loop 來建立 List

```python
temp = []
for i in range(10):
    temp.append(i ** 2)
temp
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

### pyhonic

```python
a = [x ** 2 for x in range(10)]
a
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```python
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = [x ** 2 for x in b]
c
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81]
