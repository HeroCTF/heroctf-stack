# Nextcloud

## Services

- Nextcloud : Hosting service.
- Colabora online : Office online.
- Redis : Cache service.
- PostgreSQL : Database server.

## Plugins

### Customization

- Breeze Dark : Dark theme.

### Intregration

- Twitter integration : Twitter notifications on dashboard.
- Keeweb : Keepass web integration.

### Web app

- Draw.io : Draw.io editor.
- Mind map : A mindmap editor.
- Collabora Online : Online office editor.
- Deck : Web todo list.
- Mail : Web mail.

### Alerting / Security

- Quota warning : Alerting on disk quota.
- Brute-force settings : Protects again bruteforce.

## Accessing files using Linux

You can access nextcloud files from your file manager (ex: `Nautilus`, `Dolphin`, ...)

Read the [docs](https://docs.nextcloud.com/server/20/user_manual/en/files/access_webdav.html#accessing-files-using-linux), for more information.

### File manager : Nautilus

Generic URL : `davs://example.com/nextcloud/remote.php/dav/files/<USERNAME>/`

Example : `davs://drive.heroctf.fr/remote.php/dav/files/admin/`

### File manager : Dolphin

Generic URL : `webdav://example.com/nextcloud/remote.php/dav/files/<USERNAME>/`
