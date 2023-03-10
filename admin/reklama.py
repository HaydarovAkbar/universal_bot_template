from telegram.ext import CallbackContext
from telegram import Update
from datetime import datetime
from keyboards.admin_keyboard import *
from static_files.admin_files.rek_files import *
import random
from time import sleep


def text_reklama_to_bot(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        user_lang = database_db.get_user_if_id(user.id)[4]
        context.bot.send_message(chat_id=user.id,
                                 text=text_reklama_add_txt.get(user_lang),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
    return 16


def text_reklama_to_db(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        user_lang = database_db.get_user_if_id(user.id)[4]
        text = update.message.text
        database_db.insert_text_reklama(text, datetime.now().strftime("%Y-%m-%d %H:%M"))
        context.bot.send_message(chat_id=user.id,
                                 text=text_reklama_succesfuly_txt.get(user_lang),
                                 parse_mode="HTML",
                                 reply_markup=admin_batton(user_lang))
    except Exception as e:
        print(e)
    return 10


def text_reklama_deactivation(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        user_lang = database_db.get_user_if_id(user.id)[4]
        random_number = random.randint(10000, 1000000)
        random_txt = {
            "uz": f"<b>Rekamani faolsizlantirish uchun <code>{random_number}</code>-kodni kiriting✅</b>",
            "ru": f"<b>Введите <code>{random_number}</code>, чтобы деактивировать тег ✅</b>",
            "en": f"<b>Enter <code>{random_number}</code> to deactivate the tag ✅</b>",
        }
        context.chat_data['random'] = random_number
        context.bot.send_message(chat_id=user.id,
                                 text=random_txt.get(user_lang),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
    return 17


def text_reklama_deactivation_succesfuly(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        user_lang = 'uz'
        if update.message.text == str(context.chat_data['random']):
            db_rek = database_db.get_rek_1()
            database_db.update_reklama(db_rek[0])
            context.bot.send_message(chat_id=user.id,
                                     text=text_reklama_deactivate_succesfuly_txt.get(user_lang),
                                     parse_mode="HTML",
                                     reply_markup=admin_batton(user_lang))
        else:
            context.bot.send_message(chat_id=user.id,
                                     text=random_number_bug_txt.get(user_lang),
                                     parse_mode="HTML",
                                     reply_markup=back_batton(user_lang))
            return 17
    except Exception as e:
        print(e)
    return 10


def reklama(update, context):
    # user_lang = database_db.get_user_if_id(user.id)[4]
    user_lang = 'uz'
    update.message.reply_html(text=you_choose_batton_rek_txt.get(user_lang),
                              reply_markup=admin_rek_type_batton(user_lang))
    return 25


def reklama_type(update, context):
    # user_lang = database_db.get_user_if_id(user.id)[4]
    user_lang = 'uz'
    update.message.reply_html(text=reklama_get_inline_batton_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 22


# def rek_text1(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id,
#                              text="<b>Text Faylni jo'natishingiz mumkin!</b>",
#                              parse_mode="HTML",
#                              reply_markup=about)
#     return 8
#
#
# def rek(update, context):
#     user_id = update.message.from_user.id
#     text = update.message.text
#     if user_id in [s[2] for s in database_db.get_admin()]:
#         s = 0
#         for item in database_db.get_id():
#             try:
#                 context.bot.send_message(chat_id=item[0], text=text + "\n\n    @kerakli_linklar_bot")
#                 s += 1
#             except Exception as e:
#                 print(e)
#         context.bot.send_message(chat_id=user_id,
#                                  text=f"Jo'natgan  xabaringiz {s}-ta userga bordi!",
#                                  reply_markup=about)
#         return 2
#     else:
#         context.bot.send_message(chat_id=user_id,
#                                  text=f"Uzr sizni tanimadim🧐",
#                                  reply_markup=about)
#     return 1


def rek_photo1(update, context):
    user_lang = 'uz'
    update.message.reply_html(text=reklama_get_photo_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 21


def rek_video1(update, context):
    user_lang = 'uz'
    update.message.reply_html(text=reklama_get_video_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 21


def rek_voice1(update, context):
    user_lang = 'uz'
    update.message.reply_html(text=reklama_get_voice_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 21


def rek_audio1(update, context):
    user_lang = 'uz'
    update.message.reply_html(text=reklama_get_audio_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 21


def rek_text1(update, context):
    user_lang = 'uz'
    update.message.reply_html(text=reklama_get_text_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 21


def get_forward_photo(update: Update, context: CallbackContext):
    photo, caption = update.message.photo[-1].file_id, update.message.caption
    forward_from_id = update.message.forward_from_chat.id if not update.message.forward_from_chat is None else update.message.forward_from.id
    c = 0
    if context.chat_data['battons']:
        for user in database_db.get_user_all():
            try:
                update.message.bot.send_photo(chat_id=user[1],
                                              photo=photo,
                                              # from_chat_id=forward_from_id,
                                              caption=caption,
                                              disable_notification=False,
                                              reply_markup=link_batton(context.chat_data['battons']))
                c += 1
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_all():
            try:
                context.bot.send_photo(chat_id=user[1],
                                       photo=photo,
                                       # from_chat_id=forward_from_id,
                                       caption=caption)
                c += 1
            except Exception as e:
                print(e)
    context.bot.send_message(chat_id=758934089, text=f"XABAR {c}-ta foydalanuvchiga bordi")
    # update.message.bot.forward_message(chat_id=update.message.chat.id, from_chat_id='@' + channel_username, message_id=message_id)
    # context.bot.send_photo(chat_id=user.id, photo=photo, from_chat_id=forward_from_id, caption=caption,
    #                        reply_markup=link_batton())
    # update.message.reply_html(text=reklama_get_inline_batton_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 10


def get_forward_video(update: Update, context: CallbackContext):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[4]
    video, caption = update.message.video.file_id, update.message.caption
    forward_from_id = update.message.forward_from_chat.id if update.message.forward_from is None else update.message.forward_from.id
    context.chat_data['video'], context.chat_data['forward_from_id'] = video, forward_from_id
    context.chat_data['caption'] = caption
    update.message.reply_html(text=reklama_get_inline_batton_txt.get(user_lang),
                              reply_markup=back_batton(user_lang))
    return 10


def get_forward_audio(update: Update, context: CallbackContext):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[4]
    audio, caption = update.message.audio.file_id, update.message.caption
    forward_from_id = update.message.forward_from_chat.id if update.message.forward_from is None else update.message.forward_from.id
    context.chat_data['audio'], context.chat_data['forward_from_id'] = audio, forward_from_id
    context.chat_data['caption'] = caption
    update.message.reply_html(text=reklama_get_inline_batton_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 10


def get_forward_voice(update: Update, context: CallbackContext):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[4]
    voice, caption = update.message.voice.file_id, update.message.caption
    forward_from_id = update.message.forward_from_chat.id if update.message.forward_from is None else update.message.forward_from.id
    context.chat_data['voice'], context.chat_data['forward_from_id'] = voice, forward_from_id
    context.chat_data['caption'] = caption
    update.message.reply_html(text=reklama_get_inline_batton_txt.get(user_lang),
                              reply_markup=back_batton(user_lang))
    return 10
    # update.message.bot.forward_message(chat_id=update.message.chat.id, from_chat_id='@' + channel_username, message_id=message_id)


def send_aktiv_user_to_admins(update: Update, context: CallbackContext):
    all_user = database_db.get_user_all_count()
    c = context.chat_data['aktiv']
    admin_txt = f"XABAR {c}-ta foydalanuvchiga bordi\n\nBarcha obunachilar soni: <b>{all_user[0]}</b>\nFaol obunachilar soni: <b>{c}</b>"
    context.bot.send_message(chat_id=758934089, text=admin_txt, parse_mode="HTML")
    all_admins = database_db.get_admin_list()
    for item in all_admins:
        try:
            context.bot.send_message(chat_id=item[1], text=admin_txt, parse_mode="HTML")
        except Exception:
            pass
    return 10


def get_photo(update: Update, context: CallbackContext):
    photo, caption = update.message.photo[-1].file_id, update.message.caption
    c = 0
    if context.chat_data['battons']:
        for user in database_db.get_user_all():
            try:
                _caption = caption.replace('#firstname', user[1])
                sleep(0.07)
                update.message.bot.send_photo(chat_id=user[0],
                                              photo=photo,
                                              caption=_caption,
                                              disable_notification=False,
                                              reply_markup=link_batton(context.chat_data['battons']))

                # forwarded_message = update.message.forward_from_chat
                # context.bot.send_photo(chat_id=user[1], photo=photo, caption=caption,
                #                        forward_from_chat=forwarded_message)
                c += 1
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_all():
            try:
                sleep(0.07)
                _caption = caption.replace('#firstname', user[1])
                context.bot.send_photo(chat_id=user[0],
                                       photo=photo,
                                       # forward_from_chat=update.message.forward_from_chat,
                                       caption=_caption)
                c += 1
            except Exception as e:
                print(e)
    context.chat_data['aktiv'] = c
    return send_aktiv_user_to_admins(update, context)


def get_video(update: Update, context: CallbackContext):
    video, caption = update.message.video.file_id, update.message.caption
    c = 0
    if context.chat_data['battons']:
        for user in database_db.get_user_all():
            try:
                _caption = caption.replace('#firstname', user[1])
                sleep(0.07)
                update.message.bot.send_video(chat_id=user[0],
                                              video=video,
                                              caption=_caption,
                                              disable_notification=False,
                                              # forward_from_chat=update.message.forward_from_chat,
                                              reply_markup=link_batton(context.chat_data['battons']))
                c += 1
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_all():
            try:
                _caption = caption.replace('#firstname', user[1])
                sleep(0.07)
                context.bot.send_video(chat_id=user[0],
                                       video=video,
                                       # forward_from_chat=update.message.forward_from_chat,
                                       caption=_caption)
                c += 1
            except Exception as e:
                print(e)
    context.chat_data['aktiv'] = c
    return send_aktiv_user_to_admins(update, context)


def get_audio(update: Update, context: CallbackContext):
    audio, caption = update.message.audio.file_id, update.message.caption
    c = 0
    if context.chat_data['battons']:
        for user in database_db.get_user_all():
            try:
                _caption = caption.replace('#firstname', user[1])
                sleep(0.07)
                update.message.bot.send_audio(chat_id=user[0],
                                              audio=audio,
                                              caption=_caption,
                                              disable_notification=False,
                                              # forward_from_chat=update.message.forward_from_chat,

                                              reply_markup=link_batton(context.chat_data['battons']))
                c += 1
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_all():
            try:
                _caption = caption.replace('#firstname', user[1])
                sleep(0.07)
                context.bot.send_audio(chat_id=user[0],
                                       audio=audio,
                                       # forward_from_chat=update.message.forward_from_chat,
                                       caption=_caption)
                c += 1
            except Exception as e:
                print(e)
    context.chat_data['aktiv'] = c
    return send_aktiv_user_to_admins(update, context)


def get_voice(update: Update, context: CallbackContext):
    voice, caption = update.message.voice.file_id, update.message.caption
    c = 0
    if context.chat_data['battons']:
        for user in database_db.get_user_all():
            try:
                _caption = caption.replace('#firstname', user[1])
                sleep(0.07)
                update.message.bot.send_voice(chat_id=user[0],
                                              voice=voice,
                                              caption=_caption,
                                              # forward_from_chat=update.message.forward_from_chat,
                                              disable_notification=False,
                                              reply_markup=link_batton(context.chat_data['battons']))
                c += 1
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_all():
            try:
                _caption = caption.replace('#firstname', user[1])
                sleep(0.07)
                context.bot.send_voice(chat_id=user[0],
                                       voice=voice,
                                       # forward_from_chat=update.message.forward_from_chat,

                                       caption=_caption)
                c += 1
            except Exception as e:
                print(e)
    context.chat_data['aktiv'] = c
    return send_aktiv_user_to_admins(update, context)
    # update.message.bot.forward_message(chat_id=update.message.chat.id, from_chat_id='@' + channel_username, message_id=message_id)


def get_text(update: Update, context: CallbackContext):
    rek_text = update.message.text
    c = 0
    if context.chat_data['battons']:
        for user in database_db.get_user_all():
            try:
                _rek_text = rek_text.replace('#firstname', user[1])
                sleep(0.07)
                update.message.bot.send_message(chat_id=user[0],
                                                text=_rek_text,
                                                reply_markup=link_batton(context.chat_data['battons']))
                c += 1
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_all():
            try:
                _rek_text = rek_text.replace('#firstname', user[1])
                sleep(0.07)
                context.bot.send_message(chat_id=user[0],
                                         text=_rek_text, )
                c += 1
            except Exception as e:
                print(e)
    context.chat_data['aktiv'] = c
    return send_aktiv_user_to_admins(update, context)
    # update.message.bot.forward_message(chat_id=update.message.chat.id, from_chat_id='@' + channel_username, message_id=message_id)


def get_link_batton(update: Update, context: CallbackContext):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[4]
    text = update.message.text
    if text == 'No':
        batton_lists = []
    else:
        batton_lists = []
        batton_list = [item for item in text.split(' - ')]
        for item in batton_list:
            if '\n' in item:
                for i in item.split('\n'):
                    batton_lists.append(i)
            else:
                batton_lists.append(item)
    context.chat_data['battons'] = batton_lists
    update.message.reply_html(text=reklama_txt.get(user_lang), reply_markup=admin_rek_batton(user_lang))
    return 20


def get_not_link_batton(update: Update, context: CallbackContext):
    user_lang = 'uz'
    batton_lists = []
    context.chat_data['battons'] = batton_lists
    update.message.reply_html(text=reklama_txt.get(user_lang), reply_markup=admin_rek_batton(user_lang))
    return 20