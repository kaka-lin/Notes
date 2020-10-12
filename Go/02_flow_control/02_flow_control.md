---
title: "[Go] Ch1: Go Basics - 02 Flow Control"
date: 2020-07-11
series: [Go]
categories: [Go]
---

## For

Go has `only one looping construct`, the `foor` loop

```go
for <init state>; <condition>; <post state>
```

```go
sum := 0
for i := 0; i < 10; i++ {
    sum += i
}
```

- Go的for看起來跟C或Java中的依樣，但是沒有 `()`，但`{}`是必要的，如上所示。

#### Note

`For的 init 和 post statements可以為空。`

```go
sum  :=1
for ; sum < 1000; {
    sum += sum
} // 1024
```

## While

`Go沒有While`, 因為可以省略分號(`;`)，C的while在Go中就是for

```go
sum := 1
for sum < 1000 {
    sum += sum // 1024
}
```

#### Infinite loop

```go
for {
    // do something
}
```

## If

Go's `if` statements are like its `for` loops; the expression need not be surrounded by parentheses ` ( )` but the braces `{ }` are required.

```go
if <condition> {
    // do something
}
```

### If with a short statement

跟`for`一樣，`if`可以在條件之前執行一個簡單的語句，這個語句的作用範圍僅在`if`的範圍內

```go
func pow(x, n, lim float64) float64 {
    if v := math.Pow(x, n); v < lim {
        return v
    }
    return lim
}
```

### If and else

```go
func pow(x, n, lim float64) float64 {
    if v := math.Pow(x, n); v < lim {
        return v
    } else {
        fmt.Printf("%g >= %g\n", v, lim)
    }
    return lim
}
```

## Exercise: Loop and Functions

#### 用牛頓法實現開根號函式

- 牛頓法:

    選擇一個初始點，然後帶入下面公式重覆計算，來求`Sqrt(x)`的近似值

    $z = z - ((z^2 - x) / 2z)$

此練習我們宣告一個浮點數`1.0`當作我們的初始值，並且重覆計算10次，觀察結果是否與`math.Sqrt()`相近

```go
package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	// define init value
	z := 1.0
	cal_times := 10

	for cal_times > 0 {
		z -= (z*z - x) / (2 * x)
		cal_times -= 1
	}
	return z
}

func main() {
	fmt.Println(Sqrt(4))
	fmt.Println(math.Sqrt(4))
}
```

## Switch

Go's `switch` is like the one in C, C++, Java, Javascript, and PHP.

- Go的`switch`會自動提供`break`在每個case的結尾，所以不用自己寫
- Go的`swich case不必為常數，且值也不必為整數`

```go
switch os := runtime.GOOS; os {
    case "drawin":
        fmt.Println("OS X.")
    case "linux":
        fmt.Println("Linux.")
    default:
        fmt.Printf("%s.\n", os)
}
```

## Defer

A `defer` statement defers the execution of a function until the surrounding function returns.

    The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.

```go
func main() {
    defer fmt.Println("world")

    fmt.Println("hello")
}
```

[Output]:

```
hello
world
```

### Sracking defers

Deferred function calls are pushed onto a `stack`.

    When a function returns, its deferred calls are executed in last-in-first-out order.

```go
func main() {
    fmt.Println("counting")

    for i := 0; i < 10; i++ {
        defer fmt.Println(i)
    }

    fmt.Println("done")
}
```

[Output]:

```
counting
done
9
8
7
6
5
4
3
2
1
0
```
