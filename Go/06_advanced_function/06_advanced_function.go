package main

import (
	"fmt"
	"math"
)

// Function as Arguments: Example 1
func print(fn func(int, int) int, a, b int) {
	fmt.Println(fn(a, b))
}

func area(a, b int) int {
	return a * b
}

func sum(a, b int) int {
	return a + b
}

// Function as Arguments: Example 2
func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

func hypot(x, y float64) float64 {
	return math.Sqrt(x*x + y*y)
}

// Anonymous Function as a return value
func printSum() func(int, int) {
	return func(x, y int) {
		fmt.Println(x + y)
	}
}

// Function closures
func intSeq() func() int {
	i := 0
	return func() int {
		i += 1
		return i
	}
}

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	// Function as Argument
	print(area, 3, 4)           // 12
	print(sum, 3, 4)            // 7
	fmt.Println(compute(hypot)) // 5

	// Anonymous Function
	fn := printSum()
	fn(3, 4)

	// Function closures
	nextInt := intSeq()
	fmt.Println(nextInt()) // 1
	fmt.Println(nextInt()) // 2
	fmt.Println(nextInt()) // 3

	fn2 := adder()
	for i := 0; i < 10; i++ {
		fmt.Println(fn2(i))
	}

}
