# Python MultiProcessing - Shared Memory

> `在 3.8 版被加入.`

> 該模組提供了一個 SharedMemory 類別，用於分配和管理被多核心或對稱多處理器 (symmetric multiprocessor, SMP) 機器上的一個或多個行程存取的共享記憶體。為了協助共享記憶體的生命週期管理，特別是跨不同行程的管理，multiprocessing.managers 模組中還提供了一個 BaseManager 子類別 SharedMemoryManager。
>
> 在此模組中，共享記憶體是指「POSIX 風格」的共享記憶體區塊（儘管不一定如此明確實作），而不是指「分散式共享記憶體 (distributed shared memory)」。這種型別的共享記憶體允許不同的行程潛在地讀取和寫入揮發性記憶體 (volatile memory) 的公開（或共享）區域。通常行程只能存取自己的行程記憶體空間，但共享記憶體允許在行程之間共享資料，從而避免需要跨行程傳遞資料的情境。與透過硬碟或 socket 或其他需要序列化/還原序列化 (serialization/deserialization) 和複製資料的通訊方式以共享資料相比，直接透過記憶體共享資料可以提供顯著的性能優勢。

[multiprocessing.shared_memory](https://docs.python.org/zh-tw/3.13/library/multiprocessing.shared_memory.html) 模組提供了在不同行程 (process) 間共享記憶體區塊的能力。常見應用場景是在多行程中高效地讀寫大型陣列（例如 NumPy 陣列），避免反覆拷貝資料。

主要 Componet:

- `SharedMemory`: 代表一塊共享記憶體區塊，可手動建立（create=True）或附加到已存在的同名區塊。
- `ShareableList`: 基於 `SharedMemory`，提供類似 Python list 的介面，內部自動序列化支援 int、float、bytes 及字串。
- `SharedMemoryManager`: 一個 `multiprocessing.managers.BaseManager` 的子類別，用於管理跨行程的共享記憶體生命週期。

## multiprocessing.shared_memory.SharedMemory(name=None, create=False, size=0)

- `name` (str | None, default: `None`)
  - 共享記憶體區塊的唯一名稱。
  - 如果 `name` 為 `None`，則會產生一個新的唯一名稱。
- `create` (bool, default: `False`)
  - `True`: 建立一個新的共享記憶體區塊。如果同名的區塊已存在，會引發 `FileExistsError`。
  - `False`: 附加到一個已存在的共享記憶體區塊。如果同名的區塊不存在，會引發 `FileNotFoundError`。
- `size` (int, default: `0`)
  - 當 `create=True` 時，指定共享記憶體區塊的大小（以位元組為單位）。
    - 如果 `create=True` 且 `size=0`，會引發 `ValueError`。
  - 如果 `create=False`，`size` 會被忽略，因為區塊大小由已存在的區塊決定。

**屬性 (Attributes):**

- `buf`: memoryview
  - 共享記憶體區塊內容的記憶體視圖 (memoryview)。
- `name`: str
  - 對共享記憶體區塊之唯一名稱的唯讀存取。
- `size`: int
  - 對共享記憶體區塊大小（以位元組為單位）的唯讀存取。

**方法 (Methods):**

- `close()`
  - 關閉對共享記憶體的存取。所有行程都必須呼叫 `close()`，共享記憶體才會被銷毀。
- `unlink()`
  - 請求銷毀共享記憶體區塊。為了確保資源清理，應在不再需要共享記憶體區塊時，由某個行程（通常是建立者）呼叫此方法。

## multiprocessing.shared_memory.ShareableList(sequence=None, *, name=None)

> 提供一個類似 list 的可變物件，其中儲存的所有值都儲存在共享記憶體區塊中。這將可儲存值限制為以下內建資料型別：
>
>   - int （有符號 64 位元）
>   - float
>   - bool
>   - str （編碼為 UTF-8 時每個小於 10M 位元組）
>   - bytes （每個小於 10M 位元組）
>   - None
>
> 它也與內建 list 型別明顯不同，因為這些 list 不能更改其總長度（即沒有 append()、insert() 等）並且不支援通過切片動態建立新的 ShareableList 實例。
>
> `ShareableList` 物件可透過索引存取 (indexing) 和切片 (slicing) 進行存取，就像內建的 `list` 一樣。然而，它們不支援透過切片來建立新的 `ShareableList` 實例。
>
> `del` 可用於單一索引（例如 `del sl[i]`）和切片（例如 `del sl[i:j]`）。然而，與內建 `list` 不同，`del` 不會改變列表的長度。它會將指定的項目或切片中的項目設定為 `None`，即該槽位的預設值。

- `sequence`:
  - 一個包含可支援型別（int, float, bool, str, bytes, None）的序列，用於初始化 `ShareableList`。
  - 如果提供 `sequence`，會自動建立一個新的共享記憶體區塊。
- `name`: str (optional)
  - 共享記憶體區塊的唯一名稱。
  - 如果提供 `name`，則會附加到一個已存在的 `ShareableList` 所使用的共享記憶體區塊。同時 `sequence` 設定為 `None`。

> 備註 `bytes` 和 `str` 值存在一個已知問題。如果它們以 `\x00` nul 位元組或字元結尾，那麼當透過索引從 `ShareableList` 中取得它們時，這些位元組或字元可能會被*默默地剝離 (silently stripped)*。這種 `.rstrip(b'\x00')` 行為被認為是一個錯誤，將來可能會消失。請參閱 [gh-106939](https://github.com/python/cpython/issues/106939)。

對於去除尾隨空值 (rstripping of trailing nulls) 會出問題的應用程式，變通解法 (workaround) 是始終無條件地在儲存時於此類值的末尾追加一個額外非 0 位元組，並在取得時也無條件地刪除它。

**屬性 (Attributes):**

- `format`
  - 唯讀屬性，包含所有目前有儲存的值所使用的 `struct` 打包格式。
- `shm`
  - 底層的 `SharedMemory` 實例。

**方法 (Methods):**

- `count(value)`
  - 回傳 `value` 在列表中出現的次數。
- `index(value)`
  - 回傳 `value` 在列表中首次出現的索引。如果 `value` 不存在，引發 `ValueError`。

## multiprocessing.managers.SharedMemoryManager

`multiprocessing.managers.BaseManager` 的一個子類別，可用於管理跨行程的共享記憶體區塊。

一旦透過 `start()` 啟動，`SharedMemoryManager` 物件的方法就可以用來建立和管理 `SharedMemory` 和 `ShareableList` 物件。

```python
from multiprocessing.managers import SharedMemoryManager

with SharedMemoryManager() as smm:
    sl = smm.ShareableList(range(4))
    # ... 在其他行程中使用 sl ...
```

**方法 (Methods):**

- `SharedMemory(size)`
  - 建立並回傳一個新的 `SharedMemory` 物件，大小為 `size` 位元組。
- `ShareableList(sequence)`
  - 建立並回傳一個新的 `ShareableList` 物件，由 `sequence` 的內容初始化。

當 `SharedMemoryManager` 實例被垃圾回收或其 `shutdown()` 方法被呼叫時，由它建立的所有共享記憶體區塊都會被釋放。
