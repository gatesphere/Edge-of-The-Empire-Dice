from flask import render_template
from app import app, pages

@app.route("/")
def home():
	if request.method == "POST":
		if request.form["submit"] == "b":
			return render_template("index.html")
		elif request.form["submit"] == "f":
			return render_template("index.html")
		else:
			return render_template("index.html")
	elif request.method == "GET":
		return render_template("index.html")