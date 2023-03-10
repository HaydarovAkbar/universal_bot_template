from database import DatabaseDB
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from static_files.methods_files.basic_static_files import basic_menyu_txt, phone_number_batton_txt, basic_batton_txt
from settings.etc import BOT_USERNAME

database_db = DatabaseDB()


def phone_batton(lang='uz'):
    phone = KeyboardButton(phone_number_batton_txt[lang], request_contact=True)
    contact_key = ReplyKeyboardMarkup([[phone]], resize_keyboard=True)
    return contact_key


def language_batton():
    result = InlineKeyboardMarkup([[InlineKeyboardButton("🇺🇿 O'zbek tili 🇺🇿", callback_data='uz')],
                                   [InlineKeyboardButton("🇷🇺 Русский 🇷🇺", callback_data='ru')],
                                   [InlineKeyboardButton("🇺🇸 English 🇺🇸", callback_data='ru')]])
    return result


def basic_batton(lang='uz'):
    batton = ReplyKeyboardMarkup([
        [basic_batton_txt[lang]],
    ], resize_keyboard=True)
    return batton


def back_batton(lang='uz'):
    batton = ReplyKeyboardMarkup([
        [basic_menyu_txt[lang]],
    ], resize_keyboard=True)
    return batton
