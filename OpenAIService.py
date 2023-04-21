import openai as openai

from API_KEY import *

API_KEY= getOpenAIApiKey()

openai.api_key = API_KEY

def sendPromptGPT3Turbo(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': prompt}])
    return response

