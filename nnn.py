import telebot

# ضع هنا التوكن الخاص بك
TOKEN = '7205713684:AAEFtrxxIjHvMEBg-Vd3fki_YgopbJfVcU0'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello!")

print("Bot is running...")
bot.polling()