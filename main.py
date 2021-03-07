from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from auth import TOKEN
from handlers import handlers


def main(hs) -> None:
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    for handler in hs:
        dispatcher.add_handler(handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main(handlers)
