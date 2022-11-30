# Linux APT 遇到 NO_PUBKEY 的 error

issue 如下所示:

```sh
Err:20 http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release.gpg
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F60F4B3D7FA2AF80
```

```sh
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F60F4B3D7FA2AF80
W: Failed to fetch http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/Release.gpg  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F60F4B3D7FA2AF80
W: Some index files failed to download. They have been ignored, or old ones used instead.
```

## 解法

```sh
$ sudo apt-key adv --keyserver keys.gnupg.net --recv-keys <PUBKEY>
```

或

```sh
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <PUBKEY>
```

Example:

```sh
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F60F4B3D7FA2AF80
```
