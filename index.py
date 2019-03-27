import sys
sys.path.append('c:\\Users\\LittleGik\\Documents\\GitHub\\SchoolBotTelegram\\functions\\')
from basicFunc import *
from controllerCommands import *
import datetime

url='https://api.telegram.org/bot853307556:AAEP98YuAL1nx2a0Gz3hcVfNuFxrFxLC1Hk/'

def main(): # Определяем команду, выполняем функцию
        
        allUpdate = requestAllUpdate(url)
        lastUpdate = requestLastUpdate(allUpdate)
        update_id = requestLastUpdateId(lastUpdate)
        while True:
                startCommand(lastUpdate,requestLastLastUpdate(allUpdate))

main()
     
            










