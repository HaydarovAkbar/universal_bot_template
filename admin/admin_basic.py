from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardRemove
from keyboards.admin_keyboard import database_db, admin_batton, back_batton, \
    admin_list_batton, admin_channel_setting_batton, admin_batton_Akbar
from datetime import datetime
from static_files.admin_files.admin_basic_files import *
from methods.basic import start
from settings.etc import DEVELOPER


def admin(update: Update, context: CallbackContext):
    user = update.effective_user
    if database_db.check_admin(user.id):
        if user.id in DEVELOPER:
            update.message.reply_html("<code>Akbar xush kelibsiz</code>", reply_markup=admin_batton_Akbar())
            return 10
        update.message.reply_html("<code>Admin xush kelibsiz</code>", reply_markup=admin_batton())
        return 10
    else:
        return start(update, context)


def fallback_text(update, context):
    try:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Botdan foydalanish uchun botni yangilang /start")
        return 3
    except Exception as e:
        print(e)


def all_user(update, context):
    user = update.effective_chat
    user_lang = database_db.get_user_if_id(user.id)[4]
    user_count = database_db.get_user_all_count()[0]
    all_user_db = database_db.get_user_50()
    all_text = "{:<1} || {:<8} || {:<23}\n\n".format("Number", "Name", "Username")
    for item in all_user_db:
        try:
            all_text += "{:<1}). || {:<8} || @{:<23}\n".format(item[0], item[2], item[3])
        except:
            pass
    context.bot.send_message(chat_id=user.id,
                             text=f"Botni foydalanuvchilar soni: {user_count}")
    context.bot.send_message(chat_id=user.id,
                             text=all_text,
                             reply_markup=admin_batton(user_lang))
    return 10


def developer(update, context):
    try:
        now = datetime.today()
        res = (now - datetime(2000, 11, 25)).days // 365 + 1
        a = context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"<b>About developer:\n\nFull Name: Akbar Haydarov\nAge: {res}\nMa'lumoti: TATU 3-kurs\nUsername: @Akbar_TUIT\n...!</b>",
                                     parse_mode="HTML")
    except Exception as e:
        print(e)


# Admin qo'shish funkisayalari
def add_admin(update: Update, context: CallbackContext):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[4]
    update.message.reply_html(text=get_new_admin_chat_id.get(user_lang),
                              reply_markup=back_batton(user_lang))
    return 1512


def get_new_admin_chat_ID(update, context):
    try:
        admin_id = update.message.text
        user = update.effective_user
        user_lang = database_db.get_user_if_id(user.id)[4]
        if admin_id.isdigit():
            context.chat_data['admin_chat_id'] = int(admin_id)
            context.bot.send_message(chat_id=user.id,
                                     text=get_new_admin_username_txt.get(user_lang),
                                     parse_mode="HTML",
                                     reply_markup=back_batton(user_lang))
            return 13
        else:
            context.bot.send_message(chat_id=user.id,
                                     text="Siz ID kiritmadingiz:(",
                                     reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Xatolik yuz berdi Dasturchi bilan bog'lanishni maslahat beraman!")
        return 10


def get_new_admin_username(update, context):
    try:
        A = database_db.insert_admin(context.chat_data['admin_chat_id'], update.message.text)
        if A:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Yangi admin Muvafaqiyatli qo'shildi:)!")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Yangi admin qo'shilmadi:)!")
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Xatolik yuz berdi Dasturchi bilan bog'lanishni maslahat beraman!")
    return 10


def admin_lists(update, context):
    try:
        name = update.message.from_user.first_name
        admin_text = name + "Adminlar ro'yxati:)\n\n"
        for i in database_db.get_admin_list():
            # count = len(database_db.get_link_userID(i[2]))
            admin_text += f"{i[0]}. chat_id={i[1]}  @{i[2]}\n"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=admin_text,
                                 reply_markup=back_batton())
    except Exception as e:
        print(e)
    return 10


def admin_delete(update, context):
    try:
        user = update.effective_user
        user_lang = database_db.get_user_if_id(user.id)[4]
        update.message.reply_html(text=admin_delete_txt.get(user_lang), reply_markup=admin_list_batton())
    except Exception as e:
        print(e)
    return 15


def admin_delete1(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        query = update.callback_query
        database_db.delete_admin(query.data)
        user_lang = database_db.get_user_if_id(user.id)[4]
        query.delete_message(timeout=1)
        context.bot.send_message(chat_id=user.id,
                                 text=admin_delete_succesfuly_txt.get(user_lang),
                                 parse_mode="HTML",
                                 reply_markup=admin_batton(user_lang))
    except Exception as e:
        print(e)
    return 10


def back(update: Update, context: CallbackContext):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[4]
    if database_db.check_admin(user.id):
        pass


""" 
Find user functions
"""


def find_user(update: Update, context: CallbackContext):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[4]
    update.message.reply_html(text=find_user_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 18


def find_user_with_name(update: Update, context: CallbackContext):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[4]
    text = update.message.text
    all_user_db = database_db.find_user_with_name(text)
    all_text = "{:<1} || {:<8} || {:<23}\n\n".format("Number", "Name", "Username")
    try:
        for item in all_user_db:
            try:
                all_text += "{:<1}). || {:<8} || @{:<23}\n".format(item[0], item[1], item[3])
            except:
                pass
    except Exception:
        pass
    update.message.reply_text(text=all_text, reply_markup=admin_batton(user_lang))
    return 10


def add_channel(update: Update, context: CallbackContext):
    update.message.reply_html(add_channel_id_txt.get("uz"), reply_markup=back_batton())
    return 1300


def add_channel_id(update: Update, context: CallbackContext):
    channel_id = update.message.text
    if not channel_id[1:].isdigit():
        channel_id_bug_txt = {
            "uz": f"Siz kiritgan Channel ID: 🚫 <code>{channel_id}</code> Xato\n\n<b>Siz Channel ID raqamini kiritishingiz kerak edi </b>",
            "ru": f"Siz kiritgan Channel ID: 🚫 <code>{channel_id}</code> Xato\n\n<b>Siz Channel ID raqamini kiritishingiz kerak edi </b>",
            "en": f"Siz kiritgan Channel ID: 🚫 <code>{channel_id}</code> Xato\n\n<b>Siz Channel ID raqamini kiritishingiz kerak edi </b>",
        }
        update.message.reply_html(channel_id_bug_txt.get('uz'))
        return 1300
    context.chat_data['channel_id'] = channel_id
    update.message.reply_html(add_channel_name_txt.get("uz"), reply_markup=back_batton())
    return 1301


def add_channel_name(update: Update, context: CallbackContext):
    channel_name = update.message.text
    context.chat_data['channel_name'] = channel_name
    update.message.reply_html(add_channel_url_txt.get("uz"), reply_markup=back_batton())
    return 1302


def add_channel_url(update: Update, context: CallbackContext):
    channel_url = update.message.text
    if not 'https://t.me/' in channel_url:
        channel_id_bug_txt = {
            "uz": f"Siz kiritgan Kanal linki: 🚫 <code>{channel_url}</code> Xato\n\n<b>Siz Kanal linkini kiritishingiz kerak edi: https://t.me/HaydarovAkbar </b>",
            "ru": f"Siz kiritgan Kanal linki: 🚫 <code>{channel_url}</code> Xato\n\n<b>Siz Kanal linkini kiritishingiz kerak edi: https://t.me/HaydarovAkbar </b>",
            "en": f"Siz kiritgan Kanal linki: 🚫 <code>{channel_url}</code> Xato\n\n<b>Siz Kanal linkini kiritishingiz kerak edi: https://t.me/HaydarovAkbar </b>",
        }
        update.message.reply_html(channel_id_bug_txt.get('uz'))
        return 1302
    channel_name, channel_id = context.chat_data['channel_name'], context.chat_data['channel_id']
    now = datetime.now()
    database_db.add_channel(channel_id, now, 1, channel_name, channel_url)
    update.message.reply_html(add_channel_succesfuly.get("uz"), reply_markup=back_batton())
    return 1000


def status_channels(update, context):
    """Channels status update"""
    data_channel = database_db.get_all_channel()
    data_text = "Barcha kanallar ro'yxati bilan tanishing:\n\n"
    for item in data_channel:
        status_name = {'1': "<code>✅ Aktiv</code>", '0': "<code>❌ Passiv</code>"}
        data_text += f"{item[0]}). <code>NAME</code>: {item[4]} <code>ID</code>: {item[1]}\n <code>DATE</code> {item[2]} 🔹 <code>STATUS</code>: {status_name.get(item[3], 'nomalum')}\n"
    update.message.reply_html(data_text)
    update.message.reply_html(channel_status_text.get('uz'), reply_markup=back_batton())
    return 1305


def status_edit_channel(update: Update, context: CallbackContext):
    message_ = update.message.text
    data = database_db.get_channel_where_id(message_)
    context.chat_data['channel_edit_id'] = data[0]
    data_text = "O'zgartirish turini tanlang"
    update.message.reply_text(data_text, reply_markup=admin_channel_setting_batton())
    return 1306


def status_edit_channel_id(update: Update, context: CallbackContext):
    data = database_db.get_channel_where_id(context.chat_data['channel_edit_id'])
    context.chat_data['channel_edit_id'] = data[0]
    data_text = f"{data[1]}\n{data[3]}\n{data[4]}\n\n\n Kanalni xuddi shunday akslantiring"
    update.message.reply_text(data_text, reply_markup=back_batton())
    return 1306


def get_channel_update_text(update: Update, context: CallbackContext):
    msg_text = update.message.text
    channel_id = context.chat_data['channel_edit_id']
    text_data = msg_text.split('\n')
    database_db.update_channel(text_data[0], text_data[1], text_data[2], channel_id)
    update.message.reply_html(update_channel_data_succesfuly.get('uz', '!'), reply_markup=back_batton())
    return 10


def channel_status_update_text(update: Update, context: CallbackContext):
    channel_id = context.chat_data['channel_edit_id']
    channel_data = database_db.get_channel_where_id(channel_id)
    status = '0' if channel_data[6] == '1' else '1'
    database_db.update_channel_status(channel_id, status)
    update.message.reply_html(update_channel_data_succesfuly.get('uz', '!'), reply_markup=back_batton())
    return 10
