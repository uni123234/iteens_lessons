from telegram.ext import ContextTypes, CallbackContext
from telegram import Update
import logging

HISTORY_FILE: str = 'history.txt'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def history(update: Update, context: ContextTypes):
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            history_text = f.read()
        if history_text:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=history_text)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Історія повідомлень порожня.')
    except FileNotFoundError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Історія повідомлень не знайдена.')


def save_message_to_history(update: Update, context: CallbackContext):
    if update.message.text:
        logger.info(f"Повідомлення користувача: {update.message.text}")
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(update.message.text + '\n')


async def unknown_command(update: Update, context: CallbackContext):
    if update.message.text:
        logger.info(f'Отримано невідому команду: {update.message.text}')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Неизвестная команда. Я не понимаю вас.",
    )


async def unsupported_message(update: Update, context: CallbackContext):
    if update.message.text:
        logger.info(
            f'Отримано непідтримуване повідомлення: {update.message.text}')
    error_message = "Вибачте, не підтримую надсилання таких повідомлень.\n\n" \
        "Доступні команди:\n" \
        "/help - Показати список команд\n" \
        "/start - Почати спілкування\n" \
        "/history - Показати історію повідомлень"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=error_message,
        parse_mode="HTML",
    )


async def error_handler(update: Update, context: CallbackContext):
    logging.error(msg="Виникла помилка", exc_info=context.error)
