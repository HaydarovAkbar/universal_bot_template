from database import DatabaseDB
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from static_files.admin_files.admin_basic_files import *
from static_files.admin_files.rek_files import *
from settings.etc import BOT_USERNAME

database_db = DatabaseDB()


def back_batton(lang='uz'):
    batton = ReplyKeyboardMarkup([
        [back_txt[lang]],
    ], resize_keyboard=True)
    return batton


def admin_list_batton():
    admins = []
    for item in database_db.get_admin_list():
        admins.append([InlineKeyboardButton(str(item[2]) + "-" + str(item[1]), callback_data=item[1])])
    return InlineKeyboardMarkup(admins)


def admin_batton(lang='uz'):
    bt_txt = admin_basic_batton_txts[lang]
    _back_txt = basic_menyu_txt.get(lang)
    batton = ReplyKeyboardMarkup([
        [bt_txt[0], bt_txt[1], bt_txt[2]],
        [bt_txt[3], bt_txt[4]],  # bt_txt[5]
        [bt_txt[7], bt_txt[8]],  # bt_txt[6],
        [bt_txt[9], _back_txt]  # _back_txt
    ], resize_keyboard=True)
    return batton


def admin_batton_Akbar(lang='uz'):
    bt_txt = admin_basic_batton_txts[lang]
    _back_txt = basic_menyu_txt.get(lang)
    batton = ReplyKeyboardMarkup([
        [bt_txt[0], bt_txt[1], bt_txt[2]],
        [bt_txt[3], bt_txt[4], bt_txt[10]],  # bt_txt[5]
        [bt_txt[7], bt_txt[8], bt_txt[11]],  # bt_txt[6],
        [bt_txt[9], bt_txt[12], _back_txt]  # _back_txt
    ], resize_keyboard=True)
    return batton


def admin_rek_batton(lang='uz'):
    bt_txt = admin_rek_batton_txt[lang]
    batton = ReplyKeyboardMarkup([
        [bt_txt[0], bt_txt[1]],
        [bt_txt[2], bt_txt[3]],
        [bt_txt[4], bt_txt[5]]
    ], resize_keyboard=True)
    return batton


def admin_rek_type_batton(lang='uz'):
    bt_txt = reklama_type_all_txt[lang]
    batton = ReplyKeyboardMarkup([
        [bt_txt[0]],
        [bt_txt[1]],
        [bt_txt[2]]
    ], resize_keyboard=True)
    return batton


def help_massiv(massiv):
    len_ = len(massiv)
    name, link = [], []
    for item in range(0, len_):  # 0,1,2,3
        if item % 2 == 0:
            name.append(massiv[item])
        else:
            link.append(massiv[item])
    return [name, link]


def link_batton(data=None):
    massiv = help_massiv(data)
    massiv_len, batton, inline, k = len(massiv[0]), [], [], 1
    if massiv_len > 5:
        k = 2
    elif massiv_len > 2:
        k = 1
    else:
        k = 0
    for item in range(massiv_len):
        if len(inline) >= k:
            if k == 0 and not inline:
                inline.append(InlineKeyboardButton(text=massiv[0][item], url=f'{massiv[1][item]}'))
                continue
            inline.append(InlineKeyboardButton(text=massiv[0][item], url=f'{massiv[1][item]}'))
            batton.append(inline)
            inline = []
        else:
            inline.append(InlineKeyboardButton(text=massiv[0][item], url=f'{massiv[1][item]}'))
    batton.append(inline)
    reply_markup = InlineKeyboardMarkup(batton)
    return reply_markup


def admin_channel_setting_batton(lang='uz'):
    admin_channel_setting = ReplyKeyboardMarkup([
        [text_channel_update_txt],
        [status_channel_update_txt],
        [back_txt.get(lang)]],
        resize_keyboard=True)
    return admin_channel_setting


def friend_url_batton(chat_id):
    batton = [[InlineKeyboardButton(text=friend_url_batton_txt,
                                    url=f"https://telegram.me/share/url?url={BOT_USERNAME}?start={chat_id}&text={friend_url_txt}")]]
    return InlineKeyboardMarkup(batton)
