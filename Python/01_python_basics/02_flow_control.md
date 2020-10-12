---
title: "[Python] Ch1: Python Basics - 02 Flow Control"
date: 2020-06-10
series: [Python]
categories: [Python]
---

# Flow Control

## Python `if ... else`

The general syntax for Python's if statement is this:

```python
if condition1:
    # statement1 for True condition1
elif condition2 :
    # statement2 for True condition2
elif condition3 :
    # statement3 for True condition3
else:
    # statements for each condition False
```

```python
score = int(input("請輸入成績"))
if score >= 60:
    print("成績及格!")
else:
    print("不及格，被當了!")
```

    請輸入成績45
    不及格，被當了!

```python
# Click below for a solution

score = int(input("score: "))
if score >= 90:
    print('Grade is: A')
elif score >= 80:
    print('Grade is: B')
elif score >= 70:
    print('Grade is: C')
elif score >= 60:
    print('Grade is: D')
else:
    print('Grade is: F')
```

    score: 90
    Grade is: A

## Python `for ` loops

Python's `for` loop reuses the `in` keyword, and has the following syntax:

```python
for variable in iterable:
    # suite
```

```python
sequences = [0, 1, 2, 3, 4]
for i in sequences:
    print(i)
```

    0
    1
    2
    3
    4

```python
countries = ['Denmark', 'Finland', 'Norway', 'Sweden', 'Taiwan']
for country in countries:
    print(country)
```

    Denmark
    Finland
    Norway
    Sweden
    Taiwan

```python
for i in range(10):
    print(i, end=' ')
```

    0 1 2 3 4 5 6 7 8 9

### `Nested for loops`

```python
# 99乘法表
for i in range(1, 10):
    for j in range(1, 10):
        if j == 9:
            print('\t', i * j)
        else:
            print('\t', i * j, end=' ')
```

    	 1 	 2 	 3 	 4 	 5 	 6 	 7 	 8 	 9
    	 2 	 4 	 6 	 8 	 10 	 12 	 14 	 16 	 18
    	 3 	 6 	 9 	 12 	 15 	 18 	 21 	 24 	 27
    	 4 	 8 	 12 	 16 	 20 	 24 	 28 	 32 	 36
    	 5 	 10 	 15 	 20 	 25 	 30 	 35 	 40 	 45
    	 6 	 12 	 18 	 24 	 30 	 36 	 42 	 48 	 54
    	 7 	 14 	 21 	 28 	 35 	 42 	 49 	 56 	 63
    	 8 	 16 	 24 	 32 	 40 	 48 	 56 	 64 	 72
    	 9 	 18 	 27 	 36 	 45 	 54 	 63 	 72 	 81

## Python `while` loops

The `while` statement is used to execute a suite zero or more times,
the number of times depending on the state of the while loop's condition.
Here's the syntax:

```python
while boolean_expression:
    # Body of while
```

```python
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
```

    1 2 3 4 5 6 7 8 9 10

## `break` and `continue`

```python
# break

i = 0
while True:
    i += 1
    if i == 10:
        break
    print(i, end=' ')

```

    1 2 3 4 5 6 7 8 9

```python
# continue

i = 0
while i < 10:
    i += 1
    if i == 4:
        continue
    print(i, end=' ')
```

    1 2 3 5 6 7 8 9 10

## Exercise: Guessing Game

```python
import random

number = random.randint(1, 100)

print('Guess the number!')

while True:
    print('Please enter your guess:')
    guess = int(input())
    if guess == number:
        print('Good job')
        break
    elif guess < number:
        print('Your guess is too low')
    else:
        print('Your guess is too heigh')
```
