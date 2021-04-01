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


white_list = None


def init(permissions):
    global white_list
    white_list = permissions


def start(update: Update, context: CallbackContext) -> int:
    params = update.message.text.split()

    if len(params) != 2:
        return bad_command(update, context)

    try:
        cid = int(params[1])
        squad = white_list.get_squad(cid)
    except ValueError:
        return bad_command(update, context)

    print(squad)
    if not squad != -1:
        update.message.reply_text(f"player not found")
        return ConversationHandler.END

    context.user_data['player'] = squad

    p = player['player']
    r_name = white_list.get_rank_name(player['rank'])
    msg = f" Role: {r_name.capitalize()}\n Name: {p['name']}\n UID: {p['uid']}"

    is_you = ""

    if p['uid'] == update.message.from_user.id:
        is_you = "\n... YOURSELF"

    white_list.rm_user(context.user_data['player']['player']['uid'])

    update.message.reply_text(f"Removing...\n\n{msg}\n{is_you}")
