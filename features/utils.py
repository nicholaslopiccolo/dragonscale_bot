from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from telegram import (
    ReplyKeyboardRemove,
    Update
)

"""Use bad_comand to quit to an handler

bad_command receive Update and CallbackContext object as parameters
and return an ConversationHandler.END to end the handler.
REMEMBER to return the bad_command() function in the caller.
"""


def bad_command(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "bad command", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
