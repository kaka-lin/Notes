# Sorting Algorithm

在電腦科學所使用的排序演算法通常依以下標準分類：

- 計算的複雜度 (Computational Complexity)
  - `時間複雜度 (Time Complexity)`:

    有分成 [Best, worst and average case](https://en.wikipedia.org/wiki/Best,_worst_and_average_case)，依據 list 的大小而言，好的行為是 $O(nlogn)$，壞的行為是 $O(n^2)$。

  - `記憶體使用量 (Memory Usuage) or 空間複雜度 (Space Complexity)`
    - "in-place" algorithms: $O(1)$

- `穩定性 (Stability)`

    相同鍵值的資料，排序後順序和排序前一樣。

    Example:

    ```
    排序前： 2, 7(藍), 9, 3, 7(紅) ⇒ 藍7在紅7前面
    排序後： 2, 3, 7(藍), 7(紅), 9 ⇒ 藍7保持在紅7前面
    ```
- `適應性 (Adaptability)`

    輸入的預排序是否會影響運行時間，我們稱其為 `adaptive`。

    ```
    Whether or not the presortedness of the input affects the running time.
    ```

     > can early stop

    - 假設今天有一個 Array 已經差不多排好了，那麼它只需要花很少的力氣，就可以排好。

- 排序的方法
  - 比較式排序演算法 (Compare Sorting)
  - 非比較式排序演算法 (Non-Compare Sorting)

## 常用排序演算法整理

| Name | Best case | Average case | Worts case | Space Complexity | Stability | Other notes |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [選擇排序 (Selection Sort)](https://github.com/kaka-lin/Notes/tree/master/DSA/Sort/Selection%20Sort) | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | unstable | Stable with O(n) extra space, when using linked lists. |
| [插入排序 (Insertion Sort)](https://github.com/kaka-lin/Notes/tree/master/DSA/Sort/Insertion%20Sort) | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | stable | backwise implementation `adaptive`|
| [泡沫排序 (Bubble Sort)](https://github.com/kaka-lin/Notes/tree/master/DSA/Sort/Bubble%20Sort) | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | stable<br>`adaptive` | Exchanging (old tape days) |
| [堆積排序 (Heap Sort)](https://github.com/kaka-lin/Notes/tree/master/DSA/Sort/Heap%20Sort) | $O(nlogn)$ | $O(nlogn)$ | $O(nlogn)$ | $O(1)$ | unstable | usually preferred over selection (faster) |
| [合併排序 (Merge Sort)](https://github.com/kaka-lin/Notes/tree/master/DSA/Sort/Merge%20Sort) | $O(nlogn)$ | $O(nlogn)$ |$O(nlogn)$ | $O(n)$ | stable | parallelizable |
| [快速排序 (Quick Sort)](https://github.com/kaka-lin/Notes/tree/master/DSA/Sort/Quick%20Sort) | $O(nlogn)$ | $O(nlogn)$ | $O(n^2)$ | average $O(logn)$ <br> worst $O(n)$| unstable | Quicksort is usually done in-place with O(logn) stack space |
| Tree Sort | $O(nlogn)$ | $O(nlogn)$ | $O(n^2)$ | average $O(logn)$  <br> worst $O(n) |  | |
| Shell Sort | $O(nlogn)$ | $O(n^{4/3})$ | $O(n^{3/2})$ | $O(1)$ | unstable/adaptive | often faster than $O(n^2)$ |
| [桶排序 (Bucket Sort)](https://github.com/kaka-lin/Notes/tree/master/DSA/Sort/Bucket%20Sort) | - | $O(n)$ | $O(n^2)$ | $O(m)$ | - | Non-comparison sorts |

## Sorting Algorithm Visualize

- [15 Sorting Algorithms in 6 Minutes](https://www.youtube.com/watch?v=kPRA0W1kECg)
- [Visualgo](https://visualgo.net/en/sorting)

## Reference

- [wiki: Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [DSA 20200609: Sorting / Summary](https://www.youtube.com/watch?v=cxbabnqtWsk&feature=youtu.be)
