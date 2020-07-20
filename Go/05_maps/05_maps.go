package main

import (
	"fmt"
	"strings"

	"golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {
	m := make(map[string]int)
	//a := strings.Split(s, " ")
	a := strings.Fields(s)

	for _, c := range a {
		m[c]++
	}

	return m
}

func main() {
	// Define a map
	var m map[string]int

	// using `make()` to initiate map
	m = make(map[string]int)
	m["age"] = 28
	fmt.Println(m["age"])

	// Define a map with an initial value
	var m1 = map[string]int{
		"age":    28,
		"height": 175,
	}
	fmt.Println(m1)

	wc.Test(WordCount)
}
