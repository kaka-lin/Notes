# SocketCAN Support for Kvaser Devices

If you want to [use SocketCAN with Kvaser devices](https://www.kvaser.com/socketcan-support-for-kvaser-devices-updated/), follow the steps as below.

#### Step 1. Check your `Linux kernel version: >= 4.19`

If your Linux kernel oldest than 4.19, please upgrade to Linux kernel 4.19, as below:

1. Download the 4.19 kernel (for 64 bit system):

    ```sh
    $ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.19/linux-headers-4.19.0-041900_4.19.0-041900.201810221809_all.deb
    $ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.19/linux-headers-4.19.0-041900-generic_4.19.0-041900.201810221809_amd64.deb
    $ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.19/linux-image-unsigned-4.19.0-041900-generic_4.19.0-041900.201810221809_amd64.deb
    $ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.19/linux-modules-4.19.0-041900-generic_4.19.0-041900.201810221809_amd64.deb
    ```

2. Install the Linux kernel

    ```sh
    $ sudo dpkg -i *.deb
    ```

3. Reboot the system

    ```sh
    $ sudo reboot
    ```

4. Check whether kernel upgrade succeeded or not

    ```sh
    $ uname -r
    ```

    Output:

    ```
    4.19.0-041900-generic
    ```

#### Step 2. Install Kvaser SocketCAN Device Drivers

1. Download [Kvaser SocketCAN Device Drivers](https://www.kvaser.com/download/?utm_source=software&utm_ean=7330130982192&utm_status=latest)

2. Unzip the files you just downloaded

    ```sh
    $ tar zxvf socketcan_kvaser_drivers.tar.gz
    ```

3. follow `README` install the driver (USB or PCIe).

    ###### If you encountered an `SSL error` when installing as bellow

    ```sh
    At main.c:158:
        - SSL error:02001002:system library:fopen:No such file or directory: bss_file.c:175
        - SSL error:2006D080:BIO routines:BIO_new_file:no such file: bss_file.c:178 sign-file: certs/signing_key.pem: No such file or directory
        DEPMOD 4.10.0-20-generic
    ```

    ###### Solution:

    1. You need to generate the key as below:

        ```sh
        $ openssl req -new -nodes -utf8 -sha512 -days 36500 -batch -x509 -config x509.genkey -outform DER -out signing_key.x509 -keyout signing_key.pem
        ```

        Where `x509.genkey` is a file with the contents:

        ```
        [ req ]
        default_bits = 4096
        distinguished_name = req_distinguished_name
        prompt = no
        string_mask = utf8only
        x509_extensions = myexts

        [ req_distinguished_name ]
        CN = kvaser.com

        [ myexts ]
        basicConstraints=critical,CA:FALSE
        keyUsage=digitalSignature
        subjectKeyIdentifier=hash
        authorityKeyIdentifier=keyid
        ```

    2. then moving the key you just generated to related `certs folder`

        ```sh
        $ sudo mv signing_key.pem signing_key.x509 `find /usr/src/*-generic/certs`
        ```

## Reference

- [No OpenSSL sign-file signing_key.pem leads to error while loading kernel modules](https://superuser.com/questions/1214116/no-openssl-sign-file-signing-key-pem-leads-to-error-while-loading-kernel-modules)
