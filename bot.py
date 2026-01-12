import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)

TOKEN = "8547377508:AAFNTQbe8zXzVJhD6_WS8Yfo2wI1H0Z19V4"
ADMIN_ID = 7854011227
