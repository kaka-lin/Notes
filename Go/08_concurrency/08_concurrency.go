package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

// range and close
func fibonacci(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

// select
func fibonacci2(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func main() {
	// single thread
	fmt.Println("===== Single thread =====")
	say("world")
	say("hello")

	// multi thread: use goroutine
	fmt.Println("===== Multi thread: use goroutine =====")
	go say("world")
	say("hello")

	// channels
	ch := make(chan int)
	//ch <- 1
	//fmt.Println(<-ch)

	// Sender (寫入)
	go func() {
		ch <- 1
	}()

	// Receiver (讀取)
	val := <-ch
	fmt.Println(val)

	ch2 := make(chan int, 1)
	ch2 <- 2
	fmt.Println(<-ch2)

	// Channel: range and close
	c3 := make(chan int, 10)
	go fibonacci(cap(c3), c3)
	for i := range c3 {
		fmt.Println(i)
	}
	fmt.Println(<-c3) // 0

	// Select
	c4 := make(chan int)
	quit := make(chan int)

	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-c4)
		}
		quit <- 0
	}()
	fibonacci2(c4, quit)

	tick := time.Tick(100 * time.Millisecond)
	boom := time.After(500 * time.Millisecond)

	for {
		select {
		case <-tick:
			fmt.Println("tick.")
		case <-boom:
			fmt.Println("BOOM!")
			return
		default:
			fmt.Println("    .")
			time.Sleep(50 * time.Millisecond)
		}
	}
}
