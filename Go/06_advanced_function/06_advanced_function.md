---
title: "[Go] Ch1: Go Basics - 06 Advanced Function"
date: 2020-07-18
series: [Go]
categories: [Go]
---

## Function as Arguments

In Go, `function is also a type`. So we can pass function as another function's parameters.

當我們將function當成參數使用時，必須在參數列表列出funtion本身的參數type與及其所需的回傳type, 如:

```go
func(int, int) int
```

### Example 1

```go
func print(fn func(int, int) int, a, b int) {
    fmt.Println(fn(a, b))
}

func area(a, b int) int {
    return a * b
}

func sum(a, b int) int {
    return a + b
}

func main() {
    print(area, 3, 4) // 12
    print(sum, 3, 4) // 7
}
```

### Example 2

```go
func compute(fn func(float64, float64) float64) float64 {
    return fn(3, 4)
}

func hypot(x, y float64) float64 {
    return math.Sqrt(x*x + y*y)
}

func main() {
    fmt.Println(compute(hypot)) // 5
}
```

## Function Closures

Golang supports [anonymous functions(匿名函式)](https://en.wikipedia.org/wiki/Anonymous_function) which can form [closures(閉包)](https://en.wikipedia.org/wiki/Closure_(computer_programming)). `Anonymous functions` are useful when you want to `define a function inline without having to name it`.

### Anonymous Function

```
所謂的匿名函式就是沒有名字的函式
```

- 匿名函式可以作為返回值
- 匿名函式也可以作為變數

#### Example

```go
// anonymous function
func(x, y int) int {
    return x + y
}

// anonymous function as a return value
func printSum() func(int, int) {
	return func(x, y int) {
		fmt.Println(x + y)
	}
}

// anonymous function as a variable
f := func(x, y int) int {
    return x + y
}
```

- Python's `lambda`

```python
# anonymous function
lambda x, y: x + y

f = lambda x, y: x + y
```

### Closure

A closure is a function value that references variables from outside its body

```
閉包就是能夠讀取其他函式內部變量的函式。好處是可以把變數隱藏在內部，讓外部存取不到，只能看到我們想要提供的值
```

#### Example 1

```go
func intSeq() func() int {
    i := 0
    return func() int {
        i += 1
        return i
    }
}

func main() {
    nextInt := intSeq()
    fmt.Println(nextInt()) // 1
	fmt.Println(nextInt()) // 2
	fmt.Println(nextInt()) // 3
}
```

上例將變數`i`隱藏在內部匿名函式中，我們無法對變數`i`進行操作，只能拿到他的值。

#### Example 2

```go
func adder() func(int) int {
    sum := 0
    return func(x int) int {
        sum += x
        return sum
    }
}
```

- Closure in Python

```python
def printMessage():
    string = "This is closure"
    def print_msg():
        print(string)
    return print_msg
```

### Exercise: Fibonacci closure

```go
// fibonacci is a function that returns
// a function that return an int.
func fibonacci() func() int {
	a, b := 0, 1
	return func() int {
		v := a
		a, b = b, a+b
		return v
	}
}
```
