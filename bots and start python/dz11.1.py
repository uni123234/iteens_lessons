import logging
import telegram
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CommandHandler, CallbackContext, ExtBot, \
    JobQueue

BOT_TOKEN = ''
HISTORY_FILE = 'history.txt'


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


def save_message(update: Update, _: CallbackContext):
    if update.message.text:
        with open(HISTORY_FILE, 'a') as f:
            f.write(update.message.text + '\n')


def main() -> None:
    application_builder = Application.builder()
    application_token = application_builder.token(BOT_TOKEN)
    application = application_token.build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    history_handler = CommandHandler('history', history)
    message_handler = MessageHandler(filters.Text, save_message)

    application.add_handler(history_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(message_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
