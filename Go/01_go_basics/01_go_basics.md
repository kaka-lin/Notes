---
title: "[Go] Ch1: Go Basics - 01 Go Basics"
date: 2020-07-11
series: [Go]
categories: [Go]
---

## Packages (套件)

每個 `Go Program` 都是由`套件(packages)`組成的

程式運行的入口是: package `main`

```go
package main

func main() {}
```

## Import

```go
import (
    "fmt"
    "math"
)
```

## Exported names

In Go, a name is `exported` if it begins with a `capital letter`.

For example, `Pi` is an exported name which is from the `math` package.

## Variables

The `var` statement declares a list of variables; as in function arguments lists, the type is last.

```go
// statement (陳述)
var i int

// expression (表達)
var j = 2
```

- 如果變數初始化是使用表達，則可以省略型別，如上所示。變數從初始值中獲得型別。

## Short variable declarations

`:=` short assignment statement

在函式中，在明確類型的地方可以用 `:=` 取代 `var`。

```go
var k = 3

// equal
k := 3
```

## Functions

Define with function `func`.

### Functions continued

When two or more consecutive named function parameters share a type, you can omit the type from all but the last.

```go
x int, y int

// equal
x, y int
```

### Multiple results

```go
func swap(x, y string) (string, string) {
    return y, x
}
```

### Named return values

Go's return values may be named. If so, they are treated as variables defined at the top of the function.

```go
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}
```

- These names should be used to document the meaning of the return value.
- A return statement without arguments returns the named return values. This is known as a `"naked" return`.
- `Naked return` statements should be used only in short functions, as with the example show here. They can harm readability in longer functions.

## Basic types

```go
bool

string

int int8 int32 int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32

float32 float64

complex64 complex128
```

### Zero values

Variables declared without an explicit initial value are given their `zero value`

The `zero value` is:

- numeric type: `0`
- boolean type: `false`
- strings: `""`

### Type coversions (型別轉換)

The expression(表達式) `T(v)` convers the value to the type `T`.

```go
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)

// or
i := 42
f := float64(i)
u := uint(f)
```

### Type inference

When declaring a variable without specifying an explicit type (either by using the `:=` syntax or `var = ` expression syntax), the variable's type is `inferred from the value on the right hand side`.

```go
var i int
j := i // j is an int
```

### Constants

Constants are declared like variable, but with the `const` keyword.

- Constants can be charater, string, boolean, or numeric values.

- Constants cannot be declared using the `:=` syntax.

```go
const World = "世界"
```

### Numeric Constants

Numeric constants are `high-precision` values.

    An untyped constant takes the type needed by its context.

```go
const (
    // Create a huge number by shifting a 1 bit left 100 places.
    // In other words, the binary number that is 1 followed by 100 zeroes.
    Big = 1 << 100

    // Shift it right again 99 places, so we end up with 1<<1, or 2.
    Small = Big >> 99
)
```
