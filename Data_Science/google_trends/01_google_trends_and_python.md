---
title: "[DS] Google Trends 01: Operate with Python"
date: 2020-06-10
tags: [Data Science, Google Trends, Python]
categories: [Data Science]
---

# Get and Analysis the result of Google Trends with Python

[Google Trends (Google搜尋趨勢)](https://trends.google.com/trends/trendingsearches/daily?geo=US)
是由Google 提供的線上搜尋趨勢服務，可以簡單的看出最近哪些`關鍵字`是熱門的。
但大規模分析 `Google Trends` 是很麻煩不切實際的，且有時候連打開網頁都懶，
那麼我們如何才能有夠有效的使用`Google Trends`呢？

- [pytrends](https://github.com/GeneralMills/pytrends):
    
    Unofficial API for Google Trends
    
    ```
    Allows simple interface for automating downloading of reports from Google Trends. 
    Only good until Google changes their backend again :-P. When that happens feel free to contribute!
    ```
    
    這是一個非官方支援的API，允許從`Google Trends`下載資料（爬蟲）
   
## Install `pytrends` package

```python
!pip3 install pytrends
```

## Connect to Google

- [Pandas](https://pandas.pydata.org/):
    
    Python Data Analysis Library

```python
import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()
```

## Build Payload

設定我們想要搜尋的關鍵字、類別、時間區段、地區以及類型

```python
"""Create the payload for related queries, interest over time anf interest by region"""
TrendReq.build_payload(self, kw_list, cat=0, 
                       timeframe='today 5-y', geo='', gprop='')
```

- Parameters:
    - kw_list: 
        - keywords to get data for
        - Up to five terms in a list (最多五個)
    - timeframe: Date to start from
    - cat: Category to narrow resulta
    - geo: Two letter country abbreviation
    - gprop:  What Google property to filter to


```python
kw_list=['tea', 'coffe', 'coke', 'milk', 'water']

# timeframe=today 12-m': one year data
# geo='US': specifying location with U.S.
pytrend.build_payload(kw_list, timeframe='today 12-m', geo='TW')

# gprop=yputube: only want to see Youtube search trends
#pytrend.build_payload(kw_list, timeframe='today 12-m', geo='TW', gprop=youtube)

# cat=71: category
#pytrend.build_payload(kw_list, timeframe='today 12-m', geo='TW', gprop=youtube, cat=71)
```

## Request data (Get results)

- Interest Over Time
- Historical Hourly Interest
- Interest by REgion
- Related Topics
- Related Queries
- Trending Searches
- Top Charts
- Suggestions

### Interest Over Time

```python
"""Request data from Google's Interest Over Time section and return a dataframe"""
TrendReq.interest_over_time(self)
```

- Returns: pandas.Dataframe

```python
interest_over_time_df = pytrend.interest_over_time()
interest_over_time_df.head()
```

#### Plot the result

- [Matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)

Matplotlib 顯示中文請參考：

1. [Windows](https://kaka-lin.github.io/2020/06/matplotlib_chinese_windows/)
2. [Mac](https://kaka-lin.github.io/2020/06/matplotlib_chinese_mac/)
3. [Ubuntu](https://kaka-lin.github.io/2020/06/matplotlib_chinese_ubuntu/)

```python
#!pip3 install matplotlib seaborn
```

```python
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)
plt.style.use('fivethirtyeight')

# 中文
plt.rcParams['font.sans-serif'] = ['Noto Sans Mono CJK TC', 'sans-serif'] 
plt.rcParams['axes.unicode_minus'] = False

%matplotlib inline
```

##### Make plots of `DataFrame` using `Matplotlib`

- [plot lines](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.line.html):

    ```python
    DataFrame.plot.line(self, x=None, y=None, **kwargs)
    ```

```python
axes = interest_over_time_df.plot.line(
    figsize=(15,7),
    title='Interest Over Time')
axes.set_xlabel('Date')
axes.set_ylabel('Trends Index')
axes.tick_params(axis='both', which='major', labelsize=13)
```

![](images/google_trends_result_1.png)
![](/images/data_science/google_trends/google_trends_result_1.png)

### Google Keyword Suggestions

Return a list of additional suggested keywords that can be used to refine a trend search.

```python
"""Request data from Google's Keyword Suggestions dropdown and return a dictionary"""
TrendReq.suggestions(self, keyword)
```

- Parameters:
    - `keyword`:
        - keyword to get suggestions for

```python
keywords = pytrend.suggestions(keyword='beer')
keywords_df = pd.DataFrame(keywords)
keywords_df.drop(columns='mid') # This column makes no sense
```

### Related Queries

當使用者搜尋某個主題時，他們也會搜尋相關的內容

Return data for the related keywords to a provided keyword shown on Google Trends' Related Queries section.

```python
"""Request data from Google's Related Queries section and reutrn a dictionary of dataframe

If not top and/or rising related queries are found, 
the value for the key "top" and/or "rising" will be None
"""
TrendReq.related_queries(self)
```

- Returns: dictionary of pandas.DataFrames


```python
pytrend.build_payload(kw_list=['Coronavirus'])
```

```python
# Related Queries, return a dictionary of dataframe
related_queries = pytrend.related_queries()
related_queries
```

    {'Coronavirus': {'top':                             query  value
      0              taiwan coronavirus    100
      1                          taiwan     94
      2              coronavirus update     64
      3               coronavirus cases     52
      4                  coronavirus 中文     37
      5   thank you coronavirus helpers     33
      6                coronavirus news     31
      7                          corona     28
      8                  coronavirus us     27
      9                 coronavirus map     26
      10                          武漢 肺炎     26
      11              china coronavirus     24
      12               coronavirus tips     21
      13              world coronavirus     20
      14               coronavirus live     17
      15                coronavirus usa     17
      16                             疫情     15
      17                new coronavirus     15
      18          coronavirus in taiwan     14
      19              wuhan coronavirus     14
      20        coronavirus worldometer     13
      21       taiwan coronavirus cases     13
      22              italy coronavirus     13
      23           coronavirus symptoms     13
      24                   corona virus     13,
      'rising':                             query   value
      0              taiwan coronavirus  806850
      1                          taiwan  760150
      2              coronavirus update  520350
      3               coronavirus cases  421850
      4   thank you coronavirus helpers  264250
      5                  coronavirus us  217300
      6                 coronavirus map  210350
      7                           武漢 肺炎  207400
      8               china coronavirus  190500
      9                coronavirus tips  167400
      10              world coronavirus  161150
      11                coronavirus usa  135500
      12                             疫情  121000
      13          coronavirus in taiwan  113550
      14              wuhan coronavirus  111450
      15        coronavirus worldometer  107600
      16       taiwan coronavirus cases  105500
      17              italy coronavirus  104450
      18              coronavirus italy  100450
      19        taiwan news coronavirus   96200
      20                who coronavirus   95600
      21                          covid   94100
      22                    taiwan news   91750
      23                            who   87750
      24                 coronavirus uk   87600}}


```python
COVID_19 = related_queries['Coronavirus']['top']
COVID_19
```

```python
axes = COVID_19.plot.barh(x='query', y='value', figsize=(10,15))
```

![](images/google_trends_result_2.png)
![](/images/data_science/google_trends/google_trends_result_2.png)

## The Search Trends of COVID-19 in 2020

```python
pytrend.build_payload(kw_list=['Coronavirus'], timeframe='2020-01-01 2020-06-04')
covid_19_interest_over_time_df = pytrend.interest_over_time()
covid_19_interest_over_time_df.head()
```

```python
axes = covid_19_interest_over_time_df.plot.line(
    figsize=(20,5),
    title='The Search Trends of COVID-19 in 2020')
axes.set_yticks([0, 25, 50, 75, 100])
axes.set_xlabel('Date')
axes.set_ylabel('Trends Index')
axes.tick_params(axis='both', which='major', labelsize=13)
```

![](images/google_trends_result_3.png)
![](/images/data_science/google_trends/google_trends_result_3.png)
