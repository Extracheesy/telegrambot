import telegram.ext

import requests
import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def dog(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    print(chat_id)
    context.bot.send_photo(chat_id=chat_id, photo=url)

def start(update, context):
    update.message.reply_text("Hello! Starting the bot! trend / list / pred")

def trend(update, context):
    update.message.reply_text("Get market trend recommendation...")

def list(update, context):
    update.message.reply_text("Get stock list...")

def pred(update, context):
    update.message.reply_text("Get trend pred...")

def handle_message(update, context):
    update.message.reply_text(f"You said: {update.message.text}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('token.txt', 'r') as f:
        TOKEN = f.read()

    updater = telegram.ext.Updater(TOKEN, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(telegram.ext.CommandHandler("start",start))
    disp.add_handler(telegram.ext.CommandHandler("trend", trend))
    disp.add_handler(telegram.ext.CommandHandler("list", list))
    disp.add_handler(telegram.ext.CommandHandler("pred", pred))
    disp.add_handler(telegram.ext.CommandHandler('dog',dog))
    disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
