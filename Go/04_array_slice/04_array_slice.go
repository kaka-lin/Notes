package main

import (
	"fmt"
	"strings"

	"golang.org/x/tour/pic"
)

func printSlices(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func Pic(dx, dy int) [][]uint8 {
	image := make([][]uint8, dy)
	for i := range image {
		image[i] = make([]uint8, dx)
		for j := range image[i] {
			image[i][j] = uint8((i + j) / 2)
		}
	}

	return image
}

func main() {
	// Creating an Array
	var a [10]int
	fmt.Println(a)

	// Array initialize
	//a := [6]int{1, 2, 3, 4, 5, 6}
	a1 := []int{1, 2, 3, 4, 5, 6}
	fmt.Println(a1) // [1 2 3 4 5 6]

	// Creating a Slice
	var s []int
	printSlices(s) // nil
	fmt.Println(s == nil)

	s1 := make([]int, 5)     // lenght == capacity
	s2 := make([]int, 5, 10) // lenght: 5, capacity: 10
	printSlices(s1)
	printSlices(s2)

	s3 := a1[1:4]
	printSlices(s3) // [2 3 4]

	// Slices are like references to arrays
	s3[1] = 10
	printSlices(s3) // [2 10 4]
	printSlices(a1) // [1 2 10 4 5 6]

	// Slice length and capacity
	s4 := []int{2, 3, 5, 7, 11, 13}
	printSlices(s4)

	// 1. Slice the slice to give it zero length
	s41 := s4[:0]
	printSlices(s41)

	// 2. Extend its length
	s42 := s41[:4]
	printSlices(s42)

	// 3. Drop its first two values
	s43 := s42[2:]
	printSlices(s43)

	// Slices of slices
	// 1. 3x3 Array
	matrix := [][]int{
		make([]int, 3),
		make([]int, 3),
		make([]int, 3),
	}

	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			fmt.Printf("%d ", matrix[i][j])
		}
		fmt.Println()
	}

	// 2. tic-tac-toe boart(井字遊戲)
	board := [][]string{
		[]string{"-", "-", "-"},
		[]string{"-", "-", "-"},
		[]string{"-", "-", "-"},
	}

	board[0][0] = "X"
	board[1][0] = "O"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}

	// append function
	var s5 []int
	printSlices(s5)

	// append works on nil slices
	s5 = append(s5, 0)
	printSlices(s5)

	// The slice grows as needed
	s5 = append(s5, 1)
	printSlices(s5)

	var a2 = []int{1, 2, 3, 4, 5}

	for i, v := range a2 {
		fmt.Printf("a[%d]: %d\n", i, v)
	}

	// copy function
	s6 := []int{1, 2, 3}
	s7 := make([]int, 2)
	copied_size := copy(s7, s6)
	printSlices(s6)                 // [1 2 3]
	printSlices(s7)                 // [1 2]
	fmt.Printf("%d\n", copied_size) // 2

	// Exercise: Slices
	pic.Show(Pic)
}
