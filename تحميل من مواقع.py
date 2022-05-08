import telebot
import requests
from telebot import types
#- - - - - - - #
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
#- - - - - - - #
token = input(Z+"["+F+"●"+Z+"]"+B+"TOKEN : ")
id = input(Z+"["+F+"●"+Z+"]"+B+" id  : ")
chi = input(Z+"["+F+"●"+Z+"]"+Y+"يورز القناة بدون @  : ")
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def s(message):
	from_id = message.from_user.id
	m = "عذرا عزيزي عليك اشتراك بالقناة البوت"
	url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{chi}&user_id={from_id}"
	req = requests.get(url)
	if from_id == id or 'member' in req.text or 'creator' in req.text or 'administrator' in req.text:
		name = message.from_user.first_name
		bot.send_message(message.chat.id, "اهلا عزيزي {name} في بوت تحميل من مواقع\n\n ارسل رابط ليتم تحميل\n dev : @d666d6")
	else:
		bot.send_message(message.chat.id, "{} : @{}".format(m,chi))
@bot.message_handler(func=lambda m: True)
def Get(message):
    try:
        msg = message.text
        bot.send_message(message.chat.id, text="انتضر قليل من فضلك .")
        url = f"https://iiraq.tk/api/s.php?url={msg}"
        req = requests.get(url)
        o = req.json()
        o1 = o["meta"]["title"]
        o4 = o["url"][0]["url"]
        
        bot.send_video(message.chat.id,o4)
        bot.send_message(message.chat.id,f"العنوان : {o1}")
    except:
        pass
bot.polling()