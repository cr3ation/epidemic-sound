# Client
Gather inventory data and send to a webservice (127.0.0.1:5000)

## Prerequesite 
* python3

## Usage
```shell
usage: client.py [-h] [-d] [-u] [-p]

Sends inventory information to a webservice

optional arguments:
  -h, --help   show this help message and exit
  -d, --dry    dry run, no data sent to webservice
  -u, --users  list all users
  -p, --print  prints computer information
```

## Examples
`python3 client.py`
```shell
{"computerNames": {"ComputerName": "59458", "LocalHostName": "59458", "HostName": "59458"}, "fileVault": "Enabled", "firewall": "Off", "operatingSystem": "11.2.3", "users": [{"name": "henrik.engstrom", "id": 502}, {"name": "admin", "id": 501}], "serialNumber": "C02ZN353MD7Q", "googleChrome": {"HomepageLocation": "https://buzz.schibsted.com", "ShowHomeButton": true}}
```

`python3 client.py --print`
```shell
  [general]:
    [firewall]: Off
    [names]: {'ComputerName': '59458', 'LocalHostName': '59458', 'HostName': '59458'}
    [os]: 11.2.3
    [serial]: C02ZN353MD7Q
  [storage]:
    [encryption]: Enabled
  [users]: 
    [user]: henrik.engstrom (502)
    [user]: admin (501)
  [applications]:
    [googleChrome]: {'HomepageLocation': 'https://buzz.schibsted.com', 'ShowHomeButton': True}
    [microsoftOffice]: None

```

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## Authors
* **Henrik Engström** - *Initial work* - [cr3ation](https://github.com/cr3ation)
See also the list of [contributors](https://github.com/cr3ation/epidemic-sound/contributors) who 
participated in this project.
