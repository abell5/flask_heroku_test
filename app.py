from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello_world!'
	#return render_template('home.html')