from flask import Flask, render_template, flash, request, url_for, redirect, session
import sys

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def home():
    return render_template('home.html')
	
if __name__ == '__main__':
    app.debug = True
    app.run()