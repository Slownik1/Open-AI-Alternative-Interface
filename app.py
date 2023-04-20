import requests
from flask import *
from formDTO import *

app = Flask(__name__)


@app.route("/index", methods=['GET', 'POST'])
@app.route("/" , methods=['GET', 'POST'])
def say_hello():
    if request.method =="POST":
        prompt = request.form.get("prompt")
        print(prompt)
    return render_template("index.html", prompt=prompt)


if __name__ == '__main__':
    app.run()
