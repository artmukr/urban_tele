import requests
import re
from telebot import TeleBot
from telebot import types

bot = TeleBot("1017831541:AAEugg0KbRuc2EBR0vEdfZpZmCKLcG5lpGs")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_word(message):
	word = message.text
	translation = requests.get(
		f'http://api.urbandictionary.com/v0/define?term={word}'
	).json()
	mes = str(
		[el['definition'] for el in translation['list']])[1:-1].\
		replace(",", ',\n')

	words = re.findall(r"[[][\w, \s]*[]]", mes)

	bot.send_message(message.chat.id, mes)
	markup = types.ReplyKeyboardMarkup(row_width=2)

	for w in words:
		button = types.KeyboardButton(w[1:-1])
		markup.add(button)
	bot.send_message(message.chat.id, 'Choose your word: ', reply_markup=markup)


if __name__ == '__main__':
	bot.polling()
