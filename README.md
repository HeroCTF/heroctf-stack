# HeroCTF stack

List of self-hosted projects.

## Projects

- [discord-bot](discord-bot) : A Discord bot that helps us to reinitialize the Discord server after a CTF.
- [nextcloud](nextcloud) : Project management and self hosting.
- [nginx](nginx) : Acts as a reverse-proxy in front of all web applications exposed to the web.

## Installation

Each project contains a `docker-compose.yml` file. You can run each of them using `docker-compose up -d`.

You can also use a simple bash script to do it :

```bash
$ git clone https://github.com/HeroCTF/heroctf-stack.git
$ cd heroctf-stack
$ cat <<EOF >nextcloud/.env
POSTGRES_PASSWORD=02737e4e8c87d7466b623c1f844fdd71
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=aae9ed2aebd46960a986cfb376bc1eca
NEXTCLOUD_TRUSTED_DOMAINS=drive.heroctf.fr
COLLABORA_DOMAIN=collabora.heroctf.fr
COLLABORA_PASSWORD=16c52c6e8326c071da771e66dc6e9e57
EOF
$ # Edit nginx/conf.d/*.conf files
$ # Add HTTPS certificates to nginx/certs/
$ bash install.sh
```

> Generate self-signed certificate :
>
> `openssl genrsa > privkey.pem`<br>
> `openssl req -new -x509 -key privkey.pem > fullchain.pem`

## Todo

- Add certbot docker to nginx