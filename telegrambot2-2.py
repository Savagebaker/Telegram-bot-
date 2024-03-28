import telebot
import datetime
from telebot import types
from datetime import date
token = '6901025557:AAGVk4wO5EfZWwMcMV_OmZRH2o9lCNPAtgM'
bot = telebot.TeleBot(token)
d = datetime.datetime.utcnow().strftime("%Y%m%d")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row = ('Назад')
d1 = 0
d2 = 0
d3 = 0
d4 = 0
m1 = 0
y1 = 0
y2 = int(d[0:4])
m2 = int(d[4:6])
d11= int(d[6:8])
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Погнали!")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="""Привет, {0.first_name}! Погнали?
    """.format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])

def q1(message):
    if(message.text == "Погнали!")or (message.text == "Заново"):
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да")
            btn2 = types.KeyboardButton("Нет")
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id, text="""Работаешь сегодня?
            """.format(message.from_user), reply_markup=markup)
            bot.register_next_step_handler(message, q2)
        except:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Заново")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
            """.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def q2(message):
    try:
        if(message.text == "Да"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("1")
            btn2 = types.KeyboardButton("2")
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id, text="""Какой по счёту рабочий день?
            """.format(message.from_user), reply_markup=markup)
            bot.register_next_step_handler(message, work1)
        elif(message.text == "Нет"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("1")
            btn2 = types.KeyboardButton("2")
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id, text="""Какой по счёту выходной день?
            """.format(message.from_user), reply_markup=markup)
            bot.register_next_step_handler(message, free1)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заново")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
        """.format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def work1(message):
    try:
        if(message.text == "1"):
            msg = bot.send_message(message.chat.id, text="""Введи день.(Например 31)
            """,reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, month1)
        elif(message.text == "2"):
            msg = bot.send_message(message.chat.id, text="""Введи день.(Например 31)
            """, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, month2)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заново")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
        """.format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def free1(message):
    try:
        if(message.text == "1"):
            msg = bot.send_message(message.chat.id, text="""Введи день.(Например 31)
            """,reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, month3)
        elif(message.text == "2"):
            msg = bot.send_message(message.chat.id, text="""Введи день.(Например 31)
            """,reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, month4)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заново")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
        """.format(message.from_user), reply_markup=markup)
def month1(message):
    try:
        global d1
        msg  = bot.send_message(message.chat.id, text="""Введи месяц.(Например 12)
        """,reply_markup=types.ReplyKeyboardRemove())
        d1 = int(message.text)
        bot.register_next_step_handler(msg, year1)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заново")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
        """.format(message.from_user), reply_markup=markup)
def month2(message):
    try:
        global d2
        msg  = bot.send_message(message.chat.id, text="""Введи месяц.(Например 12)
        """,reply_markup=types.ReplyKeyboardRemove())
        d2 = int(message.text)
        bot.register_next_step_handler(msg, year1)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заново")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
        """.format(message.from_user), reply_markup=markup)
def month3(message):
    try:
        global d3
        msg  = bot.send_message(message.chat.id, text="""Введи месяц.(Например 12)
        """,reply_markup=types.ReplyKeyboardRemove())
        d3 = int(message.text)
        bot.register_next_step_handler(msg, year1)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заново")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
        """.format(message.from_user), reply_markup=markup)
def month4(message):
    try:
        global d4
        msg  = bot.send_message(message.chat.id, text="""Введи месяц.(Например 12)
        """,reply_markup=types.ReplyKeyboardRemove())
        d4 = int(message.text)
        bot.register_next_step_handler(msg, year1)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заново")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
        """.format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def year1(message):
    try:
        global m1
        msg =bot.send_message(message.chat.id, text="""Введи год.(Например 2023)
        """.format(message.from_user), reply_markup=types.ReplyKeyboardRemove())
        m1 = int(message.text)
        bot.register_next_step_handler(msg, formula_otca)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заново")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
        """.format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def formula_otca(message):
    global y1
    global d1
    global d2
    global d3
    global d4
    global m1
    global m2
    global y2
    global d11
    y1 = int(message.text)
    print(d,y1,d1,d2,d3,d4,m1,m2,y2,d11)
    if d1 !=0:
        try:
            date1 = date(y1,m1,d1)
            date2 = date(y2,m2,d11)
            delta = date1 - date2
            e = delta.days
            x = 0
            while x <= e - 4:
                x +=4
            if x == e:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                msg =bot.send_message(message.chat.id, text="""Это твой первый рабочий день.
                """.format(message.from_user), reply_markup=markup)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                bot.register_next_step_handler(msg, q1)
            elif e - x == 1:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                msg =bot.send_message(message.chat.id, text="""Это твой второй рабочий день.
                """.format(message.from_user), reply_markup=markup)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                bot.register_next_step_handler(msg, q1)
            elif e - x == 2:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                msg =bot.send_message(message.chat.id, text="""Это твой первый выходной день.
                """.format(message.from_user), reply_markup=markup)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                bot.register_next_step_handler(msg, q1)

            elif e - x == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                msg =bot.send_message(message.chat.id, text="""Это твой второй выходной день.
                """.format(message.from_user), reply_markup=markup)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                bot.register_next_step_handler(msg, q1)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
                """.format(message.from_user), reply_markup=markup)
        except:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Заново")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
            """.format(message.from_user), reply_markup=markup)
    elif d2 !=0:
        try:
            date1 = date(y1,m1,d2)
            date2 = date(y2,m2,d11)
            delta = date1 - date2
            e = delta.days
            x = 0
            while x <= e - 4:
                x +=4
            if x == e:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                msg =bot.send_message(message.chat.id, text="""Это твой второй рабочий день.
                """.format(message.from_user), reply_markup=markup)
                bot.register_next_step_handler(msg, q1)
            elif e - x == 1:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                msg =bot.send_message(message.chat.id, text="""Это твой первый выходной день.
                """.format(message.from_user), reply_markup=markup)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                bot.register_next_step_handler(msg, q1)
            elif e - x == 2:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                msg =bot.send_message(message.chat.id, text="""Это твой второй выходной день.
                """.format(message.from_user), reply_markup=markup)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                bot.register_next_step_handler(msg, q1)
            elif e - x == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                msg =bot.send_message(message.chat.id, text="""Это твой первый рабочий день.
                """.format(message.from_user), reply_markup=markup)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                bot.register_next_step_handler(msg, q1)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
                """.format(message.from_user), reply_markup=markup)
        except:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Заново")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
            """.format(message.from_user), reply_markup=markup)
    elif d3 !=0:
        try:
            date1 = date(y1,m1,d3)
            date2 = date(y2,m2,d11)
            delta = date1 - date2
            e = delta.days
            x = 0
            while x <= e - 4:
                x +=4
            if x == e:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                msg =bot.send_message(message.chat.id, text="""Это твой первый выходной день.
                """.format(message.from_user), reply_markup=markup)
                bot.register_next_step_handler(msg, q1)
            elif e - x == 1:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                msg =bot.send_message(message.chat.id, text="""Это твой второй выходной день.
                """.format(message.from_user), reply_markup=markup)
                bot.register_next_step_handler(msg, q1)
            elif e - x == 2:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                msg =bot.send_message(message.chat.id, text="""Это твой первый рабочий день.
                """.format(message.from_user), reply_markup=markup)
                bot.register_next_step_handler(msg, q1)
            elif e - x == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                msg =bot.send_message(message.chat.id, text="""Это твой второй рабочий день.
                """.format(message.from_user), reply_markup=markup)
                bot.register_next_step_handler(msg, q1)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
                """.format(message.from_user), reply_markup=markup)
        except:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Заново")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
            """.format(message.from_user), reply_markup=markup)
    elif d4 !=0:
        try:
            date1 = date(y1,m1,d4)
            date2 = date(y2,m2,d11)
            delta = date1 - date2
            e = delta.days
            x = 0
            while x <= e - 4:
                x +=4
            if x == e:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                d4 = 0
                msg =bot.send_message(message.chat.id, text="""Это твой второй выходной день.
                """.format(message.from_user), reply_markup=markup)
                bot.register_next_step_handler(msg, q1)
            elif e - x == 1:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                msg =bot.send_message(message.chat.id, text="""Это твой первый рабочий день.
                """.format(message.from_user), reply_markup=markup)
                bot.register_next_step_handler(msg, q1)
            elif e - x == 2:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                msg =bot.send_message(message.chat.id, text="""Это твой второй рабочий день.
                """.format(message.from_user), reply_markup=markup)
                bot.register_next_step_handler(msg, q1)
            elif e - x == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                m1 = 0
                y1 = 0
                msg =bot.send_message(message.chat.id, text="""Это твой первый выходной день.
                """.format(message.from_user), reply_markup=markup)
                bot.register_next_step_handler(msg, q1)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Заново")
                markup.add(btn1)
                bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
                """.format(message.from_user), reply_markup=markup)
        except:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Заново")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="""Что-то пошло не так.Попробуй ввести данные еще раз
            """.format(message.from_user), reply_markup=markup)


















bot.polling(none_stop=True, interval = 0)
