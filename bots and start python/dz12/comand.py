from telegram.ext import ContextTypes, CallbackContext
from telegram import Update
from func import *


async def start(update: Update, context: ContextTypes):
    save_message_to_history(update, context)
    user_tag = f'<b>@{update.message.from_user.username}</b>'
    welcome_message = f'Привіт, {user_tag}!\nЯ телеграм бот.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message, parse_mode='HTML')


async def help(update: Update, context: ContextTypes):
    save_message_to_history(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='''Писати за допомогою @Uni000l'
    Команди
    /help
    /start
    /history''')
