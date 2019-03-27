import datetime
import time
from basicFunc import *

def sendTimeLesson(chatId, lastTime):
    
    return sendMess(chatId,TimeLesson(lastTime))

    

def TimeLesson(lastTime):
    
    daysend = int(time.strftime('%w', time.localtime()))
    min = str(time.gmtime(1553705087))
    minut = min.find('tm_min=')
    hour = min.find('tm_hour=')
    daysend = int(time.strftime('%w', time.localtime()))
    hoursend = int(min[hour+8:hour+10])
    minsend = int(min[minut+7:minut+9])
    
    arraySignal = getTextTimeLesson('fileText/TimeLesson') # Массив в формате [номерзвонка][0 - час\ 1 -минута]
    lastTimeSignal = arraySignal[len(arraySignal)][0] # достаём час последнего звонка
    firstTimeSignal = arraySignal[len(arraySignal)][0] # достаём минуту последнего звонка 
    
    if(daysend != 0 and hoursend <= lastTimeSignal  and hoursend >= firstTimeSignal):
        for i in range(1,len(arraySignal)):
            if(hoursend == arraySignal[i][0]):
                if(minsend <= arraySignal[i][1]):
                    BegSignal = arraySignal[i][1] - minsend
                    index = i
                    break;
            else:
                if(minsend > arraySignal[i][1]):
                    BegSignal = 60 - minsend
                    BegSignal += arraySignal[i+1][1]
                    index = i
                    break;
        if(index % 2 == 0):
            text = 'До начала урока осталось:  ' + BegSignal +' минут(-ы)'
        else: text = 'Держись, ещё немного и звонок: ' +BegSignal + ' минут(-ы).'
        return text        
                        
    else: return 0



def getTextTimeLesson(file): #Возвращает массив, где под четным индексом время перемены
    
    text = open(file +'.txt', 'r', encoding='utf-8')
    text = text.read()
    
    countSignal = text.count('*')
    arraySignalHourMinute = [0]*countSignal+1
    
    for i in range(1,countSignal+1):
        for j in range(0,2):
            indexSlice=text.find(':')
            if(j == 0):
                hour = text[2:indexslice]
                arraySignalHourMinute[i].append()
            else: 
                minute = text[indexSlice+1:indexSlice+2]
                text = text[6:]
    return arraySignalHourMinute

    


    
