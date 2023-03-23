openssl req -new -nodes -utf8 -sha512 -days 36500 -batch -x509 -config x509.genkey -outform DER -out signing_key.x509 -keyout signing_key.pem
sudo mv signing_key.pem signing_key.x509 `find /usr/src/*-generic/certs`
