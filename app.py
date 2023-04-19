from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index", methods=['GET', 'POST'])
@app.route("/")
def say_hello():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()