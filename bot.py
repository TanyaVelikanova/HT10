import telebot
import requests


bot = telebot.TeleBot('5900301929:AAFzHGw1NRHwvF1HCj3m_jdnU8ft4s-ij-U')

@bot.message_handler(commands=["currency"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Выберите валюту, например USD')
        
@bot.message_handler(content_types=["text"])
def handle_text(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    key = message.text
    try:
        message_v = res['Valute'][key]['Value']
        message_n = res['Valute'][key]['Name']
        bot.send_message(message.chat.id, message_n + ': ' + str(message_v))
    except KeyError:
        bot.send_message(message.chat.id, 'Такой валюты нет в списке')
print('server run')
bot.infinity_polling()