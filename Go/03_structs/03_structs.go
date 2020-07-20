package main

import (
	"fmt"
)

type Vertex struct {
	X int
	Y int
}

var (
	v1 = Vertex{1, 2} // has type Vertex
	p1 = &v1          // has type *Vertex

	p2 = &Vertex{3, 4} // has type *Vertex

	r = Vertex{X: 1} // Y:0 is implicit
	s = Vertex{}     // X:0 and Y:0
)

func main() {
	p1.X = 1e3
	fmt.Println(v1, p1, p2, r, s)
}
