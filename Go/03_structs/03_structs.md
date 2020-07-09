# Go Data Structure: `Structs`

- [Go Data Structure: `Structs`](#go-data-structure-structs)
  - [Structs (Structures)](#structs-structures)
    - [Defining a struct](#defining-a-struct)
    - [Accessing Struct Fields (Members)](#accessing-struct-fields-members)
  - [Pointers to Structs](#pointers-to-structs)
    - [Pointer](#pointer)
  - [Pointers to Structs](#pointers-to-structs-1)
    - [Accessing the field of Struct Pointer](#accessing-the-field-of-struct-pointer)

## Structs (Structures)

A `struct or structure` is a collection of fields.

### Defining a struct

Using `struct` keyword to create a new structure type.

```go
type StructName struct {
    field1 fieldType1
    field2 fieldType2
    ...
}
```

Example:

```go
type Vertex struct {
    X int
    Y int
}
```

### Accessing Struct Fields (Members)

Struct fields are accessed using a `dot`.

```go
v := Vertrx{1, 2}
v.X = 4
fmt.Println(v.X) // 4
```

## Pointers to Structs

### Pointer

A `pointer` holds the memory address of a value.

The type `*T` is a pointer to a `T` value. Its zero value is `nil`.

```go
var *p int
```

The `&` operator generates a pointer to its operand.

```go
i := 42
p = &i
```

The `*` operator denotes the pointer's underlying value.

```go
fmt.Println(*p) // read i through the pointer p
*p = 21         // set i through the pointer p
```

This is known as `"dereferencing"` or `"indirecting"`.

- Unlike C, Go has `no pointer arithmetic (沒有指針運算)`.

## Pointers to Structs

Struct fields can be accessed through a struct pointer.

The syntax to create a pointer to a struct is as follows.

```go
s := StructType{...}
p := &s

// or
p := &StructType{...}
```

Example:

```go
v := Vertex{1, 2}
p := &v

q := &Vertex{3, 4}
```

### Accessing the field of Struct Pointer

To access the field `X` of a struct when we have the `struct pointer p`, we need to use `dereferencing syntax (*p)` to get the actual value of struct it is pointing to and use `(*p).X` to access `X` of that struct value.

However, that notation is cumbersome, so the language permits us instead to write just `p.X`, without the explicit dereference.

```go
v := Vertex{1, 2}
p := &v
p.X = 1e3
fmt.Println(v) // {1000, 2}
```
