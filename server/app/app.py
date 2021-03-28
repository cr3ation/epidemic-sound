from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import slack

# Create webapp
app = Flask(__name__)
api = Api(app)

# Limitations per host per day / hour
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["50 per day", "20 per hour"])


class Computer(Resource):
    def get(self, serial):
        data = "FOO BAR!"
        if not data:
            # Nothing to return
            return("", 204)
        return(data)

    def put(self, serial):
        data = request.json
        if not data:
            # Nothing was passed to webservice
            return("", 204)

        # TODO: Store data somewhere

        slack_info = 'Inventory recieved from *{}*'.format(serial)
        slack.post_message_to_slack(slack_info)

        return(jsonify(serialNumber=serial))


class HelloWorld(Resource):
    def get(self):
        return("Hello, World!")


api.add_resource(HelloWorld, "/hello")
api.add_resource(Computer, "/computer/<string:serial>")

if __name__ == "__main__":
    # Create certificates:
    # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    context = ('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', debug=False, ssl_context=('cert.pem', 'key.pem'))
