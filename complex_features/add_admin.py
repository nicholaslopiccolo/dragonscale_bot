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


ROLE, UID, NAME = range(3)


def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = []
    for el in white_list.rank_map:
        reply_keyboard.append([el])
    update.message.reply_text(
        'Choose role type:',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True),
    )

    return ROLE


def role(update: Update, context: CallbackContext) -> int:
    role = update.message.text
    if role not in white_list.rank_map:
        return start(update, context)

    context.user_data['role'] = role

    update.message.reply_text(
        'Insert UserId of the admin:', reply_markup=ReplyKeyboardRemove())

    return UID


def user_id(update: Update, context: CallbackContext) -> int:
    try:
        context.user_data['uid'] = int(update.message.text)
    except ValueError:
        update.message.reply_text(
            'Insert UserId of the admin:', reply_markup=ReplyKeyboardRemove())
        return UID
    update.message.reply_text('Last but not least admin name:')

    return NAME


def name(update: Update, context: CallbackContext) -> int:
    try:
        int(update.message.text)
        update.message.reply_text('Not a number!!')
        update.message.reply_text('Last but not least admin name:')
        return NAME
    except ValueError:
        admin = {
            'name': update.message.text,
            'uid': context.user_data['uid'],
            'role': context.user_data['role']
        }
        white_list.add_user(admin['uid'], white_list.rank_map.index(
            admin['role']), admin['name'])

        update.message.reply_text(
            f"Now {admin['name']} is a {admin['role']} of Dragonscale Castle\n UID: {admin['uid']}")

        return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    update.message.reply_text('OK', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END
