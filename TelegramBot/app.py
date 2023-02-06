import telebot

from config import TOKEN, keys
from extensions import ConvertionExeption, CrypoConvector

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])  #Инструкция
def echo_test(message: telebot.types.Message):
    text = "Чтобы перевести валюту наберите сообщение в формате\n 'Валюта которую переводите' 'Валюта в которую переводите' 'Сумма'\nНапример:\nрубль доллар 100\nЧтобы посмотреть список доступных валют введите: /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values']) #Валюты
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ]) # Конвектор
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExeption('Некорректный ввод параметров')

        quote, base, amount = values
        total_base = CrypoConvector.convert(quote, base, amount)

    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)



bot.polling()
