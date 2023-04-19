import openai as openai

from API_KEY import *

API_KEY= getApiKey()

openai.api_key = API_KEY

# response = openai.Completion.create(model="text-davinci-003", prompt="Napisz cześć Magdalena ", temperature=1, max_tokens=100)
# print(response)

