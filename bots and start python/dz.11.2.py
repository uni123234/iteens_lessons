import logging
import telegram
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CommandHandler, CallbackContext, ExtBot, \
    JobQueue

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

BOT_TOKEN = ''
HISTORY_FILE: str = 'history.txt'


async def start(update: Update, context: ContextTypes):
    if update.message.text:
        with open(HISTORY_FILE, 'a') as f:
            f.write(update.message.text + '\n')
    user_tag = f'<b>@{update.message.from_user.username}</b>'
    welcome_message = f'Привіт, {user_tag}!\nЯ телеграм бот.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message, parse_mode='HTML')


async def help(update: Update, context: ContextTypes):
    if update.message.text:
        with open(HISTORY_FILE, 'a') as f:
            f.write(update.message.text + '\n')
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


async def save_message_to_history(update: Update, context: CallbackContext):
    if update.message.text:
        with open(HISTORY_FILE, 'a') as f:
            f.write(update.message.text + '\n')


async def unknown_command(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Неизвестная команда. Я не понимаю вас.")


async def unsupported_message(update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='Вибачте, не підтримую надсилання таких повідомлень.',
                                   parse_mode='HTML')


async def error_handler(update: Update, context: CallbackContext):
    logging.error(msg="Виникла помилка", exc_info=context.error)


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
    unsupported_message_handler = MessageHandler(filters.ALL,  unsupported_message)

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
