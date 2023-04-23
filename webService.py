from OpenAIService import *


def chooseModel(argument, userPrompt):
    match argument:
        case "Davinci3":
            print('davinc')
            return sendPromptDavinci3(userPrompt)
        case "GPT3Turbo":
            print('GPT')
            return sendPromptGPT3Turbo(userPrompt)
        case "Dalle":
            return sendPromptDalle(userPrompt)
        case default:
            return ""