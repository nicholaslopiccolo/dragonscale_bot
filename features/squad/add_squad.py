from utils.bad_comand import bad_command
from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update
)
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)

from objects.squad import squad


App = None


def init(app):
    global App
    App = app

#   /add_admin role uid name


def start(update: Update, context: CallbackContext) -> int:
    params = update.message.text.split()
    # print(params)
    if len(params) < 4:
        return bad_command(update, context)
    # try:

    cid = int(params[1])
    tp = int(params[2])
    name = ' '.join(params[3:])

    sq = squad(cid, tp, name)

    App.add_squad(sq)

    update.message.reply_text(
        f"NEW SQUAD:\n Name: {sq.get_name()}\n type: {sq.get_type()}\n channel id: {sq.get_chat_id()}")

    return ConversationHandler.END
    # except ValueError:
    #    return bad_command(update, context)
