---
title: "[Go] Ch1: Go Basics - 08 Concurrency"
date: 2020-08-26
series: [Go]
categories: [Go]
---

# Concurrency

Go provides concurrency features as part of the core language.

This module goes over `goroutines` and `channels`,
and how they are used to implement different concurrency patterns.

複習: [Concurrency and Parallelism](https://kaka-lin.github.io/2020/07/concurrency_parallelism/)

## Goroutines

A `goroutine` is a `lightweight thread` managed by Go runtime.

```
goroutine是輕量級的執行緒(lightweight thread)，
可以想像建立 goroutine 就是建立了一個新的Thread
```

```
Thread是屬於OS的。而Goroutine是屬於Go runtime的
```

### Creating a Goroutine

```go
go f(x, y, z)
```

### Example

```go
func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}
```

#### 1. Single Thread

```go
func main() {
    // single thread
    fmt.Println("===== Single thread =====")
    say("world")
    say("hello")
}
```

Output:

```bash
===== Single thread =====
world
world
world
world
world
hello
hello
hello
hello
hello
```

#### 2. Goroutine: Multi Thread

```go
func main() {
	// multi thread: use goroutine
	fmt.Println("===== Multi thread: use goroutine =====")
	go say("world")
	say("hello")
}
```

Output:

```bash
===== Multi thread: use goroutine =====
world
hello
hello
world
hello
world
hello
world
world
hello
```

## Channels

Channels are a typed conduit through which you can `send` and `receive` values with the channel operator, `<-`

```go
ch <- v   // Send v to channel ch.
v := <-ch // Receive from ch,
          // and assign value to v
```

### Creating a Channels

Like maps and slices, channels must be created before use:

```go
ch := make(chan val_type)

// buffered channels
ch := make(chan val_type, capacity)
```

- `capacity`:

    容量(capacity)代表Channel可容納的元素的量，代表Channel的`Buffer大小`。

### Channels: Blocking

`By default` or `capacity is 0`, sends and receives block until the other side is ready.

Sends to a buffered channel block only when
the buffer is full

```
Channel有Sender(寫入)和Receiver(讀取)。

如果Channel沒有設capacity或者capacity為0，
說明Channel沒有Buffer，此時只有當Sender和Receiver都ready時，訊息才會傳遞成功(Blocking)。

如果有設計Buffer，就不會Blocking，只有當Buffer滿的時候
才會發生Blocking。
```

This allows goroutines to synchronize without explicit locks ot condition variables.

#### Example 1: would cause dead-lock

當執行到`ch <- 1`時，Sender會進入ready狀態，
然後就停住了，所以code不會執行到`fmt.Println(<-ch)`

```go
func main() {
    ch := make(chan int)
	ch <- 1
	fmt.Println(<-ch)
}
```

Output:

```bash
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send]:
main.main()
        /Users/kakalin/Projects/Notes/Go/08_concurrency/08_concurrency.go:28 +0x1a3
exit status 2
```

#### Solutions of Example 1

解法1: 建立`goroutine`去跑Sender/Receiver

```go
func main() {
    ch := make(chan int)

    // Sender (寫入)
    go func() {
        ch <- 1
    }()

    // Receiver (讀取)
	val := <-ch
	fmt.Println(val)
}
```

解法2: `Buffered Channels`

```go
func main() {
    ch := make(chan int, 1)
    ch <- 1
	fmt.Println(<-ch)
}
```

### Range and Close

就像 `Map` or `Array`，Channel可以通過`for ... range`來取得channel中的值，他會一直迭代直到channel被`close`。

若不用channel時，可用`close`將channel關閉。

- A sender can close a channel to indicate
that no more values will be sent.

- Receivers can test whether a channel has been closed by assigning a second parameter to the receive expression: after.

Note:

1. Only the sender should close a channel.

2. You don't usually need to close channels.
   Closing is only necessary when the receiver must
   be told there are no more values coming,
   such as to terminate a `range` loop.

```bash
channel關閉後:

Sender: 繼續send資料給他會導致`panic: send on closed channel`

Receiver: 可以繼續receive資料，且當超過send資料數量時，會讀取0值
```

```go
func fibonacci(n int, c chan int) {
    x, y := 0, 1
    for i := 0; i < n; i++ {
        c <- x
        x, y = y, x+y
    }
    close(c)
}

func main() {
    c := make(chan int, 10)
    go fibonacci(cap(c), c)
    for i := range c {
        fmt.Println(i)
    }
}
```

### Select

The `select` statement lets a goroutine wait on multiple communication operations.

A `select` blocks until one of its cases can run,
then it executes that case.
It chooses one at random if multiple are ready.

- Default Selection:

    The `default` case in a `select` is run if no other
    case is ready.

```
透過select，我們可以在多個channel中做選擇。
類似switch，但是但是只用來處理通訊操作(communication operations)。
```

#### Example 1

```go
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
    c := make(chan int)
    quit := make(chan int)

    go func() {
        for i := 0; i < 10; i++ {
            fmt.Println(<-c)
        }
        quit <- 0
    }()

    fibonacci2(c, quit)

}
```

Output:

```bash
0
1
1
2
3
5
8
13
21
34
quit
```

#### Example 2

```go
func main() {
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
```

Output:

```bash
    .
    .
tick.
    .
    .
tick.
    .
    .
tick.
    .
    .
tick.
    .
    .
tick.
BOOM!
```
