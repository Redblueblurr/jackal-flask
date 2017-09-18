from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World."

@app.route("/welcome")
def welcome():
    return "Jackal Flask Setup Tutorial!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
