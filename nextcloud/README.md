# Nextcloud

## Installation

```bash
$ git clone https://github.com/HeroCTF/heroctf-stack
$ cd heroctf-stack/nextcloud
$ cat <<EOF > .env
POSTGRES_PASSWORD=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c32)
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c32)
NEXTCLOUD_TRUSTED_DOMAINS=nextcloud.yourdomain.com
COLLABORA_DOMAIN=collabora.yourdomain.com
COLLABORA_PASSWORD=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c32)
EOF
$ sudo docker-compose up -d
```

## Applications

- Nextcloud : Hosting service.
- Colabora online : Office online.
- Redis : Cache service
- PostgreSQL : Database server.