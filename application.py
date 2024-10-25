from flask import Flask

app = Flask(__name__)

@app.route("/")
def print_rollno():
	return "2350"