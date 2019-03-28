import datetime
import time
from basicFunc import *

def sendTimeLesson(chatId, lastTime):
    arrayTimeIndex = TimeLesson(lastTime)
    time = int(arrayTimeIndex[0])
    index = int(arrayTimeIndex[1])
    BegText = 'Хлопчик, быстрее тикай на урок. До начала урока осталось: '
    EndText = 'Держись, ещё немного и тебя отпустят. До конца урока осталось: '
    if(arrayTimeIndex[1] == -1):
        return sendMess(chatId, 'Вася, уже урок')
    elif arrayTimeIndex[0] == -2:
        return sendMess(chatId,'Ещё не время учиться')
    else:
        if arrayTimeIndex[0] % 2 == 0:
            text = BegText + arrayTimeIndex[0] + 'минут(-ы)'
            return sendMess(chatId,text)
        else: 
            text = EndText + arrayTimeIndex[0] + 'минут(-ы)'
            return sendMess(chatId,text)

def getTextTimeLesson(file): #Возвращает массив, где под четным индексом время звонки [номерзвонка][час][минуты]
    text = open(file +'.txt', 'r', encoding='utf-8')
    text = text.read()
    
    countSignal = text.count('*')
    arraySignalHourMinute = []

    for i in range(0,countSignal):
        arraySignalHourMinute.append([])

    for i in range(0,countSignal):
        indexSlice = text.find(':')
        for j in range(0,2):
            if j == 0 :
                hour = text[0:indexSlice]
                arraySignalHourMinute[i].append([hour])
            else: 
                minute = text[indexSlice + 1:indexSlice+2]
                arraySignalHourMinute[i].append([minute])
                text = text[6:]
    return arraySignalHourMinute

def TimeLessonFunction(lastTime, h):

    min = str(time.gmtime(lastTime))
    minut = min.find('tm_min=')
    hour = min.find('tm_hour=')
    daysend = int(time.strftime('%w', time.localtime()))
    
    #Костыль для часов
    hoursend = min[hour+8:hour+10]
    if hoursend.count(',') != 0:
        hoursend = int(hoursend[0:hoursend.find(',')]) + h
    else: hoursend = int(hoursend) + h
    
    #Костыль для мину
    minsend = min[minut+7:minut+9]
    if minsend.count(',') != 0:
        minsend = int(minsend[0:minsend.find(',')])
    else: minsend  = int(minsend)
    arrayHourMinut = [0]*2
    arrayHourMinut[0] = hoursend
    arrayHourMinut[1] = minsend
    return arrayHourMinut


def TimeLesson(lastTime):
    
    arrayTime = TimeLessonFunction(lastTime, 4) # Время пользователя
    hour = arrayTime[0]
    minute = arrayTime[1]
    
    arraySignalHourMinute = getTextTimeLesson('fileText/TimeLesson') # Расписание звонков
    
    for i in range(0,len(arraySignalHourMinute)):

        if(hour == arraySignalHourMinute[i][0] ):
            
            if(minute < arraySignalHourMinute):
                timeSignal = arraySignalHourMinute[i][1] - minute
                indexSignal = i
                break;
            
            elif(minute > arraySignalHourMinute[i][0]):
                timeSignal = 60 - minute + arraySignalHourMinute[i][1]
                indexSignal = i
            
            elif(minute == arraySignalHourMinute[i][0]):
                indexSignal = -1
                timeSignal = -1 
            arrayTimeIndex = []*2
            arrayTimeIndex[0] = timeSignal
            arrayTimeIndex[1] = indexSignal

            return arrayTimeIndex
        else:
            arrayTimeIndex = [-2]*2
            return arrayTimeIndex
                


    
