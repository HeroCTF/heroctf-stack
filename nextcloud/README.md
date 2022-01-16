# Nextcloud

## Applications

- Nextcloud : Hosting service.
- Colabora online : Office online.
- Redis : Cache service.
- PostgreSQL : Database server.

## Accessing files using Linux

You can access nextcloud files from your file manager (ex: `Nautilus`, `Dolphin`, ...)

Read the [docs](https://docs.nextcloud.com/server/20/user_manual/en/files/access_webdav.html#accessing-files-using-linux), for more information.

### Example with Nautilus

URL : `davs://example.com/nextcloud/remote.php/dav/files/<USERNAME>/`

Example : `davs://drive.heroctf.fr/remote.php/dav/files/admin/`

### Example with Dolphin

URL : `webdav://example.com/nextcloud/remote.php/dav/files/<USERNAME>/`