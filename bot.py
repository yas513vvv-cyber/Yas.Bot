import random
import string
import telebot

TOKEN = "8691264599:AAFI2VUoDEtfQjgSrJhhRi3Fs9LwfyR6XH4"
bot = telebot.TeleBot(TOKEN)

def generate_username(length=4):
    characters = string.ascii_lowercase + string.digits + "_."
    first_char = random.choice(string.ascii_lowercase)
    rest_chars = ''.join(random.choice(characters) for _ in range(length - 1))
    return first_char + rest_chars

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أرسل الأمر /gen لتوليد قائمة يوزرات تيك توك.")

@bot.message_handler(commands=['gen'])
def send_usernames(message):
    usernames = [generate_username(length=4) for _ in range(5)]
    response = "🎲 **اليوزرات المولدة:**\n\n"
    for u in usernames:
        response += f"`{u}`\n"
    bot.reply_to(message, response, parse_mode="Markdown")

if __name__ == "__main__":
    bot.infinity_polling()
