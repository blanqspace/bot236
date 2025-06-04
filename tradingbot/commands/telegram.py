from threading import Thread
from typing import Callable
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from tradingbot.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


class TelegramCommand(Thread):
    """Telegram bot interface."""

    def __init__(self, handler: Callable[[str], None]):
        super().__init__(daemon=True)
        self.handler = handler

    def run(self):
        if not TELEGRAM_TOKEN:
            return
        updater = Updater(TELEGRAM_TOKEN, use_context=True)
        dp = updater.dispatcher

        def generic(update: Update, context: CallbackContext):
            text = update.message.text
            self.handler(text)

        dp.add_handler(CommandHandler("buy", generic))
        dp.add_handler(CommandHandler("pause", generic))
        updater.start_polling()
        updater.idle()
