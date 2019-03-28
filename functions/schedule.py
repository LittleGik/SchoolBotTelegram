import datetime
import time
from basicFunc import *
def getNameDay(numDay): # Выводим название дня недели. На вход номер дня недели, 0 - Воскресенье
    if numDay == 0:
        day='Воскресенье'
    elif numDay == 1:
        day='Понедельник'
    elif numDay == 2:
        day='Втоник'
    elif numDay == 3:
        day='Среда'
    elif numDay == 4:
        day='Четверк'
    elif numDay == 5:
        day='Пятница'
    else: day='Суббота'
    return day

def getTextSchedule(file): #Считываем расписание с файла. Указываем путь к файлу без .txt. На выходе массив, где a[0] - воскресенье

    textSchedule = open(file+'.txt','r', encoding='utf-8')
    text=textSchedule.read()

    # Понедельник
    i=0
    il=text.find('Расписание на Вторник')
    Monday = text[i:il]

    #Вторник
    i=text.find('Расписание на Вторник')
    Tuesday = text[i:text.find('Расписание на Среду')]

    #Среда
    i=text.find('Расписание на Среду')
    Wednesday = text[i:text.find('Расписание на Четверг:')]

    #Четверг
    i=text.find('Расписание на Четверг:')
    Thursday = text[i:text.find('Расписание на Пятницу')]

    #Пятница
    i=text.find('Расписание на Пятницу:')
    Friday = text[i:text.find('Расписание на Субботу')]

    #Суббота
    i=text.find('Расписание на Субботу')
    Saturday = text[i:]

    a=[' ',Monday, Tuesday, Wednesday, Tuesday, Friday, Saturday]
    return a

def sendSchedule(chatId,numday): # отправка расписание
    numday = int(numday)
    arrayDaySchedule = getTextSchedule('fileText/Schedule')
    response = sendMess(chatId,arrayDaySchedule[numday])
    return response


def getSchedule(chatId,lastTime): # Определяет и отправляет расписание
    id = chatId
    min = str(time.gmtime(lastTime))
    minut = min.find('tm_min=')
    hour = min.find('tm_hour=')
    daysend = int(time.strftime('%w', time.localtime()))
    hoursend = int(min[hour+8:hour+10])
    minsend = int(min[minut+7:minut+9])
    numDay = 0
    if(int(hoursend) < 15):
        numDay = daysend
        sendSchedule(id,numDay)
    elif(int(hoursend) >= 15):
        numDay = daysend+1
        sendSchedule(id,numDay)
    else: sendSchedule(id,'Ошибка')
            
    
