from objects.permission import Permission

from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext)
from telegram.ext import CommandHandler
import complex_features.add_admin as add_admin
import complex_features.rm_admin as rm_admin

# rm_admin,
# add_squad,
# rm_squad,
# squads_list


# STEP 0 - INIT
white_list = Permission()
add_admin.init(white_list)
rm_admin.init(white_list)

# STEP 1 - handlers (AKA features)


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    player = white_list.get_player(user.id)
    if player != -1:
        update.message.reply_text(
            f"Hi {user.first_name}!\n{white_list.get_rank_name(player['rank'])} of Dragonscale castle", reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(
            f"Hi {user.first_name}!\n{white_list.get_rank_name(0)} of Dragonscale castle", reply_markup=ReplyKeyboardRemove())


def admins_list(update: Update, context: CallbackContext):
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


handlers = []

# /start - ask the user what action to perform
handlers.append(CommandHandler('start', start, white_list.get_users_filter(0)))
# /admins_list - show admins in the bot
handlers.append(CommandHandler(
    'admins_list', admins_list, white_list.get_users_filter(9)))
# /add_admin - cvH add new admin by setting name, uid and permission type
handlers.append(ConversationHandler(
    entry_points=[CommandHandler(
        'add_admin', add_admin.start, white_list.get_users_filter(9))],
    states={
        add_admin.ROLE: [MessageHandler(Filters.text, add_admin.role)],
        add_admin.UID: [MessageHandler(Filters.text, add_admin.user_id)],
        add_admin.NAME: [MessageHandler(Filters.text, add_admin.name)]
    },
    fallbacks=[CommandHandler('start', start)]))
# /rm_admin - cvH remove admin from name or uid
handlers.append(ConversationHandler(
    entry_points=[CommandHandler(
        'rm_admin', rm_admin.start, white_list.get_users_filter(9))],
    states={
        rm_admin.NorUID: [MessageHandler(Filters.text, rm_admin.name_or_uid)],
        rm_admin.CONF: [MessageHandler(Filters.text, rm_admin.conf)]
    },
    fallbacks=[CommandHandler('start', start)]))
