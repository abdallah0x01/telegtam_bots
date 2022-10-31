from telegram.ext import *
API_KEY = '5495430715:AAEjpn2vbB5J-yeSxx-LnmMKfQ6pDb_yPCA'

print('bot started...')


def simple_response(text):
    user_message = str(text).lower()

    if user_message in ('what is your career', 'career', 'career?'):
        return 'I am electrical student engineer'
    if user_message in ('country', 'country?', 'what is you canotry?', 'what is you canotry'):
        return 'I am from Egypt'
    if user_message in ('what is your hoppies', 'hoppies', 'hoppies?'):
        return 'love programming, hacking, reading, making things'
    else:
        return 'I don\'t understand you!'


def start_command(update, context):
    update.message.reply_text('type anything')


def help_command(update, context):
    update.message.reply_text(
        'You can ask for: \n1) Career\n2) Country\n3) Hoppies')


def handle_message(update, context):
    text = str(update.message.text).lower()  # text that user type
    response = simple_response(text)
    update.message.reply_text(response)  # response of bot to user


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))

    # filter message writen in bot
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()


main()
