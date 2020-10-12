---
title: "[Go] Ch1: Go Basics - 07 Methods and Interfaces"
date: 2020-08-04
series: [Go]
categories: [Go]
---

# Methods and Interfaces

Learn how to define `methods` on types, how to declare `interfaces`,
and how to put everything together.

## Methods (方法)

`Go does not classes`. However, you can define `methods on types`.

```
A method is a function with a special receiver argument.
```

- The `receiver` appears in its own argument list between the `func` keword and the method name.

### Example

The `Abs()` method has a `receiver` of type Vertex named v.

```go
type Vertex struct {
    X, Y float64
}

func (v Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
```

### Method on Non-struct type

```go
type MyFloat float64

func (f MyFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}
```

```
Can only delcare a method with a receiver whose
type is defined in the sampe packages as method.
```

### Pointer receivers

Can declare methods with `pointer receivers`.

The receiver type has the literal syntax `*T`
for some type T.

```
Methods with pointer receivers can modify the value to which the receiver points.

Since methods often need to modify their receiver,
pointer receivers are more common than value receivers.
```

```go
func (v *Vertex) Scale(f float64) {
    v.X = v.X * f
    v.Y = v.Y * f
}
```

### Choosing a value or pointer receiver

有兩種使用`pointer receiver`的優點:

1. 可以修改`receiver`指向的值
2. 因為pointer是參考到同一個位址，所以可以避面在每次method call都複製一次值。這樣比較有效率，尤其當`receiver`是一個很大的資料結構時。

```
通常在給定的Type上都有value或pointer receiver。
但不能兩者混用。
```

## Interfaces (介面)

```
A Interface type is defined as a set of method
signatures.
```

介面(Interface)就是只有宣告方法，但沒有實作的型別，如下所示:

```go
type IVertex interface {
    X() float64
    Y() float64
    SetX(float64)
    SetY(float64)
    Abs() float64
}

type Vertex struct {
    x float64
    y float64
}
```

### Implement methods of an interface

`Interfaces are implemented implicitly`

```
There is no explicit declaration of intent,
no "implements" keyword.
```

- Implicit interface `decouple` the `definition` of an interface from its `implementation`, which could then appear in any package without prearrangement(預先安排).

```go
// 實作方法
func (v *Vertex) X() float64{
    return v.x
}

func (v *Vertex) Y() float64{
    return v.y
}

func (v *Vertex) SetX(x float64) {
    v.x = x
}

func (v *Vertex) SeYX(y float64) {
    v.y = y
}

func (v *Vertex) Abs() float64{
    return math.Sqrt(v.x*v.x + v.y*v.y)
}
```

```go
func main() {
    var p IPoint = &Point{3, 4}
    ...
}
```

### Interface values

An `interface values` consist of a tuple of `value` and `concrete type`.

```
(value, type)
```

在`fmt.Printf`裡，我們可以用`%v`印出`value`以及使用`T`印出`type`

```go
fmt.Printf("(%v, %T)\n", p, p) // (&{3 4}, *main.Point)
```

### The empty interface

The interface type that specifies zero methods is known as the `empty interface`

```go
interface{}
```

- An empty interface may hold values of `any type`.

    Are used by code that `handles values of unknown type`.

    - Exmaple:

        [fmt.Print](https://golang.org/pkg/fmt/#Print) takes any number of arguments of type `interface{}`.

```go
func describw(i interface{}) {
    fmt.Printf("(%v, %T)\n", i, i)
}
```

#### Type assertions

A `type assertion` provide access to an interface value's `underlying` concrete value`.

有兩種形式:

```go
t := i.(T) // T is type that you want to access
```

- if `i` does not hold a `T`:

    The statement will trigger a `panic`.


```go
t, ok := i.(T)
```

- if `i` holds a `T`:

    return `underlying value`, `true`

- if `i` does not hold a `T`:

    return `zero`, `false (no panic)`

#### Type switches

```go
switch v := i.(type) {
    case T:
        // here v has type T
    case S:
        // here v has type S
    default:
        // no match; here v hase type the same type as i
}
```

##### Example

```go
func do(i interface{}) {
    switch v := i.(type) {
        case int:
            fmt.Printf("Twice %v is %v\n", v, v*2)
        case string:
            fmt.Println("%q is %v bytes long\n", v, len(v))
        default:
            fmt.Println("I don't know about type %T\n", v)
    }
}
```

