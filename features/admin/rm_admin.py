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

App = None
white_list = None


def init(app):
    global App
    global white_list
    App = app
    white_list = app.get_white_list()


def start(update: Update, context: CallbackContext) -> int:
    params = update.message.text.split()

    if len(params) != 2:
        return bad_command(update, context)

    try:
        uid = int(params[1])
        player = white_list.get_player(uid)

        if player == -1:
            update.message.reply_text(f"player not found")
            return ConversationHandler.END

        r_name = white_list.get_rank_name(player.get_rank())
        uid = player.get_uid()
        msg = f" Role: {r_name.capitalize()}\n Name: {player.get_name()}\n UID: {uid}"

        is_you = ""

        if uid == update.message.from_user.id:
            is_you = "\n... YOURSELF"

        App.rm_player(player)

        update.message.reply_text(f"Removing...\n\n{msg}\n{is_you}")
    except ValueError:
        return bad_command(update, context)
