from api import *
import os
import flask

app = flask.Flask(__name__)

if __name__ == '__init__.py':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
    # app.run(debug=True, threaded=True, port=5050)
	