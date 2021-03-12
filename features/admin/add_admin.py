from ..utils import bad_command
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

#   /add_admin role uid name


def start(update: Update, context: CallbackContext) -> int:
    params = update.message.text.split()
    # print(params)
    if len(params) != 4:
        return bad_command(update, context)
    # try:

    role = int(params[1])
    uid = int(params[2])
    name = params[3]

    admin = {
        'name': name,
        'uid': uid,
        'role': role
    }
    white_list.add_user(admin['uid'], admin['role'], admin['name'])

    update.message.reply_text(
        f"{admin['name'].capitalize()} is a brave { white_list.get_rank_name(admin['role'])} of Dragonscale Castle \nUID: {admin['uid']}")

    return ConversationHandler.END
    # except ValueError:
    #    return bad_command(update, context)
