import requests
from flask import *
from formDTO import *
from OpenAIService import *
from jsonService import *

app = Flask(__name__)



@app.route("/index", methods=['GET'])
@app.route("/" , methods=['GET'])
def index():
    return render_template("index.html", prompt="Hi")

@app.route("/index", methods=['POST'])
@app.route("/" , methods=['POST'])
def response():

    userPrompt = request.form.get("prompt")
    AIResponse = sendPromptDavinci3(userPrompt)
    return render_template("index.html", prompt=AIResponse)

if __name__ == '__main__':
    app.run()
