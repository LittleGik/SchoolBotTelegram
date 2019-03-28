# нахождение команды и её правильное исполнение
# добавление команды вывода информации о других команд
import sys
sys.path.append('c:\\Users\\LittleGik\\Documents\\GitHub\\SchoolBotTelegram\\functions\\')
from basicFunc import *
from schedule import getSchedule
from TimeLesson import sendTimeLesson
from help import sendHelp
from start import sendStart



def startCommand(lastUpdate):
    findCommand(lastUpdate)

    


def findCommand(lastUpdate):
    lastTime = int(getTime(lastUpdate))
    command = getText(lastUpdate)
    chatId = getChatId(lastUpdate)

    if(command == '/schedule'):
        return getSchedule(chatId,lastTime)
    elif(command == '/start'):
        return sendStart(chatId)
    elif(command == '/help'):
        return sendHelp(chatId)
    elif(command == '/timelesson'):
        return sendTimeLesson(chatId, lastTime)
    else: return sendMess(chatId,'Неверная команда. Воспользуйтесь командой /help')
    
