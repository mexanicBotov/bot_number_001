import telebot
from telebot import types
import random
from requests import get
from bs4 import BeautifulSoup

from telebot import apihelper
 
apihelper.proxy = {'http':'http://217.182.96.199:3128',
                   }#'https':'https://169.255.225.4:53281'}

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)
            
token = '576771008:AAFBb3PQjTJTW33ogZ_Xgru8S7HP_20wBbw'
bot = telebot.TeleBot(token)
bot.set_update_listener(listener)

        
stickersList = ['CAADAgADAQADi607HFPFkz_ao3qOAg',
                'CAADAgADAgADi607HDgCNWtGK8S8Ag',
                'CAADAgADAwADi607HITNFgABri8pnQI',
                'CAADAgADBAADi607HD3U5Wsmv6HCAg',
                'CAADAgADBQADi607HLmhaCty5u_RAg',
                'CAADAgADBgADi607HFtWgj96hQkMAg',
                'CAADAgADBwADi607HF12FbYfZ_7bAg',
                'CAADAgADCAADi607HMc0kFAPmaH7Ag',
                'CAADAgADCQADi607HDnLTBgHFED3Ag',
                'CAADAgADCgADi607HAX_Czjh-RzWAg',
                'CAADAgADCwADi607HFCp3GjfQE3yAg',
                'CAADAgADDAADi607HEUsZxooPqR-Ag',
                'CAADAgADDQADi607HJjeQ56EmaCRAg',
                'CAADAgADAQAD9lUxG5csTsJY88NdAg' ,
                'CAADAgADAgAD9lUxGysvA6C-jwaVAg' ,
                'CAADAgADAwAD9lUxG6H7Us0usmRBAg' ,
                'CAADAgADBAAD9lUxG5c5Mha_dy6XAg' ,
                'CAADAgADBQAD9lUxGxwgqnFavK_PAg' ,
                'CAADAgADBgAD9lUxG-mBasbZRCQRAg' ,
                'CAADAgADBwAD9lUxG7Hr6BJ6DoHpAg' ,
                'CAADAgADCAAD9lUxG-iYrBCNQ3cyAg' ,
                'CAADAgADCQAD9lUxG3gHDIIBUtN6Ag' ,
                'CAADAgADCgAD9lUxG7xbepSQGsAOAg' ,
                'CAADAgADCwAD9lUxG0QBP-O4VZ_7Ag' ,
                'CAADAgADDAAD9lUxGyAlog1lKQgrAg' ,
                'CAADAgADDQAD9lUxG_-XtXQ5qZHVAg' ,
                'CAADAgADDgAD9lUxG4s9zmoc6aAiAg' ,
                'CAADAgADDwAD9lUxG4_tUn7P89vAAg' ,
                'CAADAgADEAAD9lUxGy8umjccQNk4Ag' ,
                'CAADAgADEQAD9lUxG1qSGUKj_djSAg' ,
                'CAADAgADEgAD9lUxG_5ANb8CJXXwAg' ,
                'CAADAgADEwAD9lUxG7PfuU5P3in9Ag' ,
                'CAADAgADFAAD9lUxG2rbp2WFymTzAg',
                'CAADAgADAQAD9lUxG5csTsJY88NdAg' ,
                'CAADAgADAgAD9lUxGysvA6C-jwaVAg' ,
                'CAADAgADAwAD9lUxG6H7Us0usmRBAg' ,
                'CAADAgADBAAD9lUxG5c5Mha_dy6XAg' ,
                'CAADAgADBQAD9lUxGxwgqnFavK_PAg' ,
                'CAADAgADBgAD9lUxG-mBasbZRCQRAg' ,
                'CAADAgADBwAD9lUxG7Hr6BJ6DoHpAg' ,
                'CAADAgADCAAD9lUxG-iYrBCNQ3cyAg' ,
                'CAADAgADCQAD9lUxG3gHDIIBUtN6Ag' ,
                'CAADAgADCgAD9lUxG7xbepSQGsAOAg' ,
                'CAADAgADCwAD9lUxG0QBP-O4VZ_7Ag' ,
                'CAADAgADDAAD9lUxGyAlog1lKQgrAg' ,
                'CAADAgADDQAD9lUxG_-XtXQ5qZHVAg' ,
                'CAADAgADDgAD9lUxG4s9zmoc6aAiAg' ,
                'CAADAgADDwAD9lUxG4_tUn7P89vAAg' ,
                'CAADAgADEAAD9lUxGy8umjccQNk4Ag' ,
                'CAADAgADEQAD9lUxG1qSGUKj_djSAg' ,
                'CAADAgADEgAD9lUxG_5ANb8CJXXwAg' ,
                'CAADAgADEwAD9lUxG7PfuU5P3in9Ag' ,
                'CAADAgADFAAD9lUxG2rbp2WFymTzAg',
                'CAADAgADAQAD9lUxG5csTsJY88NdAg' ,
                'CAADAgADAgADNQrBDhnQb9TfXxNDAg',
                'CAADAgADAwADNQrBDhTmTZ0zlFFqAg',
                'CAADAgADBAADNQrBDhxfOoIOP13JAg',
                'CAADAgADBQADNQrBDi23kh4kF-k7Ag',
                'CAADAgADBgADNQrBDrVi0ELSL1zyAg',
                'CAADAgADBwADNQrBDvLqfDwCRQ5SAg',
                'CAADAgADCAADNQrBDnAs6c8pXBeMAg',
                'CAADAgADCQADNQrBDrUY_aU2SMu7Ag',
                'CAADAgADAQADhoNqF0AykX_u8nghAg',
                'CAADAgADBAADhoNqF1RRKZvuzAs2Ag',
                'CAADAgADBgADhoNqF4qoqJGuNWjyAg',
                'CAADAgADBwADhoNqF9Wf4h3LEsHiAg',
                'CAADAgADBQADhoNqF6_AmmkLThF0Ag',
                'CAADAgADAgADd4SFF4vZhzWnjk-KAg',
                'CAADAgADEAADd4SFF6neAg_BEXk6Ag',
                'CAADAgADAQADd4SFF-eDg31__dPiAg',
                'CAADAgADAwADd4SFF-U0saMGIgz8Ag',
                'CAADAgADBAADd4SFFwd1Eet0EiR2Ag',
                'CAADAgADBQADd4SFFxiGuVkrNV7gAg',
                'CAADAgADGQADd4SFF4Vs4UR3b7nVAg',
                'CAADAgADCAADd4SFF5SrsIkPXriMAg',
                'CAADAgADDAADd4SFF52aUzHpAa7DAg',
                'CAADAgADDwADd4SFF3DBKaoJ4-OxAg',
                'CAADAgADDQADd4SFF6t62pLDIdqNAg',
                'CAADAgADCQADd4SFF3in2ClabG8wAg',
                'CAADAgADFgADd4SFF00l-OP_TGcLAg',
                'CAADAgADGwADd4SFFzOWbD3SHU8GAg',
                'CAADAgADFAADd4SFFx3-ffmxrrdPAg',
                'CAADAgADEQADd4SFF4o9Tq4d7Wd4Ag',
                'CAADAgADBgADd4SFF1YHSp3ZA9fsAg',
                'CAADAgADCgADd4SFF1URpfnLJZa4Ag',
                'CAADAgADCwADd4SFF7gYA63equHwAg',
                'CAADAgADIAADd4SFF6DF7rqMvrlEAg',
                'CAADAgADDgADd4SFF2h1boGofv6CAg',
                'CAADAgADEgADd4SFF2D4QNz6aiIsAg',
                'CAADAgADEwADd4SFF6KAOd55fBGtAg',
                'CAADAgADJgADd4SFFzig6MiF8-UmAg',
                'CAADAgADIwADd4SFFzJ0fuuYe0DzAg',
                'CAADAgADBwADd4SFF0v2YctH8EbVAg',
                'CAADAgADJwADd4SFFw0UdvX8XZB5Ag',
                'CAADAgADFQADd4SFF1Qps6wiL3MQAg',
                'CAADAgADFwADd4SFF7xCNud_iIL5Ag',
                'CAADAgADGAADd4SFF-SOzmSp6paKAg',
                'CAADAgADGgADd4SFF_ySJn6SWGXZAg',
                'CAADAgADIQADd4SFF9cOBlU_-CnBAg',
                'CAADAgADIgADd4SFF1t_0kPU9UFAAg',
                'CAADAgADHAADd4SFF0UPuefBe9qTAg',
                'CAADAgADHQADd4SFFwgFU1zL0AO9Ag',
                'CAADAgADHgADd4SFF5LjX2FKLqk0Ag',
                'CAADAgADHwADd4SFF9CFxegdP9JoAg',
                'CAADAgADJAADd4SFF9BM-ft_nZPSAg',
                'CAADAgADJQADd4SFF9U8w8hw4QZUAg',]

#def write_stickList():
#    with open("stickersList.txt","r") as f:
#        for i in f:
#            stickersList.append(i)
#    f.close

GROUP_ID = -274884695

    
    

    

@bot.message_handler(commands = ['stick'])
def get_start(message):
    rnd = random.randrange(0, 104, 1)
    #bot.send_message(message.chat.id, 'Слушаюсь и повенуюсь')
    bot.send_sticker(message.chat.id, stickersList[rnd])
    
@bot.message_handler(commands = ['send_stick'])
def send_sticks(message):
    rnd = random.randrange(0, 104, 1)
#    if chanse == 0:
    bot.send_sticker(GROUP_ID, stickersList[rnd])
    
@bot.message_handler(commands = ['hi'])
def get_start2(message):
    bot.send_message(message.chat.id, 'Здравствуйте')
    
@bot.message_handler(commands = ['yes'])
def get_start3(message):
    bot.send_message(message.chat.id, 'Да')
    
@bot.message_handler(commands = ['who_are_you'])
def get_start4(message):
    bot.send_message(message.chat.id, 'Качок')
    
@bot.message_handler(commands = ['hata'])
def get_start4(message):
    bot.send_message(message.chat.id, 'Без проблем')
    
@bot.message_handler(commands = ['game'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Крутим", callback_data="test1")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Играем в бутылочу", reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    won = random.randrange(0, 2, 1)
    if won == 0:
        if call.message:
            if call.data == "test1":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Красава")
    if won == 1:
        if call.message:
            if call.data == "test1":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лох")
                
@bot.message_handler(commands = ['weather'])
def find_weather(message):
    s_city = "Ufa,RU"
    city_id = 0
    appid = "ffcce017b2512cc3d358d2f46c860a1f"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
    pass
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        
        print("conditions:", data['weather'][0]['description'])
        bot.send_message(message.chat.id, "Погода в УФЕ: "+data['weather'][0]['description'])
        print("temp:", data['main']['temp'])
        bot.send_message(message.chat.id, "Температура: "+str(data['main']['temp'])+"C°")
        print("temp_min:", data['main']['temp_min'])
        #bot.send_message(message.chat.id, "Температура:"+data['main']['temp'])
        #print("temp_max:", data['main']['temp_max'])
    except Exception as e:
        print("Exception (weather):", e)
    pass
    #bot.send_message(message.chat.id, 'Что хотите передать?')
#@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_AGE.value)
#def get_upd(message):
    #rnd = random.randrange(0, 104, 1)
    #bot.send_sticker(message.chat.id, stickersList[rnd])
#@bot.message_handler(chat_id = message.chat.id)


@bot.message_handler(content_types=["sticker"])
def repeat_all_messages(message): 
#    chanse = random.randrange(0, 3, 1)
    rnd = random.randrange(0, 104, 1)
#    if chanse == 0:
    bot.send_sticker(message.chat.id, stickersList[rnd])
    
@bot.message_handler(content_types=["text"])
def sand_txt(message):
    if message.text[0] == "*":
        s = ""
        for i in message.text:
            if i != "*": s = s+i
        bot.send_message(GROUP_ID, s)
    #f_id = str(message.sticker.file_id)
    #print("'",f_id,"',", sep='')
#@bot.message_handler(commands=['start'])
#def start_bot():
#    repeat_all_messages              
#@bot.message_handler(content_types=["text"])
#def repeat_all_messages2(message): 
#    chanse = 0 # random.randrange(0, 3, 1)
#    rnd = random.randrange(0, 104, 1)
#    if chanse == 0:
#        bot.send_sticker(message.chat.id, stickersList[rnd])
    
def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

bot.polling(none_stop=True)