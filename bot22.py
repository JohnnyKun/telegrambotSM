import telebot

bot = telebot.TeleBot('1995689321:AAE92ClZ7eNS1oEtm_MCM55JulUYRRiLvxo')


# AdvancedCustomFilter is for list, string filter values
class MainFilter(telebot.custom_filters.AdvancedCustomFilter):
    key='text'
    @staticmethod
    def check(message, text):
        return message.text in text

# SimpleCustomFilter is for boolean values, such as is_admin=True
class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key='is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']


@bot.message_handler(is_admin=True, commands=['admin']) # Check if user is admin
def admin_rep(message):
    bot.send_message(message.chat.id, "Здорово отец)")

@bot.message_handler(is_admin=False, commands=['admin']) # If user is not admin
def not_admin(message):
    bot.send_message(message.chat.id, "Ты не отец(")

@bot.message_handler(text=['Здорово']) # Response to hi message
def welcome_hi(message):
    bot.send_message(message.chat.id, ':)')

@bot.message_handler(text=['Пока']) # Response to bye message
def bye_user(message):
    bot.send_message(message.chat.id, ':(')

@bot.message_handler(text=['hehe','хехе','))',')))'])
def hehe_user(message):
        bot.send_message(message.chat.id, 'юморишь-юморишь')

@bot.message_handler(text=['План Аркадий'])
def hehe_user(message):
        bot.send_message(message.chat.id, 'Destroy mode was activate')

@bot.message_handler(text=['Привет','привет', 'Hi', 'hi', 'konnichiwa'])
def hello_user(message):
        bot.send_message(message.chat.id, 'привет')

@bot.message_handler(text=['@TadaNingen', 'Легенда'])
def hello_user(message):
        bot.send_message(message.chat.id, 'вызывается скамMACHINE(ОРЕЛ)')

@bot.message_handler(text=['@Shrijayavardenepurakotte'])
def hello_user(message):
        bot.send_message(message.chat.id, 'вызывается суетолог')

@bot.message_handler(text=['(',':(',':/','(((','(('])
def hello_user(message):
        bot.send_message(message.chat.id, 'что с лицом? сделай проще')

@bot.message_handler(text=['Именно','именно', 'имено'])
def hello_user(message):
        bot.send_message(message.chat.id, 'абсолютно! (а нет заскамил<3)')

@bot.message_handler(text=['@ZEUXMark'])
def hello_user(message):
        bot.send_message(message.chat.id, 'Марк, появись!')

@bot.message_handler(text=['Спокойной ночи','спокойной ночи'])
def hello_user(message):
        bot.send_message(message.chat.id, 'и сладких тебе снов а')

@bot.message_handler(text=['да?','Да?'])
def hello_user(message):
        bot.send_message(message.chat.id, 'да(а может и нет, я не разбираюсь)')


@bot.message_handler(text=['лох', 'ящик', 'Ящик', 'Клоун', 'Лох'])
def hello_user(message):
        bot.send_message(message.chat.id, '@TheMoonProds кам хиар')


@bot.message_handler(text=['Кто главный?'])
def hello_user(message):
        bot.send_message(message.chat.id, '@TheMoonProds - мой отец, @TadaNingen - мой праотец')


@bot.message_handler(text=['Лучшая игра?'])
def hello_user(message):
        bot.send_message(message.chat.id, 'Minecraft !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

@bot.message_handler(text=['Дедосатака'])
def hello_user(message):
        bot.send_message(message.chat.id, 'Ddos attack' * 200)

@bot.message_handler(text=['setall'])
def hello_user(message):
        bot.send_message(message.chat.id, '@Shrijayavardenepurakotte @TadaNingen @TheMoonProds @Helen_matyash @letoijok @ZEUXMark @meri_ii @smrnv0 @lizi_lok @ivanbalalaka @')


@bot.message_handler(text=['Ребенок'])
def hello_user(message):
        bot.send_message(message.chat.id, '@Shrijayavardenepurakotte')
photo = open(r'C:\Users\vasog\Pictures\apology.JPG', 'rb')
@bot.message_handler(text=['Извинись'])
def hello_user(message):
    bot.send_photo(message.chat.id, photo)


# Do not forget to register filters
bot.add_custom_filter(MainFilter())
bot.add_custom_filter(IsAdmin())

bot.polling(skip_pending=True,non_stop=True) # Skip old updates