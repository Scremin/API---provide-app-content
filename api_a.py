# api

from flask import Flask, jsonify

from control_a import *

app = Flask(__name__)
app.url_map.strict_slashes = False


# -- ROTAS.
@app.route("/")
def hominho():

	try:

		res = get_a()

		return jsonify({'result':res})
		#return "<h1>Not authorized</h1>"

	except:

		return jsonify({'result':'test failed'})


if __name__ == "__main__":
	app.debug=True
	app.run(host="0.0.0.0",port=5000)
