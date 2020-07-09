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
