# What is this?
A proof of concept of a client/server solution written i Python. Client gather inventory data from macOS and send to server.

### Server
Full docker support using environment variables and docker-compose. Also works with python venv. Server uses self signed certificates (not recommended). Includes slack notification support (currently enforced).

### Client
Gather information about a macOS and sends inventory as json to `127.0.0.1:5000/computer/{serialnumber}`

## Installation
### Server
Begin with installing the server. See [server instructions](https://github.com/cr3ation/epidemic-sound/tree/master/server)

### Client
Install client _after_ server is created. See [client instructions](https://github.com/cr3ation/epidemic-sound/tree/master/client)

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## Authors
* **Henrik Engström** - *Initial work* - [cr3ation](https://github.com/cr3ation)
See also the list of [contributors](https://github.com/cr3ation/epidemic-sound/contributors) who 
participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
