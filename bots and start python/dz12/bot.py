from telegram.ext import Application, MessageHandler, filters, CommandHandler
from func import *
from token_1 import *
from comand import *


def main() -> None:
    application_builder = Application.builder()
    application_token = application_builder.token(BOT_TOKEN)
    application = application_token.build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    history_handler = CommandHandler('history', history)

    message_handler = MessageHandler(filters.TEXT, save_message_to_history)
    unsupported_message_handler = MessageHandler(filters.ALL, unsupported_message)
    unknown_command_handler = MessageHandler(filters.Command, unknown_command)

    application.add_error_handler(error_handler)

    application.add_handler(history_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(message_handler)
    application.add_handler(unsupported_message_handler)
    application.add_handler(unknown_command_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
