# api

from flask import Flask

app = Flask(__name__)

# -- ROTAS.
@app.route("/")
def hominho():

	return "<h1>Not authorized</h1>"


if __name__ == "__main__":
	app.debug=True
	app.run(host="0.0.0.0",port=5000)
