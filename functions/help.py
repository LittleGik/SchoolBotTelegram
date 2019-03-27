from basicFunc import *

def getTextHelp(file):
    textHelp = open(file+'.txt','r',encoding='utf-8')
    text=textHelp.read()

    return text

def sendHelp(chatId):
    return sendMess(chatId, getTextHelp('fileText/help'))
