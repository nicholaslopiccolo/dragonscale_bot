from telegram import (
    ReplyKeyboardRemove,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update
)
from telegram.ext import CallbackContext


white_list = None


def init(permissions):
    global white_list
    white_list = permissions


def start(update: Update, context: CallbackContext):
    msg = ""

    for (rank, value) in reversed(list(enumerate(white_list.ranks))):
        msg += f"{white_list.get_rank_name(rank).capitalize()}:\n"
        if len(value['players']) > 0:
            for (i, player) in enumerate(value['players']):
                msg += f" {player['name']}: {player['uid']}\n"
        else:
            msg += "  None\n"
        msg += "\n"

    update.message.reply_text(msg)
    """
    keyboard = []

    for (rank, value) in enumerate(white_list.ranks):
        if len(value['players']) > 0:
            for (i, player) in enumerate(value['players']):
                res = []
                res.append(InlineKeyboardButton(
                    f"{white_list.rank_map[rank]} {player['name']}", callback_data=player['uid']))
                keyboard.append(res)

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Here your list:', reply_markup=reply_markup)
    """
