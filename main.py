import telebot
#import leggin
#import scraper
import urllib3
token = "2124853168:AAGjIAkOf5dGJYdlPMBxLSF_v57LsuCiDEw"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["teste"])
def teste(mensagem):
    bot.send_message(mensagem.chat.id, "teste")



bot.infinity_polling(timeout=10, long_polling_timeout = 5)


