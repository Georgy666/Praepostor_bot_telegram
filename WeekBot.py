#!/usr/bin/env python3.5
import telebot
import time
import Const
import datetime
import TopWeek
import BottomWeek
import ConfigLogging

API_TOKEN = Const.token
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    ConfigLogging.logging.info(ConfigLogging.logStart) # Log command 'start'

    bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name)

@bot.message_handler(commands=['help'])
def help_command(message):
    ConfigLogging.logging.info(ConfigLogging.logHelp)  # Log command 'help'

    bot.send_message(message.chat.id, Const.Reg)
    bot.send_message(message.chat.id, Const.Araay_Commands_week)
    bot.send_message(message.chat.id, Const.Araay_Commands_day_week)
    bot.send_message(message.chat.id, Const.Araay_Commands_common) 

@bot.message_handler(commands=['weekend'])
def weekend_command(message):
    ConfigLogging.logging.info(ConfigLogging.logWeekend) # Log command 'weekend'

    event_date = datetime.date.today()

    ny_2018Start = datetime.date(2018, 1, 1)  # Winter holiday
    ny_2018Over = datetime.date(2018, 1, 9)
    DeltaOverWinter = ny_2018Over - event_date
    DeltaStartWinter = ny_2018Start - event_date

    if event_date == ny_2018Start:
        bot.send_message(message.chat.id, 'каникулы ещё идут. А закончатся они, через: ' + str(DeltaOverWinter.days) + ' дней')
    else:
        bot.send_message(message.chat.id, 'Зимние каникулы закончились и снова начнутся через: ' + str(DeltaStartWinter.days) + ' дней')

    sum_2017Start = datetime.date(2017, 6, 25)  # Summer holiday
    sum_2017Over = datetime.date(2017, 9, 1)
    DeltaOverSummer = sum_2017Over - event_date
    DeltaStartSummer = sum_2017Start - event_date

    if event_date == sum_2017Start:
        bot.send_message(message.chat.id,
                         'каникулы ещё идут. А закончатся они, через: ' + str(DeltaOverSummer.days) + ' дней')
    else:
        bot.send_message(message.chat.id,
                         'Летние каникулы закончились и снова начнутся через: ' + str(DeltaStartSummer.days) + ' дней')


@bot.message_handler(commands=['curator'])  # Send curator number
def curator_command(message):
    ConfigLogging.logging.info(ConfigLogging.logCurator)   # Log weekend 'curator'
    bot.send_message(message.chat.id, 'Держи, ' + message.chat.first_name + ':' + Const.CuratorNumber)

@bot.message_handler(commands=['whatweek'])  # Send number week
def what_week_command(message):
    ConfigLogging.logging.info(ConfigLogging.logWhatweek)  # Log command 'whatweek'

    now_date = datetime.date.today()
    day = now_date.day
    if day % 2 == 0:
        bot.send_message(message.chat.id, 'нижняя неделя')
    else:
        bot.send_message(message.chat.id, 'верхняя неделя')

@bot.message_handler(content_types=['text'])
def top_and_bottom_week(message):

    if message.text == 'вся верхняя неделя' or message.text == 'Вся верхняя неделя':  # request top week
        bot.send_message(message.chat.id, TopWeek.Top_array, ConfigLogging.logging.info(ConfigLogging.log_TopAllWeek)) # Log request schedules
    elif message.text == 'пн, верхняя неделя' or message.text == 'Пн, верхняя неделя':
        bot.send_message(message.chat.id, TopWeek.Top_array_Mon, ConfigLogging.logging.info(ConfigLogging.log_TopMon))
    elif message.text == 'вт, верхняя неделя' or message.text == 'Вт, верхняя неделя':
        bot.send_message(message.chat.id, TopWeek.Top_array_Tue, ConfigLogging.logging.info(ConfigLogging.log_TopTue))
    elif message.text == 'ср, верхняя неделя' or message.text == 'Ср, верхняя неделя':
        bot.send_message(message.chat.id, TopWeek.Top_array_Wed, ConfigLogging.logging.info(ConfigLogging.log_TopWed))
    elif message.text == 'чт, верхняя неделя' or message.text == 'Чт, верхняя неделя':
        bot.send_message(message.chat.id, TopWeek.Top_array_Thu, ConfigLogging.logging.info(ConfigLogging.log_TopThu))
    elif message.text == 'пт, верхняя неделя' or message.text == 'Пт, верхняя неделя':
        bot.send_message(message.chat.id, TopWeek.Top_array_Fri, ConfigLogging.logging.info(ConfigLogging.log_TopFri))
    elif message.text == 'сб, верхняя неделя' or message.text == 'Сб, верхняя неделя':
        bot.send_message(message.chat.id, TopWeek.Top_array_Sat, ConfigLogging.logging.info(ConfigLogging.log_TopSat))

    elif message.text == 'вся нижняя неделя' or message.text == 'Вся нижняя неделя':  # request bottom week
        bot.send_message(message.chat.id, BottomWeek.Bottom_array, ConfigLogging.logging.info(ConfigLogging.log_BottomAllWeek))
    elif message.text == 'пн, нижняя неделя' or message.text == 'Пн, нижняя неделя':
        bot.send_message(message.chat.id, BottomWeek.Bottom_array_Mon, ConfigLogging.logging.info(ConfigLogging.log_BottomMon))
    elif message.text == 'вт, нижняя неделя' or message.text == 'Вт, нижняя неделя':
        bot.send_message(message.chat.id, BottomWeek.Bottom_array_Tue, ConfigLogging.logging.info(ConfigLogging.log_BottomTue))
    elif message.text == 'ср, нижняя неделя' or message.text == 'Ср, нижняя неделя':
        bot.send_message(message.chat.id, BottomWeek.Bottom_array_Wed, ConfigLogging.logging.info(ConfigLogging.log_BottomWed))
    elif message.text == 'чт, нижняя неделя' or message.text == 'Чт, нижняя неделя':
        bot.send_message(message.chat.id, BottomWeek.Bottom_array_Thu, ConfigLogging.logging.info(ConfigLogging.log_BottomThu))
    elif message.text == 'пт, нижняя неделя' or message.text == 'Пт, нижняя неделя':
        bot.send_message(message.chat.id, BottomWeek.Bottom_array_Fri, ConfigLogging.logging.info(ConfigLogging.log_BottomFri))
    elif message.text == 'сб, нижняя неделя' or message.text == 'Сб, нижняя неделя':
        bot.send_message(message.chat.id, BottomWeek.Bottom_array_Sat, ConfigLogging.logging.info(ConfigLogging.log_BottomSat))
    elif message.text == 'вс' or message.text == 'Вс':  # Weekend
        bot.send_message(message.chat.id, 'Сегодня выходной!')

    # Bot response to some of the phrases of the user.

    elif message.text == 'Привет' or message.text == 'привет':
        bot.send_message(message.chat.id, 'Какое расписание тебе нужно, ' + message.chat.first_name + '?', ConfigLogging.logging.info(ConfigLogging.log_reqest))

    elif message.text == 'Пока' or message.text == 'пока':
        bot.send_message(message.chat.id, 'До встречи, ' + message.chat.first_name, ConfigLogging.logging.info(ConfigLogging.log_goodbay))

    else:
        bot.send_message(message.chat.id, 'Эта команда не верна, попробуй ещё раз.', ConfigLogging.logging.info(ConfigLogging.log_NoneCommand))


# bot tries connect to telegram api, if connection error him tries again and so five time
i = 0
while i <= 4:
    try:
    
        bot.polling(none_stop=True, interval=0)
    
    except Exception as err:
    
        ConfigLogging.logging.error(err)
        time.sleep(350)
        i += 1
    
        print("VPN error!")
        

# this code send random cat, if requested command in development
'''
directory  = 'C:\\users\Vilgelm\Desktop\Задачи на Python\Bot\Photo'
    all_files_in_directory = os.listdir(directory)
    random_file = random.choice(all_files_in_directory)
    img = open(directory + '/' + random_file, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img, 'пока что в разработке...')
    img.close()'''
