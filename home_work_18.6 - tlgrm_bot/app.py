import telebot
from config import keys, TOKEN
from extensions import CurrencyConverter, APIExeptions

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help']) # присылает инструкцию пользователю поссле ввода комманд /start /help
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n <имя валюты> <в какую валюту перевести> <количество валюты>\n Отправьте /values, чтобы увидеть все доступные валюты'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values']) # присылает список доступных валют
def values(mesage: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(mesage, text)

@bot.message_handler(content_types=['text', ]) # основной обработчки запросов
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ') # отлавливаем ошибки обращаясь к файлу extensions, выдаем пользователю сообщения о роде ошибки

        if len(values) != 3:
            raise APIExeptions('Неверное количество параметров')

        quote, base, amount = values
        total_base = CurrencyConverter.convert(quote, base, amount)

    except APIExeptions as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')

    else:
        total_base = int(amount) * float(total_base) # считаем итоговое число сконвертированной валюты
        text = f'По текущему курсу вы получите - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()