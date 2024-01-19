import logging
import telegram
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CommandHandler, CallbackContext, ExtBot, \
    JobQueue

BOT_TOKEN = ''
HISTORY_FILE: str = 'history.txt'


async def start(update: Update, context: ContextTypes):
    user_tag = f'<b>@{update.message.from_user.username}</b>'
    welcome_message = f'Привіт, {user_tag}!\nЯ телеграм бот.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message, parse_mode='HTML')


async def help(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='''Писати за допомогою @Uni000l'
    Команди
    /help
    /start
    /history''')


async def history(update: Update, context: ContextTypes):
    try:
        with open(HISTORY_FILE, 'r') as f:
            history_text = f.read()
        if history_text:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=history_text)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Історія повідомлень порожня.')
    except FileNotFoundError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Історія повідомлень не знайдена.')


def save_message_to_history(update: Update):
    if update.message.text:
        with open(HISTORY_FILE, 'a') as f:
            f.write(update.message.text + '\n')


async def unknown_command(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Не розумію команду. Спробуйте ще раз.')


async def unsupported_message(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='Вибачте, не підтримую надсилання таких повідомлень.',
                                   parse_mode='HTML')


async def non_text_message(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, this bot only accepts text messages.")


# noinspection PyGlobalUndefined
def main() -> None:
    global non_text_message
    application_builder = Application.builder()
    application_token = application_builder.token(BOT_TOKEN)
    application = application_token.build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    history_handler = CommandHandler('history', history)
    message_handler = MessageHandler(filters.Text, save_message_to_history)
    unknown_command_handler = MessageHandler(filters.Command, unknown_command)
    unsupported_message_handler = MessageHandler(
        filters.Text |
        filters._Audio |
        filters.Document |
        filters._Photo |
        filters.Sticker |
        filters._Video |
        filters._Voice |
        filters._VideoNote |
        filters._Contact |
        filters._Location |
        filters._Venue |
        filters._Game |
        filters._Invoice |
        filters._SuccessfulPayment |
        filters._Animation |
        filters._Poll |
        filters.Dice,
        unsupported_message
    )

    application.add_handler(history_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(message_handler)
    application.add_handler(unknown_command_handler)
    application.add_handler(unsupported_message_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
