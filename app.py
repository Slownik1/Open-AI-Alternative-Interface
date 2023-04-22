
from flask import *
from OpenAIService import *
from jsonService import *
from webService import *

app = Flask(__name__)



@app.route("/index", methods=['GET'])
@app.route("/" , methods=['GET'])
def index():
    return render_template("index.html", prompt="Hi",
                           data=[{'name':'GPT3Turbo'},{'name':'Davinci3'}])

@app.route("/index", methods=['POST'])
@app.route("/" , methods=['POST'])
def response():

    userPrompt = request.form.get("prompt")
    model = request.form.get("modelSelect")
    print(model)
    AIResponse = chooseModel(model, userPrompt)
    return render_template("index.html", prompt=AIResponse,
             data=[{'name': 'Davinci3'}, {'name': 'GPT3Turbo'}])

if __name__ == '__main__':
    app.run()
