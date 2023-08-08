import telebot
import json
from json.decoder import JSONDecodeError


bot = telebot.TeleBot("Insert token HERE")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет, ничтожество! Я бот, который может валидировать джсон. Вставляй его в сообщении и жми энтер")


@bot.message_handler(content_types=['text'])
def text_message(message):
    
    try:
        json_message = json.loads(message.text)
        bot.reply_to(message, "JSON - валидный.")
    except JSONDecodeError:
        bot.reply_to(message, "JSON - НЕвалидный.")
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка при обработке сообщения: {}".format(e))


bot.polling()
