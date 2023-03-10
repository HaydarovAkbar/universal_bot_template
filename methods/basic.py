from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardRemove
from static_files.methods_files import *
from telegram import ParseMode
from keyboards.admin_keyboard import admin_list_batton
from methods.check_channel import is_subscribed, is_not_subscribed
from datetime import datetime
from database.user_db import DatabaseDB

database_db = DatabaseDB()


def start(update: Update, context: CallbackContext):
    user = update.effective_chat
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    if not database_db.get_user_if_id(user.id):
        _ = database_db.insert_start_user(user.id, user.username, now, user.first_name)
    channels = database_db.get_all_channel_id()
    is_subscribed_ = is_subscribed(channels, user.id)
    if is_subscribed_ is False:
        return is_not_subscribed(update, context)
    user_id = update.effective_chat.id
    database_db.update_user_firstname(update.effective_user.first_name, user_id)
    context.bot.send_message(chat_id=user.id, text=welcome_user_txt.get('uz'), parse_mode="HTML")
    return


def user_txt_bug(update: Update, context: CallbackContext):
    user = update.effective_user
    channels = database_db.get_all_channel_id()
    is_subscribed_ = is_subscribed(channels, user.id)
    if is_subscribed_ is False:
        return is_not_subscribed(update, context)
    user_db = database_db.get_user_if_id(user.id)
    na = user_txt.get(user_db[4])
    text = f"[{na}](tg://user?id={user.id}) " + back_user_not_html_form_txt.get(user_db[4])
    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN_V2)
    return 1


def back_user(update, context):
    user = update.effective_user
    channels = database_db.get_all_channel_id()
    is_subscribed_ = is_subscribed(channels, user.id)
    if is_subscribed_ is False:
        return is_not_subscribed(update, context)
    # if database_db.check_admin(user.id):
    #     if user.id == 758934089:
    #         update.message.reply_html("<code>Akbar xush kelibsiz</code>", reply_markup=admin_batton_Akbar())
    #         return 10
    #     update.message.reply_html("<code>Admin xush kelibsiz</code>", reply_markup=admin_batton())
    #     return 10
    context.bot.send_message(chat_id=user.id, text="<code>Asosiy menyuga qaytdik</code>",
                             parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
    # context.bot.send_message(chat_id=user.id, text=welcome_user_txt.get('uz'),
    #                          parse_mode="HTML", reply_markup=all_category_batton())
    return 1