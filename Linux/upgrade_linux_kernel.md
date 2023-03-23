# Upgrade the Ubuntu Linux kernel

因為 Ubuntu 18.04 的 Linux kernel 版本是 `4.15`， 如果你因各種需求需要升級 Linux kernel 時，可以依照以下步驟升級。

這邊以 Ubuntu 18.04 upgrade to `Linux kernel 4.19` 為例:

#### Step 1. Download the 4.19 kernel (for 64 bit system):

```sh
$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.19/linux-headers-4.19.0-041900_4.19.0-041900.201810221809_all.deb
$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.19/linux-headers-4.19.0-041900-generic_4.19.0-041900.201810221809_amd64.deb
$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.19/linux-image-unsigned-4.19.0-041900-generic_4.19.0-041900.201810221809_amd64.deb
$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.19/linux-modules-4.19.0-041900-generic_4.19.0-041900.201810221809_amd64.deb
```

#### Step 2. Install the Linux kernel

```sh
$ sudo dpkg -i *.deb
```

#### Step 3. Reboot the system

```sh
$ sudo reboot
```

#### Step 4. Check whether kernel upgrade succeeded or not

```sh
$ uname -r
```

Output:

```
4.19.0-041900-generic
```

## Reference

- [How to Upgrade the Ubuntu 18.04 Kernel to v4.19](https://graspingtech.com/upgrade-ubuntu-18-04-kernel/)
- [Linux Kernel 4.19 Released, How to Install it in Ubuntu](https://ubuntuhandbook.org/index.php/2018/10/linux-kernel-4-19-released-install-ubuntu/)
