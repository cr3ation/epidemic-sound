# Server
A webserver written in python to recieve computer inventory data, store it, and send a Slack-notification.

## Installation – manually
### Windows
1) Create python3 _venv_ with `virtualenv venv` (install virtualvenv `pip install virtualenv` if missing)
2) Activate with `venv\Scripts\activate`
3) Run `pip install -r requirements.txt` to install required modules.
4) Edit config in `.\app\settings_sample.py` and rename to `.\app\settings.py`.
5) Start `C:\path-to-venv\Scripts\python.exe` with argument `"C:\path\to\app.py"`

### macOS
1) Create python3 _venv_ with `virtualenv venv` (run `pip install virtualenv` if virtualenv is needed)
2) Activate with `source venv\bin\activate`
3) Run `pip install -r requirements.txt` to install required modules.
4) Edit config in `./app/settings_sample.py` and rename to `./app/settings.py`.
5) Create a LaunchAgent in `/Library/LaunchAgents/com.cr3ation.server.plist` and execute `/path/to/app.py`

## Note
Default port is 5000

## Docker
Install using `docker-compose` or by building the image from scratch. Examples below.

### Prerequisities
In order to run within a container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [macOS](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Install using docker-compose
Edit `docker-compose.yaml`. Add `SLACK_CHANNEL`, `SLACK_TOKEN`, `SLACK_ICON_URL` and `SLACK_USER_NAME`. Then run
```shell
docker-compose up 
```

### Install using docker
#### Build image
```shell
docker build -t server:latest . 
```

#### Run container
```shell
docker run -d -e SLACK_CHANNEL=<channel> -e SLACK_TOKEN=<token> -e SLACK_ICON_URL=<https://server.com/icon.png> -e SLACK_USER_NAME=<user>  server:latest
```

### Environment Variables
* `SLACK_CHANNEL` - Mandatory
* `SLACK_TOKEN` - Mandatory
* `SLACK_ICON_URL` - Mandatory
* `SLACK_USER_NAME` - Mandatory

### Volumes
* `/app/` - Entire project including logs

### Useful File Locations (inside container)
* `/app/app.py` - Main application
* `/app/settings.py` - Settings

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## Authors
* **Henrik Engström** - *Initial work* - [cr3ation](https://github.com/cr3ation)
See also the list of [contributors](https://github.com/cr3ation/epidemic-sound/contributors) who 
participated in this project.
