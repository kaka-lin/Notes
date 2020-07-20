package main

import (
	"fmt"
	"math"
	"math/cmplx"
	"math/rand"
	"time"
)

// Functions
func add(x int, y int) int {
	return x + y
}

// Multiple results
func swap(x, y string) (string, string) {
	return y, x
}

// Named return values
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

// Variables
var i int // zero values

// Variable with initializers
var j, k int = 1, 2

// Basic types
var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

// Numeric Constants
const (
	// Create a huge number by shifting a 1 bit left 100 places.
	// In other words, the binary number that is 1 followed by 100 zeroes.
	Big = 1 << 100

	// Shift it right again 99 places, so we end up with 1<<1, or 2.
	Small = Big >> 99
)

func needInt(x int) int {
	return x*10 + 1
}

func needFloat(x float64) float64 {
	return x * 0.1
}

func main() {
	//fmt.Printf("Hello, world\n")
	fmt.Println("Hello, world")

	fmt.Println("The time is", time.Now())

	fmt.Println("My favorite number is", rand.Intn(10))

	fmt.Println(math.Pi)

	// Functions
	fmt.Println(add(42, 13))

	// Multiple results
	a, b := swap("hello", "world")
	fmt.Println(a, b)

	// Named return values
	fmt.Println(split(17))

	// Variable with initializers
	var c, python, java = true, false, "no!"
	// 在函式中， 明確賦值時 := 可以取代var
	// 但 := 不能在函數以外的地方使用
	m := 3
	fmt.Println(i, j, k, m, c, python, java)

	// Basics types
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	// or
	const myprint = "Type %T Value %v\n"
	fmt.Printf(myprint, MaxInt, MaxInt)
	fmt.Printf(myprint, z, z)

	// Type conversion
	var x, y int = 3, 4
	var f float64 = math.Sqrt(float64(x*x + y*y))
	var z uint = uint(f)
	fmt.Println(x, y, z)

	// Numeric constants
	fmt.Println(needInt(Small))
	fmt.Println(needFloat(Small))
	fmt.Println(needFloat(Big))
}
