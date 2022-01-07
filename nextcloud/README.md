# Nextcloud

## Installation

```bash
$ git clone https://github.com/HeroCTF/heroctf-stack
$ cd heroctf-stack/nextcloud
$ echo "POSTGRES_PASSWORD=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c32)" > .env
$ echo 'NEXTCLOUD_ADMIN_USER=admin' >> .env
$ echo "NEXTCLOUD_ADMIN_PASSWORD=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c32)" >> .env
$ echo 'NEXTCLOUD_TRUSTED_DOMAINS=nextcloud.yourdomain.com' >> .env
$ sudo docker-compose up -d
```

## Applications

- Nextcloud : Hosting service.
- Redis : Cache service
- PostgreSQL : Database server.