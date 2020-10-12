---
title: "[Python] Ch1: Python Basics - 04 Dictionary"
date: 2020-06-10
series: [Python]
categories: [Python]
---

# Dictionary 字典

在字典裡，皆由key(鍵)和value(值)組成

```python
dict = {key1 : value1, key2 : value2 }
```

```python
kaka = {'firstname':'lin', 'age': 28, 'height': 175}
print(kaka)
```

    {'firstname': 'lin', 'age': 28, 'height': 175}

## 取得 Dictionary 裡有幾個元素: len()

```python
print(len(kaka))
```

    [Out]: 3

## 取得 Dictionay 裡的資料

透過`key`來取得相對應的`value`

```python
dict[key] -> return value
```

```python
kaka['age']
```

    [Out]: 28

### 取得 Dictionary 裡的所有 key

```python
dict.keys()
```

```python
kaka.keys()
```

    dict_keys(['firstname', 'age', 'height'])

### 取得 Dictionary 裡的所有 value

```python
dict.values()
```

```python
kaka.values()
```

    dict_values(['lin', 28, 175])

### 取得 Dictionary 裡的所有資料

```python
dict.items()
```

```python
kaka.items()
```

    dict_items([('firstname', 'lin'), ('age', 28), ('height', 175)])

## 增加 Dictionary 裡的資料

```python
dict[new_key] = value
```

```python
kaka['weight'] = 68
kaka
```

    {'firstname': 'lin', 'age': 28, 'height': 175, 'weight': 68}

## 更新 Dictionary 裡的資料

```python
dict[key] = new_value
```

```python
kaka['weight'] = 70
kaka
```

    {'firstname': 'lin', 'age': 28, 'height': 175, 'weight': 70}

## 移除 Dictionary 裡的資料

### del method

```python
del dict[key]
```

```python
del kaka['weight']
kaka
```

    {'firstname': 'lin', 'age': 28, 'height': 175}

### pop method

```python
dict.pop(key)
```

```python
kaka['weight'] = 70
kaka
```

    {'firstname': 'lin', 'age': 28, 'height': 175, 'weight': 70}

```python
kaka.pop('weight')
kaka
```
    {'firstname': 'lin', 'age': 28, 'height': 175}


## 檢查指定的key是否存在於Dictionary中

```python
key in dict -> return True 或是 False
```

```python
'firstname' in kaka
```

    [Out]: True

```python
'weight' in kaka
```

    [Out]: False

## Dictionary 與 for-loop

```python
for k, v in kaka.items():
    print('{}: {}'.format(k, v))
```

    firstname: lin
    age: 28
    height: 175

### 用 for-loop 來建立 Dictionary

```python
temp = {}
for i in range(10):
    temp[i] = i ** 2
temp
```

    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

### pyhonic

```python
a = {x: x ** 2 for x in range(10)}
a
```

    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
