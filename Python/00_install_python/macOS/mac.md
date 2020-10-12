---
title: "[Python] Ch0: Install Python: Mac"
date: 2020-05-23
series: [Python]
categories: [Python]
---

## 1. Install Package Manager

- [Homebrew](https://brew.sh/)

    It is the ```package manager``` for macOS. Following the install step on the website to install it.

    ![](img/brew.png)
    ![](/images/python/00_install_python/mac/brew.png)

## 2. Install Python3

### 2-1. Homebrew

```bash
$ brew install python
```

### 2-2. [Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html)

#### 1. Download installer

```bash
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
```

#### 2. Install

```bash
# install miniconda in ~/opt
$ mkdir -p ~/opt
$ chmod +x Miniconda3-latest-MacOSX-x86_64.sh
$ bash Miniconda3-latest-MacOSX-x86_64.sh
```

![](img/conda-install-1.png)
![](/images/python/00_install_python/mac/conda-install-1.png)

![](img/conda-install-2.png)
![](/images/python/00_install_python/mac/conda-install-2.png)

![](img/conda-install-3.png)
![](/images/python/00_install_python/mac/conda-install-3.png)

#### 3. Activate conda

##### 1. bash

* Copy `conda initialize` in `~/.bash_profile` to `~/.bashrc`, as below:

![](img/conda-initialize-bash.png)
![](/images/python/00_install_python/mac/conda-initialize-bash.png)

*  Activate

```bash
$ source ~/.bashrc # or open new Terminal
```

![](img/conda-init-bash.png)
![](/images/python/00_install_python/mac/bash.png)

##### 2. zsh

* Copy `conda initialize` in `~/.bash_profile` to `~/.zshrc`, as below:

![](img/conda-initialize-zsh.png)
![](/images/python/00_install_python/mac/conda-initialize-zsh.png)

* Activate

```bash
$ source ~/.zshrc # or open new Terminal
```

![](img/conda-init-zsh.png)
![](/images/python/00_install_python/mac/conda-init-zsh.png)
