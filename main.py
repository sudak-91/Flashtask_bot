import telebot
import setting
import DB.dbmain as db




bot = telebot.TeleBot(setting.token)

@bot.message_handler(commands=['start'])
def repeat_all_message(message):
    bot.send_message(message.chat.id, "Hi")
    print(message.chat.id)
    DB = db.DBmain(setting.db_name)
    result = DB.select_id(message.chat.id)

    if len(result) == 0:
        keybord = telebot.types.InlineKeyboardMarkup()
        callback_button = telebot.types.InlineKeyboardButton(text='Регистрация', callback_data="registration")
        keybord.add(callback_button)
        bot.send_message(message.chat.id, "Я не знаю кто ты)", reply_markup= keybord)
    else:
        bot.send_message(message.chat.id, result)

@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data=="registration":
            bot.send_message(call.message.chat.id, "Как вас зовут?")
            @bot.message_handler(content_types='text')
            def registration(message):
                DB = db.DBmain(setting.db_name)
                DB.add_user(message.chat.id, message.text)


if __name__ == "__main__":
    bot.polling(none_stop=True)