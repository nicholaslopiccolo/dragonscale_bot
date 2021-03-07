from operator import itemgetter
from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update
)
from telegram.ext import (
    Updater,
    Filters,
    ConversationHandler,
    CallbackContext,
)


white_list = None


def init(permissions):
    global white_list
    white_list = permissions


NorUID, CONF = range(2)


def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'REMOVE MEMBER\n\nPlease send me name or uid:', reply_markup=ReplyKeyboardRemove())

    return NorUID


def name_or_uid(update: Update, context: CallbackContext) -> int:
    # UID
    try:
        uid = int(update.message.text)
        player = white_list.get_player(uid)
# NAME
    except ValueError:
        name = update.message.text
        player = white_list.get_player_by_name(name)

    if not player != -1:
        update.message.reply_text(f"player not found")
        return ConversationHandler.END

    context.user_data['player'] = player

    p = player['player']
    r_name = white_list.get_rank_name(player['rank'])
    msg = f"Role: {r_name.capitalize()}\nName: {p['name']}\nUID: {p['uid']}"

    is_you = ""

    if p['uid'] == update.message.from_user.id:
        is_you = "...DELETING YOURSELF"

    update.message.reply_text(
        f"{msg}\n\nAre you sure?"+is_you, reply_markup=ReplyKeyboardMarkup(
            [["Yes", "No"]], one_time_keyboard=True))

    return CONF


def conf(update: Update, context: CallbackContext) -> int:
    if update.message.text == "Yes":
        white_list.rm_user(context.user_data['player']['player']['uid'])
        update.message.reply_text("Ok")
    else:
        update.message.reply_text("Aborted")

    return ConversationHandler.END
