
import requests
url='https://api.telegram.org/bot853307556:AAEP98YuAL1nx2a0Gz3hcVfNuFxrFxLC1Hk/'

def requestAllUpdate(urlbot):
  params = {'timeout': 100, 'offset': None}
  response = requests.get(urlbot +'getupdates', data = params ) # делаем запрос на сайт
  return response.json()

def requestLastUpdate(allUpdate):
  lastUpdate = allUpdate['result']
  indexlastUpdate = len(lastUpdate) - 1 
  return lastUpdate[indexlastUpdate]


def requestLastUpdateId(requestLastUpdate):
  lastUpdate = requestLastUpdate['update_id']
  return int(lastUpdate)
  

def getChatId(requestLastUpdate):
  chatId=requestLastUpdate['message']['from']['id'] # result[]
  return chatId
def getFirstName(requestLastUpdate):
  firstName = requestLastUpdate['message']['from']['first_name']
  return firstName
def getLastName(requestLastUpdate):
  lastName = requestLastUpdate['message']['from']['last_name']
  return lastName
def getText(requestLastUpdate):
  text = requestLastUpdate['message']['text']
  return text
def getTime(requestLastUpdate):
  time=requestLastUpdate['message']['date']
  return time
def sendMess(chatId, text):
  params={'chat_id':chatId,'text':text}
  response = requests.post(url + 'sendMessage', data = params)
  return response


