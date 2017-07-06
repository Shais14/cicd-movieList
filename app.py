import os
import signal
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from movies import generator

app = Flask(__name__)
Bootstrap(app)

signal.signal(signal.SIGINT, lambda s, f:os._exit(0))

@app.route("/")
def generate_movie_review():
	result = generator.generate_movie_review()
	return render_template('index.html', review = result)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port = os.getenv('PORT'))
