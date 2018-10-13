from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    response = flask.jsonify('pong!')
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    # app.run(host='localhost')
    # es necesario ejecutar el programa con sudo po el ssl
    app.run(host='127.0.0.1', port=443, ssl_context='adhoc')
    # app.run(host='0.0.0.0', port=8080)
