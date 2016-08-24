from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!! It's me. Scott Ginther"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
