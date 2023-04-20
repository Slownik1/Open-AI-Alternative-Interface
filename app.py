import requests
from flask import *
from formDTO import *
from OpenAIService import *
from jsonService import *

app = Flask(__name__)



@app.route("/index", methods=['GET', 'POST'])
@app.route("/" , methods=['GET', 'POST'])
def response():
    AIResponse = 'Hi'
    if request.method =="POST":
        userPrompt = request.form.get("prompt")
        AIResponse = sendPromptToGPT(userPrompt)
    return render_template("index.html", prompt=jsonFormater(AIResponse))


if __name__ == '__main__':
    app.run()
