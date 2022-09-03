import telebot
from config import keys, TOKEN
from extensions import CurrencyConverter, APIExeptions

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n <имя валюты> <в какую валюту перевести> <количество валюты>\n Отправьте /values, чтобы увидеть все доступные валюты'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(mesage: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(mesage, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIExeptions('Неверное количество параметров')

        quote, base, amount = values
        total_base = CurrencyConverter.convert(quote, base, amount)
    except APIExeptions as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        total_base = int(amount) * float(total_base)
        text = f'По текущему курсу вы получите - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()