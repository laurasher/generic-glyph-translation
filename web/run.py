
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return render_template("glyph_translate.html")

@app.route('/spiral', methods=['GET'])
def spiral():
	return render_template("glyph_translate_spiral.html")

@app.route('/spectro_lines', methods=['GET'])
def spectro_lines():
	return render_template("spectro_lines.html")

@app.route('/spectro_blobs', methods=['GET'])
def spectro():
	# return render_template("spectro.html")
	return render_template("spectro_blobs.html")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5050)
