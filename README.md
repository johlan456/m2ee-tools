m2ee-tools
==========

CLI tool for deploying and managing [Mendix](https://www.mendix.com/) applications on GNU/Linux.

This is a maintained fork of the [original m2ee-tools](https://github.com/mendix/m2ee-tools/) by Mendix, which is no longer actively developed.

## Supported Versions

- **Mendix Runtime:** 7, 8, 9 (tested). Version 10+ may work but is not yet verified.
- **Python:** 3.8+
- **OS:** Any GNU/Linux distribution

## Prerequisites

- Java (JRE 8 for Mendix 7, OpenJDK 11+ for Mendix 8/9)
- PostgreSQL client tools (`pg_dump`, `pg_restore`)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) for installation

## Installation

Install m2ee-tools as the app user (one install per application user):

```sh
sudo -u myapp uv tool install git+https://github.com/johlan456/m2ee-tools
```

To upgrade:

```sh
sudo -u myapp uv tool upgrade m2ee-tools
```

Ensure `~/.local/bin` is on the app user's `PATH`.

## Application Setup

Each Mendix application should run as a dedicated system user.

### 1. Create the app user and directory structure

```sh
sudo adduser --disabled-password --gecos "" myapp
sudo -u myapp mkdir -p /srv/mendix/myapp/{runtimes,web,model,data/database,data/files,data/model-upload,data/tmp}
sudo chmod 700 /srv/mendix/myapp/model /srv/mendix/myapp/data
```

### 2. Configure m2ee

As the app user, create `~/.m2ee/m2ee.yaml`:

```sh
sudo -u myapp mkdir -p /home/myapp/.m2ee
sudo -u myapp nano /home/myapp/.m2ee/m2ee.yaml
```

Minimal `~/.m2ee/m2ee.yaml`:

```yaml
m2ee:
  app_name: My Application
  app_base: /srv/mendix/myapp
  admin_port: 9000
  admin_pass: <long random string, not used manually>
  runtime_port: 8080
  javaopts:
    - "-Dfile.encoding=UTF-8"
    - "-Xmx512M"
    - "-Xms512M"
    - "-Djava.io.tmpdir=/srv/mendix/myapp/data/tmp"
  logfile: /srv/mendix/myapp/data/app.log

logging:
  - name: FileSubscriber
    type: file
    autosubscribe: INFO
    filename: /srv/mendix/myapp/data/app.log
    max_size: 10485760
    max_rotate: 7

mxruntime:
  DatabaseType: PostgreSQL
  DatabaseHost: "127.0.0.1:5432"
  DatabaseName: myapp
  DatabaseUserName: myapp
  DatabasePassword: <password>
```

See [examples/full-documented-m2ee.yaml](examples/full-documented-m2ee.yaml) for all available options.

### 3. Create the systemd service

Create `/etc/systemd/system/mendix-myapp.service`:

```ini
[Unit]
Description=Mendix myapp
After=network.target postgresql.service

[Service]
Type=forking
User=myapp
WorkingDirectory=/home/myapp
ExecStart=/home/myapp/.local/bin/m2ee -c start
ExecStop=/home/myapp/.local/bin/m2ee -c stop
PIDFile=/home/myapp/.m2ee/m2ee.pid
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Enable and start:

```sh
sudo systemctl daemon-reload
sudo systemctl enable --now mendix-myapp
```

## First-time Deployment

```sh
# Upload your .mda file to /srv/mendix/myapp/data/model-upload/, then as the app user:
sudo -u myapp m2ee

# Unpack the deployment archive
m2ee(myapp): unpack myapp-1.0.0.mda

# Download the Mendix Runtime (first time only)
m2ee(myapp): download_runtime

# Start the application
m2ee(myapp): start

# Create the initial admin user
m2ee(myapp): create_admin_user
```

## Common Commands

| Command | Description |
|---------|-------------|
| `sudo -u myapp m2ee` | Open interactive shell |
| `sudo systemctl status mendix-myapp` | Check service status |
| `sudo systemctl restart mendix-myapp` | Restart the application |
| `sudo -u myapp m2ee -c backup_db` | Dump the database |
| `sudo -u myapp m2ee -c unpack <file>` | Deploy a new MDA archive |

## Documentation

For detailed configuration and advanced setup, see the [documentation](doc/README.md).

## Development

```sh
git clone https://github.com/johlan456/m2ee-tools
cd m2ee-tools
uv venv
uv pip install -e .
```

## License

BSD 3-Clause. See [LICENSE](LICENSE).
