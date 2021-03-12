from telegram import ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext


white_list = None


def init(permissions):
    global white_list
    white_list = permissions


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    player = white_list.get_player(user.id)
    if player != -1:
        update.message.reply_text(
            f"Hi {user.first_name}!\n{white_list.get_rank_name(player['rank'])} of Dragonscale castle", reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(
            f"Hi {user.first_name}!\n{white_list.get_rank_name(0)} of Dragonscale castle", reply_markup=ReplyKeyboardRemove())
