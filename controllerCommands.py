# нахождение команды и её правильное исполнение
# добавление команды вывода информации о других команд
import sys
sys.path.append('c:\\Users\\LittleGik\\Documents\\GitHub\\SchoolBotTelegram\\functions\\')
from basicFunc import *
from schedule import *
from TimeLesson import *
from help import *



def startCommand(lastUpdate,lastLastUpdate):

    lastTime = getTime(lastUpdate)
    lastLastTime = getTime(lastLastUpdate)

    lastChatId = getChatId(lastUpdate)
    lastLastChatId = getChatId(lastLastUpdate)

    while lastTime != lastLastTime:
        findCommand(lastUpdate,lastTime)
        lastLastTime = lastTime
    


def findCommand(lastUpdate,lastDate):
    lastTime = int(lastDate)
    command = getText(lastUpdate)
    chatId = getChatId(lastUpdate)

    if(command == '/schedule'):
        return getSchedule(chatId,lastTime)
    elif(command == '/help'):
        return sendHelp(chatId)
    elif(command == '/timelesson'):
        return sendTimeLesson(chatId, lastTime)
    else: return sendMess(chatId,'Неверная команда. Воспользуйтесь командой /help')
    
