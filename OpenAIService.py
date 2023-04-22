import openai as openai
import requests

from API_KEY import *

API_KEY= getOpenAIApiKey()

openai.api_key = API_KEY

def sendPromptGPT3Turbo(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': prompt}])
    return response["choices"][0]["message"]["content"]

def sendPromptDavinci3(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=150)
    return response["choices"][0]["text"]

def getAvalibleModel():
    response =openai.Model.list()
    return response

