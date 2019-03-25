import sys
sys.path.append('C:/Users/LittleGik/Documents/GitHub/')
from basicFunc import *
from command import *

def main(): # Определяем команду, выполняем функцию
        lastUpdate = requestLastUpdate(requestAllUpdate(url)) # Записали в переменную данные последнего обновления
        chatId = getChatId(lastUpdate)
        command = getText(lastUpdate)
        if(str(command) == '/schedule'):
                findSchedule(chatId)
        else: print(lastUpdate)


main()
        

    
            
            










