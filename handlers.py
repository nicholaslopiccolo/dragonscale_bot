from objects.core import core

from telegram.ext import ConversationHandler
from telegram.ext import CommandHandler

import features.start as start
import features.help as help

import features.admin.admins_list as admins_list
import features.admin.admin_roles as admin_roles
import features.admin.add_admin as add_admin
import features.admin.rm_admin as rm_admin

import features.squad.squads_list as squads_list
import features.squad.add_squad as add_squad
import features.squad.rm_squad as rm_squad

App = core()


def init(app):
    white_list = app.get_white_list()

    start.init(white_list)
    admins_list.init(white_list)
    admin_roles.init(white_list)
    add_admin.init(app)
    rm_admin.init(app)

    squads_list.init(app)
    add_squad.init(app)
    rm_squad.init(app)


# STEP 0 - INIT
init(App)

# STEP 1 - handlers (AKA features)
white_list = App.get_white_list()


"""
/start - ask the user what action to perform
"""
App.add_handler(
    CommandHandler('start', start.start, white_list.get_users_filter(0)))

"""
/help - print help string
"""
App.add_handler(
    CommandHandler('help', help.start, white_list.get_users_filter(0)))

#   Admin

"""
/admins_list - show admins in the bot
"""
App.add_handler(
    CommandHandler('admins_list', admins_list.start, white_list.get_users_filter(8)))

"""
/admins_roles - show admin possible roles
"""
App.add_handler(
    CommandHandler('admin_roles', admin_roles.start, white_list.get_users_filter(7)))


"""
/add_admin - add new admin by setting name, uid and permission type
"""
App.add_handler(
    CommandHandler('add_admin', add_admin.start, white_list.get_users_filter(9)))

"""
/rm_admin - remove admin from uid
"""
App.add_handler(
    CommandHandler('rm_admin', rm_admin.start, white_list.get_users_filter(9)))

#   Squad
"""
/squads_list - show squads in the castle
"""
App.add_handler(
    CommandHandler('squads_list', squads_list.start, white_list.get_users_filter(8)))

# show my squad?

"""
/add_squad - add new squad by setting chat id and name
"""
App.add_handler(
    CommandHandler('add_squad', add_squad.start, white_list.get_users_filter(9)))

"""
/rm_squad - remove squad form chat id
"""
App.add_handler(
    CommandHandler('rm_squad', rm_squad.start, white_list.get_users_filter(9)))


handlers = App.get_handlers()
