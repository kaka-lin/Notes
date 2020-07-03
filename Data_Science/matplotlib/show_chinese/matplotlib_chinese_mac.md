---
title: "[DS] Matplotlib show Chinese: Mac"
date: 2020-06-10
tags: [Data Science, matplotlib, python]
categories: [Data Science, matplotlib]
---

# Matplotlib 顯示中文

Ref: [Text with non-latin glyphs](https://matplotlib.org/3.1.0/tutorials/text/text_props.html#text-with-non-latin-glyphs)

下載思源體 - [source-han-sans](https://github.com/adobe-fonts/source-han-sans)

1. [思源黑體](https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKtc-hinted.zip)
    本教學使用此字型
2. [思源宋體](https://noto-website-2.storage.googleapis.com/pkgs/NotoSerifCJKtc-hinted.zip)

```python
# 查看安裝了哪些字型
# windows請忽略這段
# unix系統可以使用下command確認是否安裝成功
!fc-list :lang=zh family
```

```python
# 重新加載字體
from matplotlib.font_manager import _rebuild
_rebuild()
```

```python
import matplotlib 
import matplotlib.pyplot as plt

# 使用剛剛下載的思源體字型
plt.rcParams['font.sans-serif'] = ['Noto Sans Mono CJK TC', 'sans-serif'] 
plt.rcParams['axes.unicode_minus'] = False

%matplotlib inline
```

# Plot the result 

```python
plt.figure()
plt.plot((1, 2, 3),(4, 3, -1))
plt.title("聲量圖")
plt.ylabel("文章數量")
plt.xlabel("品牌名稱") 
plt.show()
```

![](images/matplotlib_chinese_mac.png)
![](/images/data_science/matplotlib/matplotlib_chinese_mac.png)
