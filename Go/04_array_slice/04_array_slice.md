---
title: "[Go] Ch1: Go Basics - 04 Go Data Structure: `Array` & `Slice`"
date: 2020-07-11
series: [Go]
categories: [Go]
---

## Array

### 1. Creating an Array

The type `[n]T` is an array of `n` values of type `T`.

The expression

```go
var a [10]int
```

- An array's length is part of its type, so `arrays cannot be resized`. But Go provides a convenient way of working with array.

### 2. Array initialize

```go
a := [6]int{2, 3, 5, 7, 11, 13}

// or
a := []int{2, 3, 5, 7, 11, 13}
```

## Slices

A slice is a `dynamically-size, flexible` view into the elements of an array.

    Slice的長度是可變的，與Array相比，提供一種更高階的觀點看待一片資料。

- Slice also has `continuous segments` of memory locations
- The default value of uninitialized slice is `nil`
- Slices `does not store the data`. It just provides `reference to an array`

### 1. Creating a Slice

#### Method 1: like array but no size

The type `[]T` is a slice with elements of type T.

```go
var s []int // length: 0, capacity: 0 -> nil
```

#### Method 2: use `make()`

Create slice by using `make()` which is available in builtin package of golang

```go
s := make([]int, 5) // lenght == capacity == 5

// or
s := make([]int, 5, 10) // lenght: 5, capacity: 10
```

#### Method 3: `[low:high]`

A slice is formed by specifying two indices, a low and high bound, seperated by a colon:

```go
var s []type = a[low:high]

//or
s := a[low:high]
```

#### Example:

```go
// Elements 1 through 3
// a = [1, 2, 3, 4, 5]

//var s []int = a[1:4]
s := a[1:4] // [2, 3, 4]
```

- More

```go
// slice initialize
a := []int{2,3,5,7,11}

a1 = a[1:4] // [3 5 7]

a2 = a[:2] // [2 3]

a3 = a[1:] // [3 5 7 11]

a4 = a[:] // [2 3 5 7 11]
```

### 2. Slices are like references to arrays

`A slice does not store any data`, it just describes a section of an underlying array.

- Changing the elements of a slice modifies the corresponding elements of its underlying array.

```go
a := [6]int{1, 2, 3, 4, 5, 6}
fmt.Println(a) // [1 2 3 4 5 6]
b := a[1:4]
fmt.Println(b) // [2 3 4]
b[1] = 10
fmt.Println(b) // [2 10 4]
fmt.Println(a) // [1 2 10 4 5 6]
```

### 3. Slice `length` and `capacity`

A slice has both a `length` and a `capacity`.

- `length`

    The length of a slice is the number of elements it contains.

    ```
    Number of elements
    ```

- `capacity`

    The capacity of a slice is the number of elements in the underlying array

    ```
    Total size
    ```

```go
// length
len(s)

// capacity
cap(s)
```

### 4. Slices of slices

Slices can contain any type, including other slices

#### Example: 2D Array

3x3 Array

```go
matrix := [][]int{
    make([]int, 3),
    make([]int, 3),
    make([]int, 3),
}
```

`tic-tac-toe boart(井字遊戲)`

```go
board := [][]string{
    []string{"-", "-", "-"},
    []string{"-", "-", "-"},
    []string{"-", "-", "-"},
}
```

### 5. `append` function

Appending new values to the slice using built-in `append` function.

```go
func append(s []T, vs ...T) []T
```

- If the backing array of `s` is `too small` to fit all the given values a `bigger array will be allocated`. The returned `slice` will `point to the newly allocated array`.

    ```
    當append的元素個數超過原slice的capacity時，append利用現有的slice建立一個新的slice，並將後續的參數附加在這個slice之後。
    ```

```go
var s []int
s = append(s, 0)
```

### 6. `copy` function

Copying one slice into another using built-in `copy` function.


```go
func copy(dst []T, src []T) int
```

- `copy` will return the number of elements copied which is the minimum of `len(dst)` and `len(src)`.
-
    ```
    複製時，目的slice的容量必須足夠，否則會發生 cap out of range的錯誤，copy函式若執行成功，會傳回複製的元素個數。
    ```

```go
s1 := []int{1,2,3}
s2 := make([]int, 2)
copy(s1, s2)
```

### 7. `range` function

The `range` form of the `for` loop iterates over a `slice` or `map`.

When ranging over a slice, two values are returned for each iteration.

1. `index`
2. copy of the `element` at that index.

```go
var a = []int{1,2,3,4,5}

for i, v := range a {
    fmt.Printf("a[%d]: %d\n", i, v)
}
```

#### Skip the index or value

Can skip the `index` or `value` by assigning to `_`

```go
for i, _ := range array
for _, v := range array
```

If only want the index, can omit the second variable.

```go
for i := range array
```

## Exercise: Slices

Implement `Pic`. It should return a slice of length `dy`, each element of which is a slice of `dx` 8-bit unsigned integers. When you run the program, it will display your picture, interpreting the integers as grayscale (well, bluescale) values.

The choice of image is up to you. Interesting functions include `(x+y)/2`, `x*y`, and `x^y`.

```go
func Pic(dx, dy int) [][]uint8 {
    image := make([][]uint8, dy)
    for i := range image {
        image[i] = make([]uint8, dx)
        for j := range image[i] {
            image[i][j] = uint8((i+j) / 2)
        }
    }

    return image
}
```
