import json

def jsonFormater(apiResponse):

    return (apiResponse["choices"][0]["message"]["content"])