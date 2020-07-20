# Go Data Structure: `Maps`

- [Go Data Structure: `Maps`](#go-data-structure-maps)
  - [Creating a `Maps`](#creating-a-maps)
    - [Method 1: like array](#method-1-like-array)
    - [Method 2: use `make()`](#method-2-use-make)
  - [Maps initialize](#maps-initialize)
  - [Mutating Maps](#mutating-maps)
    - [`Insert` or `Update`](#insert-or-update)
    - [`Detele`](#detele)
    - [Check if the key is exist](#check-if-the-key-is-exist)
  - [Exercise: Maps](#exercise-maps)

A map maps key to value.

Golang provides map data structure which implements `hashtable`.

## Creating a `Maps`

The zero value of a map is `nil`. A `nil` map has no keys, `nor can keys be added`.

### Method 1: like array

```go
// nil map
var m map[keyTpye]valueType
```

- Note: 
  
  如果使用此方法來create `map`，還需要使用`make()`來初始化此`map`，否則無法存放`key-value`.

### Method 2: use `make()`

The `make` function returns a map od the given type, initialized and ready for use.

```go
m := make(map[keyTpye]valueType)

// or

// Define a map
var m map[keyTpye]valueType
// Using make function to initiate map
m = make(map[keyTpye]valueType)
```

## Maps initialize

Map literals are like struct literals, but the keys are required.

```go
var m = map[keyType]valueType {
    key1: value1,
    key2: value2,
}
```

## Mutating Maps

### `Insert` or `Update` 

Insert or update an element in map m

```go
m[key] = value
```

### `Detele`

Delete an element

```go
delete(m, key)
```

### Check if the key is exist

Test that a key is present with a two-value assignment:

```go
v, ok := m[key]
```

- If `key` is `in` map, `ok` is true. If not, `ok` is `false`.
- If `key` is `not in` map, then `v` is `zero value` for the map's element type.

## Exercise: Maps

Implement `WordCount`. It should return a map of the counts of each “word” in the string `s`. The `wc.Test` function runs a test suite against the provided function and prints success or failure.

```go
func WordCount(s string) map[string]int {
    m := make(map[string]int)
    //a := strings.Split(s, " ")
    a := string.Fields(s)
	
	for _, c := range a {
		m[c]++
	}

	return m
}
```
