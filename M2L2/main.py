import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот, который поможет тебе сохранять природу. Используй /help, чтобы узнать больше.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help(message):
    help_text = """
    Вот что я могу:
    /tips - Получить советы по сохранению природы.
    /actions - Узнать о текущих экологических акциях.
    """
    bot.reply_to(message, help_text)

# Обработчик команды /tips
@bot.message_handler(commands=['tips'])
def tips(message):
    tips_list = [
        "Экономьте воду: закрывайте кран, когда чистите зубы.",
        "Используйте многоразовые сумки вместо пластиковых пакетов.",
        "Сортируйте мусор для переработки.",
        "Выключайте свет, когда выходите из комнаты."
    ]
    bot.reply_to(message, tips_list[0])  

# Обработчик команды /actions
@bot.message_handler(commands=['actions'])
def actions(message):
    actions_text = "К сожалению, сейчас нет активных экологических акций. Но вы можете начать с малого: посадите дерево или уберите мусор в парке!"
    bot.reply_to(message, actions_text)

# Запуск бота
bot.infinity_polling()
