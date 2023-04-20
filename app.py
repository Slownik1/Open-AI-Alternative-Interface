import requests
from flask import *
from formDTO import *
import OpenAIService

app = Flask(__name__)


@app.route("/index", methods=['GET', 'POST'])
@app.route("/" , methods=['GET', 'POST'])
def say_hello():
    AIResponse = 'Hi'
    if request.method =="POST":
        userPrompt = request.form.get("prompt")
        AIResponse = OpenAIService.sendPromptToGPT(userPrompt)
    return render_template("index.html", prompt=AIResponse)


if __name__ == '__main__':
    app.run()
