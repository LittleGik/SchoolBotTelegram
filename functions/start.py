from basicFunc import *

def sendStart(chatId):
    text = openStart('fileText/start')
    return sendMess(chatId, text)


def openStart(file):
    text = open(file + '.txt', 'r', encoding='utf-8')
    text = text.read()
    
    return text
