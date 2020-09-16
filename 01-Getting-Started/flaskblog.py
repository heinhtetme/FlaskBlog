# October 9, 2019
# set FLASK_APP=flaskblog.py
# set FLASK_DEBUG=1
# flask run ( python flaskblog.py )

from flask import Flask
app = Flask(__name__)
# app.debug = True


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
