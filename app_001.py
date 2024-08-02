import os
import random
import telebot
from telebot import types

def read_file(path):
    fo = open(path, 'r')
    text = fo.read()
    fo.close()
    return text.splitlines()


apiToken = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(apiToken)
path = "./resources/data.txt"
arr = read_file(path)
maxLength = len(arr)
@bot.message_handler(commands=['start'])


def start(message):
    helloText = """КАК ИСПОЛЬЗОВАТЬ ВОПРОСЫ:
1. Данный бот содержит 122 вопроса. Нажимайте на кнопку "👋 Получить вопрос"
2. Предложите вашему ребёнку поиграть с вами в игру "Ответь на вопрос". Вы по очереди выбираете вопрос и даёте на него ответ. Если вопрос не нравится то можно выбрать следующий. Никакого давления.
3. Данным ботом можно пользовать в дороге или при ожидании в очереди, чтобы поговорить с ребёнком и весело провести время. Или договоритесь отвечать по одному вопросу  перед ужином, когда вся семья садится кушать. Или может быть устраивайте семейную встречу на выходных с десертом, фильмом и потом ответом на вопросы. Любое время и любая форма общения с использованием этих вопросов будут полезны.
4. Не давите на ребёнка когда он отвечает на вопросы. Не ждите каких-то особенно умных или развёрнутых ответов. Радуйтесь всему что ребёнок решает вам сообщить отвечая на вопросы. Фокусируйтесь на том как вы отвечаете на вопросы которые попадают вам. Очень важно, чтобы в этом общении не было давления или особых ожиданий друг от друга. Чтобы это время было просто спокойным и приятным временем вместе с ребёнком.
5. Вы можете выбрать разные вариант, либо каждый выбирает вопросы по очереди и отвечают каждый на свой вопрос. Либо подросток выбирает вопрос в боте и потом все участники отвечают на один и тот же вопрос. Либо можете использовать любые правила которые предложит вам ваш ребёнок.
6. Заранее договоритесь со всеми участниками игры о том, что то, что вы рассказываете друг другу отвечая на вопросы останется только между вами.
Подчеркивайте что ваши разговоры строго конфиденциальны. Тогда все участники будут чувствовать себя более расслабленно."""

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Получить вопрос")
    markup.add(btn1)
    bot.send_message(message.from_user.id, helloText, reply_markup=markup)

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    if message.text == '👋 Получить вопрос':
        n = random.randint(0, maxLength-1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.InlineKeyboardButton('👋 Получить вопрос')

        markup.add(btn1)
        bot.send_message(message.from_user.id, arr[n], reply_markup=markup) #ответ бота

    elif message.text == '👋 Получить вопрос':
        n = random.randint(0, maxLength-1)
        bot.send_message(message.from_user.id, arr[n], parse_mode='Markdown')

   

while True:
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout = 5) #обязательная для работы бота часть
    except Exception as error:
        print("Error = ", error)
        sleep(3)
