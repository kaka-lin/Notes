---
title: "[Python] Ch2: Process Management
- 01 Python 多執行緒(Multi-Thread)"
date: 2020-07-18
series: [Python]
tags: [Multi-Thread]
categories: [Python, Asynchronous programming]
---

# 執行緒(Thread)

複習`作業系統(Operating System)`中的對於`執行緒(thread)`的解釋：

```
執行緒(thread)是OS能夠進行運算排程的最小單位，被包含在程序(Process)之中，是Process中的實際運算單位。
```

- 同一顆CPU執行
- 同一個Process下的Thread共享資源，如記憶體、全域變數等
- 一個執行緒被中斷會導致集體死亡

# Python 模組: [threading](https://docs.python.org/3/library/threading.html)

`threading`是Python的標準函式庫裡的模組，所以不需要另外安裝即可使用，雖然功能沒有很多，但已經足夠我們用來設計基本的多執行緒程式。

## 執行緒(Thread): `threading.Thread`

### Step 1. 建立子執行緒與執行

```python
class threading.Thread(
    group=None, target=None, name=None,
    args=(), kwargs={}, *, daemon=None)
```

- group: should be `None`; reserved for future extension when a ThreadGroup class is implemented.
- target: the callable object to be invoked by the `run()` method.
- name: the thread name.
- args: the argument tuple for the target invocation. Defaults to `()`.
- kwargs: a dictionary of keyword arguments for the target invocation. Defaults to `{}`.

### Step 2. 執行子執行緒

```python
Thread.start()
```

### Step 3. 等待子執行緒結束

```python
Thread.join(timeout=None)
```

    Wait until the thread terminates.
    When the timeout argument is present and not `None`, it should be a floating point number specifying a timeout for the operation in second

### Example

```python
import time
import threading

def job():
    for i in range(5):
        print("Child Thread: {}".format(i))
        time.sleep(1)

# 建立子執行緒
t = threading.Thread(target=job)
# 子執行緒開始執行
t.start()

# Main Thread繼續執行自己的工作
for i in range(3):
    print("Main thread: {}".format(i))
    time.sleep(1)

# 等待子執行緒執行結束
t.join()

print("All Done.")
```

[Output]

```
Child Thread: 0Main thread: 0

Child Thread: 1Main thread: 1

Child Thread: 2Main thread: 2

Child Thread: 3
Child Thread: 4
All Done.
```

這裡的主程式會在`join`的地方等待到`子執行緒t`結束後，才會繼續往下執行。

## 建立多個子執行緒與參數

```python
import time
import threading

def job2(num):
    print("Thread: {}".format(num))
    time.sleep(1)

# 建立5個子執行緒
threads = []
for i in range(5):
    threads.append(threading.Thread(target=job2, args=(i,)))
    # 執行剛剛建立的子執行緒
    threads[i].start()

# Main Thread繼續執行自己的工作
for i in range(3):
    print("Main thread: {}".format(i))
    time.sleep(1)

# 等待所有子執行緒執行結束
for i in range(5):
    threads[i].join()

print("All Done.")
```

[Output]

    Thread: 0
    Thread: 1
    Thread: 2
    Thread: 3
    Thread: 4
    Main thread: 0
    Main thread: 1
    Main thread: 2
    All Done.

## 物件導向 (Class)

將`Thread`變成一個`Class`，需要覆寫`run()`

```python
Thread.run()
```

Method representing the thread’s activity.

You may override this method in a subclass

#### Example

```python
import time
import threading
import random

class Counter(threading.Thread):
    def __init__(self, thread_name):
        super(Counter, self).__init__(name=thread_name)

    def run(self):
        '''重寫父類run方法，在執行緒啟動後執行該方法內的程式'''

        count = 0
        for i in range(1000):
            count = count + 1
        print("{}, count: {}".format(self.name, count))

# 建立5個子行緒
threads = []
for i in range(5):
    threads.append(Counter('thread_' + str(i)))
    threads[i].start()

# Main Thread繼續執行自己的工作
for i in range(3):
    print("Main thread: {}".format(i))
    time.sleep(1)

# 等待所有子執行緒執行結束
for i in range(5):
    threads[i].join()

print("All Done.")
```

[Output]

    thread_0, count: 1000
    thread_1, count: 1000
    thread_2, count: 1000
    thread_3, count: 1000thread_4, count: 1000

    Main thread: 0
    Main thread: 1
    Main thread: 2
    All Done.

## 鎖(Lock)

為了避免多個執行緒同時對同一個記憶體做存取（例如：將資料寫入同一個檔案），必須使用`Lock`將那個記憶體區段鎖起來，以確保一次只有一個執行緒可以去存取記憶體裡的資料。

我們可以使用`threading`模組裡的`Lock()`來處理。

```python
class threading.Lock()
```

利用`Thread.Lock()`來建構互斥鎖`(Mutex)`

### 1. 取得Lock

    ```python
    Lock.acquire(blocking=True, timeout=-1)
    ```

    Acquire a lock, `blocking` or `non-blocking`


### 2. 釋放Lock

    ```python
     Lock.release()
    ```

    Release a lock. This can be called from any thread, not only the thread which has acquired the lock.

### Example

#### 不使用 Lock

```python
import time
import threading
import random

count = 0

class Counter(threading.Thread):
    def __init__(self, thread_name):
        super(Counter, self).__init__(name=thread_name)

    def run(self):
        global count

        for i in range(1000):
            count += 1
        print("{}, count: {}".format(self.name, count))

# 建立5個子行緒
threads = []
for i in range(5):
    threads.append(Counter('thread_' + str(i)))
    threads[i].start()

# Main Thread繼續執行自己的工作
for i in range(3):
    print("Main thread: {}".format(i))
    time.sleep(1)

# 等待所有子執行緒執行結束
for i in range(5):
    threads[i].join()

print("Final Count: {}".format(count))
print("All Done.")
```

[Output]

    thread_0, count: 1000
    thread_1, count: 2000
    thread_2, count: 3000
    thread_3, count: 4000thread_4, count: 5000
    Main thread: 0

    Main thread: 1
    Main thread: 2
    Final Count: 5000
    All Done.

由上輸出可已看到，Output很亂。

#### 使用 Lock

```python
import time
import threading
import random

count = 0

class Counter(threading.Thread):
    def __init__(self, lock, thread_name):
        super(Counter, self).__init__(name=thread_name)
        self.lock = lock

    def run(self):
        global count

        # 取得 lock
        self.lock.acquire()
        print("Lock acquire by {}".format(self.name))

        for i in range(10000):
            count += 1

        # 不能讓多個執行續同時進行的工作
        print("{}, count: {}".format(self.name, count))
        time.sleep(1)

        # 釋放 lock
        print("Lock released by {}".format(self.name))
        self.lock.release()

# 建立 lock
lock = threading.Lock()

# 建立5個子行緒
threads = []
for i in range(5):
    threads.append(Counter(lock, 'thread_' + str(i)))
    threads[i].start()

# Main Thread繼續執行自己的工作
for i in range(3):
    print("Main thread: {}".format(i))
    time.sleep(1)

# 等待所有子執行緒執行結束
for i in range(5):
    threads[i].join()

print("Final Count: {}".format(count))
print("All Done.")
```

[Output]

    Lock acquire by thread_0
    thread_0, count: 10000
    Main thread: 0
    Lock released by thread_0
    Lock acquire by thread_1Main thread: 1

    thread_1, count: 20000
    Main thread: 2
    Lock released by thread_1
    Lock acquire by thread_2
    thread_2, count: 30000
    Lock released by thread_2
    Lock acquire by thread_3
    thread_3, count: 40000
    Lock released by thread_3
    Lock acquire by thread_4
    thread_4, count: 50000
    Lock released by thread_4
    Final Count: 50000
    All Done.

從結果可以看出，執行緒是一個接著一個執行

## 旗標(Semaphore)

```python
class threading.Semaphore([value])
```

因為系統資源有限，所以在處理某些耗資源的工作時，會允許有限的執行緒同時進行，跟鎖(Lock)類似
但是`Lock僅允許一次一個執行緒`，而`旗標(Semaphore)允許多個執行緒，但要限制同時執行的執行緒上限。`

`Semaphore`是進入與出去某個`Code block`的門鎖,
而這把門鎖會記錄多少個`Thread`進入到控制的`Code block`
以確保該`Code block`最多只能被`n`個`Thread`同時執行。

`Semaphore`物件上面只有兩個方法:
1. `acquire([blocking])`
2. `release()`

另外在取得`Semaphore`物件的時候你可以透過參數`value`指定`Code block`最多只能有多少個`Thread`同時進入該`Code block`(即是所謂的`Critical Section`).

可以簡單地把`Semaphore`想像為計數器：
- 當一個執行緒呼叫了`acquire()`時，旗標內部計數器就`減1`
- 當一個執行緒呼叫了`release()`時，旗標內部計數器就`加1`

```
當計數器為0時，之後的執行緒就要等待其他執行緒release後，才能繼續
```

### Example

```python
import threading
import time
import random

count = 0
lock = threading.Lock()
semphore = threading.Semaphore(2)

def code_block(thd, i):
    global count, lock

    lock.acquire()
    count += 1
    print("{} (+1), count: {}".format(thd.name, count))
    lock.release()

    time.sleep(random.randrange(2, 10))

    lock.acquire()
    count -= 1
    print("{} (-1), count: {}".format(thd.name, count))
    lock.release()

class Guest(threading.Thread):
    def __init__(self, semphore, thread_name):
        super(Guest, self).__init__(name=thread_name)

        self.semphore = semphore

    def run(self):
        # 取得旗標
        # acquire一次，semaphore就會減1，直到數量為0時，就會阻塞這在
        self.semphore.acquire()
        print("Semphore acquired by {}".format(self.name))

        # 僅允許有限個執行緒同時進的工作
        code_block(self, i)
        time.sleep(1)

        # 釋放旗標
        # release一次，semaphore就會加1
        print("Semphore released by {}".format(self.name))
        self.semphore.release()

# 建立3個子行緒
threads = []
for i in range(3):
    threads.append( Guest(semphore, 'thread_' + str(i)))
    threads[i].start()

# 等待所有子執行緒執行結束
for i in range(3):
    threads[i].join()

print("Final Count: {}".format(count)) # should be 0
print("All Done.")
```

[Output]

    Semphore acquired by thread_0Semphore acquired by thread_1

    thread_0 (+1), count: 1
    thread_1 (+1), count: 2
    thread_1 (-1), count: 1
    Semphore released by thread_1
    Semphore acquired by thread_2
    thread_2 (+1), count: 2
    thread_0 (-1), count: 1
    Semphore released by thread_0
    thread_2 (-1), count: 0
    Semphore released by thread_2
    Final Count: 0
    All Done.

## 事件(Event)

This is one of the simplest mechanisms for communication between threads: one thread signals an event and other threads wait for it.

```python
class threading.Event()
```

用於`Thread`之間的溝通，應用方式通常為ㄧ個`thread`發起一個`event`，然後其他`thread`會等待發出`event`的`thread`才開始做相信動作。

`Event`透過維護內部的`flag`符來實現`thread`之間的同步問題，
維護`flag`的狀態有三種方法(`wait`, `set`, `clear`)

1. `event.wait()`: 使執行緒組塞，直到flag值為`True`，初始值為`Flase`
2. `event.set()`: 通知相對應的執行緒作相應動作，將flag值設為`True`
3. `envet.clear()`: 做完相對應動作後，再次等待下次通知，將flag值設為`False`

### Example 1

```python
import time
import threading

class TestThread(threading.Thread):
    def __init__(self, name, event):
        super(TestThread, self).__init__()

        self.name = name
        self.event = event

    def run(self):
        print("\tThread: {} wait!".format(self.name))
        self.event.wait()
        print("\tThread: {} start!".format(self.name))

def run():
    event = threading.Event()

    threads = []
    for i in range(1, 5):
        threads.append(TestThread(str(i), event))

    print("Main thread start!")

    for thread in threads:
        thread.start()

    print("\n--------------------")
    print("Sleep 3 seconds!")
    time.sleep(3)

    print("Now awake other threads !")
    event.set()

run()
```

[Output]

    Main thread start!
    	Thread: 1 wait!
    	Thread: 2 wait!
    	Thread: 3 wait!
    	Thread: 4 wait!

    --------------------
    Sleep 3 seconds!
    Now awake other threads !
    	Thread: 2 start!	Thread: 4 start!
    	Thread: 3 start!
    	Thread: 1 start!


#### Example 2: 十字路口

```python
import time
import random
import threading

class VehicleThread(threading.Thread):
    ''' Class representing a motor vehicle at an intersection '''

    def __init__(self, thread_name, event):
        super(VehicleThread, self).__init__(name=thread_name)

        self.event = event

    def run(self):
        ''' Vehicle waits unless/until light is green '''

        # Staggered arrival times
        time.sleep(random.randrange(1, 10))

        # prints arrival time of car at intersection
        print("{} arrived {}".format(
            self.getName(),
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

        # wait for green light
        self.event.wait()

        # displays time that car departs intersection
        print("{} passes through the intersection at {}".format(
            self.getName(),
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def run():
    green_light = threading.Event()

    # creates and starts ten vehicle threads
    vehicle_threads = []
    for i in range(1, 11):
        vehicle_threads.append(VehicleThread('Vehicle ' + str(i), green_light))

    print("----------------- Start: {}".format(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    for vehicle in vehicle_threads:
        vehicle.start()

    # Run in jupyter notebook, default thread is: 5
    while threading.active_count() > 5:
        # sets the Event's flag to false -- block all incoming vehicles
        green_light.clear()
        print("RED LIGHT! at: {}".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

        time.sleep(3)
        print("----------------- 3 second -----------------")

        # sets the Event's flag to true -- awake all waiting vehicles
        green_light.set()
        time.sleep(1)

    print("----------------- End: {}".format(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

run()
```

[Output]

    ----------------- Start: 2020-07-15 17:51:40
    RED LIGHT! at: 2020-07-15 17:51:40
    Vehicle 1 arrived 2020-07-15 17:51:41
    Vehicle 4 arrived 2020-07-15 17:51:41
    Vehicle 2 arrived 2020-07-15 17:51:42Vehicle 5 arrived 2020-07-15 17:51:42Vehicle 7 arrived 2020-07-15 17:51:42


    ----------------- 3 second -----------------
    Vehicle 4 passes through the intersection at 2020-07-15 17:51:43Vehicle 5 passes through the intersection at 2020-07-15 17:51:43Vehicle 7 passes through the intersection at 2020-07-15 17:51:43Vehicle 2 passes through the intersection at 2020-07-15 17:51:43Vehicle 1 passes through the intersection at 2020-07-15 17:51:43




    RED LIGHT! at: 2020-07-15 17:51:44
    Vehicle 3 arrived 2020-07-15 17:51:46
    Vehicle 10 arrived 2020-07-15 17:51:46
    Vehicle 8 arrived 2020-07-15 17:51:47
    ----------------- 3 second -----------------
    Vehicle 10 passes through the intersection at 2020-07-15 17:51:47Vehicle 8 passes through the intersection at 2020-07-15 17:51:47Vehicle 3 passes through the intersection at 2020-07-15 17:51:47


    Vehicle 6 arrived 2020-07-15 17:51:48Vehicle 9 arrived 2020-07-15 17:51:48
    Vehicle 9 passes through the intersection at 2020-07-15 17:51:48

    Vehicle 6 passes through the intersection at 2020-07-15 17:51:48
    ----------------- End: 2020-07-15 17:51:48


## 條件變數(Condition)

當執行緒需要滿足某些條件才能繼續執行時，可以使用`threading`模組裡的`Lock()`來處理。

```python
class threading.Condition(lock=None)
```

- lock: Optional, default is `RLock`.

`threading.Condition`提供了三種方法，來進行`thread`之間的溝通

1. `wait()`: 條件不滿足時，執行緒會釋放並進入阻塞等待
2. `notify(n=1)`: 條件滿足後，喚醒一個在等待池裡的執行緒
3. `notifyAll()`: 條件滿足後，喚醒所有在等待池裡的執行緒

### Example：捉迷藏遊戲

1. 遊戲開始後，Seeker先把自己眼睛矇上，蒙上眼後就通知Hider
2. Hider接收到通知後，開始找地方將自己藏起來，再通知Seeker可以開始找了
3. Seeker接到通知後，就開始找hider


```python
import threading
import time

class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()

        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)  # 確保先運行Seeker中的方法

        self.cond.acquire()  # b
        print('To {}: 我已經把眼睛蒙上了'.format(self.name))
        print('\t[Info] {} notify()...'.format(self.name))
        self.cond.notify()
        print('\t[Info] {} wait()...'.format(self.name))
        self.cond.wait()  # c

        print('To {}: 我找到你了！！！'.format(self.name))
        print('\t[Info] {} notify()...'.format(self.name))
        self.cond.notify()
        print('\t[Info] {} release()...'.format(self.name))
        self.cond.release()

        print('To {}: 我贏了'.format(self.name))

class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()

        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        print('\t[Info] {} wait()...'.format(self.name))
        self.cond.wait()

        print('To {}: 我已經藏好了，你快來找我吧！！！'.format(self.name))
        print('\t[Info] {} notify()...'.format(self.name))
        self.cond.notify()
        print('\t[Info] {} wait()...'.format(self.name))
        self.cond.wait()

        print('\t[Info] {} release()...'.format(self.name))
        self.cond.release()

        print('To {}: 被你找到了，我輸了！'.format(self.name))

if __name__ == '__main__':
    cond = threading.Condition()
    seeker = Seeker(cond, 'seeker')
    hider = Hider(cond, 'hider')
    seeker.start()
    hider.start()
```

[Output]

    	[Info] seeker wait()...
    To hider: 我已經把眼睛蒙上了
    	[Info] hider notify()...
    	[Info] hider wait()...
    To seeker: 我已經藏好了，你快來找我吧！！！
    	[Info] seeker notify()...
    	[Info] seeker wait()...
    To hider: 我找到你了！！！
    	[Info] hider notify()...
    	[Info] hider release()...
    To hider: 我贏了
    	[Info] seeker release()...
    To seeker: 被你找到了，我輸了！
