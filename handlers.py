from objects.permission import Permission

from telegram.ext import ConversationHandler
from telegram.ext import CommandHandler

import features.start as start
import features.admin.admins_list as admins_list
import features.admin.add_admin as add_admin
import features.admin.rm_admin as rm_admin

# rm_admin,
# add_squad,
# rm_squad,
# squads_list

white_list = None


def init():
    global white_list
    white_list = Permission()

    start.init(white_list)
    admins_list.init(white_list)
    add_admin.init(white_list)
    rm_admin.init(white_list)


# STEP 0 - INIT
init()

# STEP 1 - handlers (AKA features)
handlers = []

"""
/start - ask the user what action to perform
"""
handlers.append(
    CommandHandler('start', start.start, white_list.get_users_filter(0)))

"""
/admins_list - show admins in the bot
"""
handlers.append(
    CommandHandler('admins_list', admins_list.start, white_list.get_users_filter(8)))

"""
/add_admin - cvH add new admin by setting name, uid and permission type
"""
handlers.append(
    CommandHandler('add_admin', add_admin.start, white_list.get_users_filter(9)))

"""
/rm_admin - cvH remove admin from name or uid
"""
handlers.append(
    CommandHandler('rm_admin', rm_admin.start, white_list.get_users_filter(9)))
