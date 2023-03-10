from telegram.ext import CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from static_files import *
import telebot
from database.user_db import DatabaseDB
from settings import TOKEN

bot_help = telebot.TeleBot(TOKEN)
connection_db = DatabaseDB()


def channel_batton(user_id):
    values = connection_db.get_all_channel()
    batton = []
    for channel in values:
        name = channel[3]
        if bot_help.get_chat_member(channel[1], user_id).status != 'left':
            continue
        batton.append([InlineKeyboardButton(text=name, url=f'{channel[4]}')])
    batton.append([InlineKeyboardButton(text="A'zolikni tekshirib ko'rish ♻️", callback_data='check')])
    return InlineKeyboardMarkup(batton)


def is_not_subscribed(update: Update, context: CallbackContext):
    user_id = update.effective_chat.id
    connection_db.update_user_firstname(update.effective_user.first_name, user_id)
    context.bot.send_message(chat_id=user_id,
                             text="Botdan foydalanish uchun barcha kanallarimizga a'zo bo'ling",
                             reply_markup=channel_batton(user_id)
                             )
    return channel_members


def is_subscribed(channels, user_id):
    try:

        members = list(map(lambda ch: bot_help.get_chat_member(ch[0], user_id).status != 'left', channels))
        if not all(members):
            return False
        return True
    except Exception:
        return False


def check_is_subscribed(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'check':
        user = update.effective_chat
        channels = connection_db.get_all_channel_id()
        is_subscribed_ = is_subscribed(channels, user.id)
        if is_subscribed_ is False:
            query.delete_message(timeout=1)
            return is_not_subscribed(update, context)
        query.delete_message(timeout=1)
        # context.bot.send_message(chat_id=user.id, text="<b>👇 Qaysi fandan test ishlamoqchisiz tanlang ❔ 👇</b>",
        #                          parse_mode="HTML", reply_markup=all_category_batton())
        # return user_quize_start_command
