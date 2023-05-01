
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return render_template("glyph_translate.html")

## 9/28/21 Try out more, and varied, marks
@app.route('/marks', methods=['GET'])
def marks():
	return render_template("extended_glyph_translate.html")

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

@app.route('/drawn_lines', methods=['GET'])
def drawn_lines():
	return render_template("drawn_lines_translate.html")

@app.route('/drawn_marks', methods=['GET'])
def drawn_marks():
	return render_template("drawn_marks_translate.html")

@app.route('/pattern_1', methods=['GET'])
def pattern_1():
	return render_template("pattern_1.html")

@app.route('/pattern_1_saveable', methods=['GET'])
def pattern_1_saveable():
	return render_template("pattern_1_saveable.html")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5050)
