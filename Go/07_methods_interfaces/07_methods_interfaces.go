package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// Pointer receivers
func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

// Methods on Non-struct types
type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

// Interface
type IPoint interface {
	X() float64
	Y() float64
	SetX(float64)
	SetY(float64)
	Abs() float64
}

type Point struct {
	x float64
	y float64
}

// 實作方法
func (p *Point) X() float64 {
	return p.x
}

func (p *Point) Y() float64 {
	return p.y
}

func (p *Point) SetX(x float64) {
	p.x = x
}

func (p *Point) SetY(y float64) {
	p.y = y
}

func (p *Point) Abs() float64 {
	return math.Sqrt(p.x*p.x + p.y*p.y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())

	f := MyFloat(-math.Sqrt2)
	fmt.Println(f.Abs())

	v.Scale(10)
	fmt.Println(v.Abs())

	// Interface
	var p IPoint = &Point{3, 4}
	describe(p)
	fmt.Println(p)
	p.SetX(5)
	p.SetY(12)
	fmt.Printf("x: %f, y:%f\n", p.X(), p.Y())
	fmt.Println(p.Abs())

	// Empty interface: Type assertions
	var i interface{} = "hello"

	s := i.(string)
	fmt.Println(s)

	s, ok := i.(string)
	fmt.Println(s, ok)

	f2, ok := i.(float64)
	fmt.Println(f2, ok)

	//f2 = i.(float64) // panic
	//fmt.Println(f2)

	// Type switch
	do(21)
	do("hello")
	do(true)
}

func describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}

// Type switch
func do(i interface{}) {
	switch v := i.(type) {
	case int:
		fmt.Printf("Twice %v is %v\n", v, v*2)
	case string:
		fmt.Printf("%q is %v bytes long\n", v, len(v))
	default:
		fmt.Printf("I don't know about type %T\n", v)
	}
}
