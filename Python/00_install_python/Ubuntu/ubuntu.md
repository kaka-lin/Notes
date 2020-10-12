---
title: "[Python] Ch0: Install Python: Ubuntu"
date: 2020-05-23
series: [Python]
categories: [Python]
---

## 1. Install request package

```bash
$ sudo apt-get update && apt-get upgrade
$ sudo apt-get install wget vim
```

## 2. Install Python3

[Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)

### 2-1. Download installer

```bash
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

![](img/conda-download.png)
![](/images/python/00_install_python/ubuntu/conda-download.png)


### 2-2. Change the access permissions of files

```
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
```

![](img/permissions-of-files.png)
![](/images/python/00_install_python/ubuntu/permissions-of-files.png)

### 2-3. Install

```bash
# install miniconda in ~/opt
$ mkdir -p ~/opt
$ bash Miniconda3-latest-Linux-x86_64.sh
```

![](img/conda-install-1.png)
![](/images/python/00_install_python/ubuntu/conda-install-1.png)

![](img/conda-install-2.png)
![](/images/python/00_install_python/ubuntu/conda-install-2.png)

![](img/conda-install-3.png)
![](/images/python/00_install_python/ubuntu/conda-install-3.png)

### 2-4. Activate conda

#### 1. bash

* Copy `conda initialize` in `~/.bash_profile` to `~/.bashrc`, as below:

![](img/conda-initialize-bash.png)
![](/images/python/00_install_python/ubuntu/conda-initialize-bash.png)

* Activate

```bash
$ source ~/.bashrc # or open new Terminal
```

![](img/conda-activate.png)
![](/images/python/00_install_python/ubuntu/conda-activate.png)

![](img/confirm.png)
![](/images/python/00_install_python/ubuntu/confirm.png)
