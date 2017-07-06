import os
import signal
from flask import Flask
from movies import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f:os._exit(0))

@app.route("/")
def generate_movie_review():
	page = '<html><body><h1>'
	page += generator.generate_movie_review();
	page += '</h1></body></html>'
	return page

if __name__ == "__main__":
	app.run(host='0.0.0.0', port = os.getenv('PORT'))