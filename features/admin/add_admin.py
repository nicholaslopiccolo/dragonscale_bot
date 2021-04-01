from utils.bad_comand import bad_command
from objects.player import player
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

#   /add_admin role uid name


def start(update: Update, context: CallbackContext) -> int:
    params = update.message.text.split()

    if len(params) < 4:
        return bad_command(update, context)

    try:
        role = int(params[1])
        uid = int(params[2])
        name = ' '.join(params[3:])

        pl = white_list.get_player(uid)
        if pl != -1:
            update.message.reply_text(f"player exsist")
            return ConversationHandler.END

        admin = player(uid, role, name)
        App.add_player(admin)

        update.message.reply_text(
            f"{admin.get_name().capitalize()} is from now a brave { white_list.get_rank_name(admin.get_rank())} of Dragonscale Castle \nUID: {admin.get_uid()}")
    except ValueError:
        bad_command(update, context)

    return ConversationHandler.END
