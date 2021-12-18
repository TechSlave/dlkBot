import telebot
import db
import leggin
import scraper
import urllib.request
from urllib.error import HTTPError
token = "2124853168:AAGjIAkOf5dGJYdlPMBxLSF_v57LsuCiDEw"
bot = telebot.TeleBot(token)


# @bot.message_handler(commands=[""])
@bot.message_handler(func=lambda m: True)
def cadastro_produto(message):
    '''
    Entry point for adding a product code
    '''
    print(message.chat.id, message.message_id, message.text)
    user = str(message.chat.id)
    message_text = (
        message.text
        .replace('/start ', '')
        .replace('/', '')
        .replace('📮', '')
        .strip()
        .split()
    )
    for word in message_text:
        if word.lower() == '@leguinebot':
            message_text.remove(word)
    """
    Scraping
    """
    codigo = message_text[0]
    try:
        url = scraper.get_url(codigo)
        urllib.request.urlretrieve(url)
        valor = scraper.get_valor(codigo)
        modelo = scraper.get_modelo(codigo)

        """
        Cria objeto Roupa
        """
        roupa1 = leggin.Roupa(codigo, url, modelo, valor)
        roupa1.update_valor(valor)

        # def add_produto(chat_id, modelo, codigo, url, valor, disponivel):
        db.add_produto(message.chat.id, roupa1.modelo, roupa1.codigo, roupa1.url, roupa1.valor, roupa1.disponivel)
        print(roupa1)
        bot.send_message(message.chat.id, roupa1)

    except urllib.error.HTTPError as err:
        if err.code == 404:
            bot.send_message(message.chat.id, "Código inválido")
            print(err.code)


"""@bot.route('/command ?(.*)')
def sending(mensagem, cmd):
    bot.send_message(mensagem.chat.id, "something_else")"""


@bot.message_handler('/lista')
def cadastro_produto(message):
    pass

print("started")
# bot.infinity_polling(timeout=10, long_polling_timeout = 5)
db.create_db()
bot.infinity_polling()


if __name__ == "__main__":
    db.create_db()
    bot.polling()


