from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.ext import Dispatcher, ConversationHandler
from admin.admin_basic import *
from admin.reklama import *
from methods.check_channel import check_is_subscribed
from settings import TOKEN
from static_files.admin_files.admin_basic_files import admin_basic_batton_txts
from methods import start, user_txt_bug, back_user
from admin.admin_basic import admin
from static_files.allstates import *

update = Updater(token=TOKEN, use_context=True, workers=1000)

dispatcher: Dispatcher = update.dispatcher
a = dispatcher.groups

hand_command = ConversationHandler(entry_points=[CommandHandler('start', start),
                                                 CommandHandler('admin', admin)],
                                   states={
                                       1: [CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.text, user_txt_bug)],
                                       10: [CommandHandler('start', start),
                                            CommandHandler('admin', admin),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][0] + ')$'),
                                                all_user),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][1] + ')$'),
                                                admin_lists),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][2] + ')$'),
                                                add_admin),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][3] + ')$'),
                                                admin_delete),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][4] + ')$'), reklama),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][5] + ')$'),
                                                text_reklama_to_bot),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][6] + ')$'),
                                                text_reklama_deactivation),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][7] + ')$'),
                                                find_user),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][8] + ')$'),
                                                add_channel),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['uz'][9] + ')$'),
                                                status_channels),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][0] + ')$'),
                                                all_user),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][1] + ')$'),
                                                admin_lists),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][2] + ')$'),
                                                add_admin),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][3] + ')$'),
                                                admin_delete),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][4] + ')$'), reklama),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][5] + ')$'),
                                                text_reklama_to_bot),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][6] + ')$'),
                                                text_reklama_deactivation),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][7] + ')$'),
                                                find_user),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][8] + ')$'),
                                                add_channel),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['ru'][9] + ')$'),
                                                status_channels),

                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][0] + ')$'),
                                                all_user),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][1] + ')$'),
                                                admin_lists),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][2] + ')$'),
                                                add_admin),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][3] + ')$'),
                                                admin_delete),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][4] + ')$'), reklama),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][5] + ')$'),
                                                text_reklama_to_bot),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][6] + ')$'),
                                                text_reklama_deactivation),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][7] + ')$'),
                                                find_user),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][8] + ')$'),
                                                add_channel),
                                            MessageHandler(
                                                Filters.regex('^(' + admin_basic_batton_txts['en'][9] + ')$'),
                                                status_channels),
                                            MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),

                                            MessageHandler(Filters.regex('^(' + basic_menyu_txt['uz'] + ')$'), start),
                                            MessageHandler(Filters.regex('^(' + basic_menyu_txt['ru'] + ')$'), start),
                                            MessageHandler(Filters.regex('^(' + basic_menyu_txt['en'] + ')$'), start),
                                            MessageHandler(Filters.text, user_txt_bug),
                                            ],
                                       # yangi admin username qo'shish
                                       1512: [CommandHandler('start', start),
                                              CommandHandler('admin', admin),
                                              MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                              MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                              MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                              MessageHandler(Filters.text, get_new_admin_chat_ID),
                                              ],
                                       13: [CommandHandler('start', start),
                                            CommandHandler('admin', admin),
                                            MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                            MessageHandler(Filters.text, get_new_admin_username),
                                            ],
                                       # admin delete functions
                                       15: [CommandHandler('start', start),
                                            CommandHandler('admin', admin),
                                            CallbackQueryHandler(admin_delete1),
                                            MessageHandler(Filters.text, user_txt_bug),
                                            ],
                                       # add text reklama
                                       16: [CommandHandler('start', start),
                                            CommandHandler('admin', admin),
                                            MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                            MessageHandler(Filters.text, text_reklama_to_db),
                                            ],
                                       # text reklama deactivate
                                       17: [CommandHandler('start', start),
                                            CommandHandler('admin', admin),
                                            MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                            MessageHandler(Filters.text, text_reklama_deactivation_succesfuly),
                                            ],
                                       # find user
                                       18: [CommandHandler('start', start),
                                            CommandHandler('admin', admin),
                                            MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                            MessageHandler(Filters.text, find_user_with_name),
                                            ],

                                       20: [CommandHandler('start', start),
                                            CommandHandler('admin', admin),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['uz'][0] + ')$'),
                                                           rek_video1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['uz'][1] + ')$'),
                                                           rek_photo1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['uz'][2] + ')$'),
                                                           rek_audio1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['uz'][3] + ')$'),
                                                           rek_voice1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['uz'][4] + ')$'),
                                                           rek_text1),

                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['ru'][0] + ')$'),
                                                           rek_video1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['ru'][1] + ')$'),
                                                           rek_photo1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['ru'][2] + ')$'),
                                                           rek_audio1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['ru'][3] + ')$'),
                                                           rek_voice1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['ru'][4] + ')$'),
                                                           rek_text1),

                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['en'][0] + ')$'),
                                                           rek_video1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['en'][1] + ')$'),
                                                           rek_photo1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['en'][2] + ')$'),
                                                           rek_audio1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['en'][3] + ')$'),
                                                           rek_voice1),
                                            MessageHandler(Filters.regex('^(' + admin_rek_batton_txt['en'][4] + ')$'),
                                                           rek_text1),

                                            MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                            MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),

                                            MessageHandler(Filters.text, find_user_with_name),
                                            ],
                                       21: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),

                                           MessageHandler(Filters.photo & Filters.forwarded, get_photo),
                                           MessageHandler(Filters.video & Filters.forwarded, get_video),
                                           MessageHandler(Filters.audio & Filters.forwarded, get_audio),
                                           MessageHandler(Filters.voice & Filters.forwarded, get_voice),

                                           MessageHandler(Filters.photo, get_photo),
                                           MessageHandler(Filters.video, get_video),
                                           MessageHandler(Filters.audio, get_audio),
                                           MessageHandler(Filters.voice, get_voice),

                                           MessageHandler(Filters.text, get_text),
                                       ],

                                       25: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + reklama_type_all_txt['uz'][0] + ')$'),
                                                          reklama_type),
                                           MessageHandler(Filters.regex('^(' + reklama_type_all_txt['ru'][1] + ')$'),
                                                          get_not_link_batton),
                                           MessageHandler(Filters.text, get_link_batton),
                                       ],

                                       22: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),

                                           MessageHandler(Filters.text, get_link_batton),
                                       ],

                                       1300: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                           MessageHandler(Filters.text, add_channel_id),
                                       ],
                                       1301: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                           MessageHandler(Filters.text, add_channel_name),
                                       ],
                                       1302: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                           MessageHandler(Filters.text, add_channel_url),
                                       ],
                                       1305: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                           MessageHandler(Filters.text, status_edit_channel),
                                       ],
                                       1306: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + text_channel_update_txt + ')$'),
                                                          status_edit_channel_id),
                                           MessageHandler(Filters.regex('^(' + status_channel_update_txt + ')$'),
                                                          channel_status_update_text),
                                           MessageHandler(Filters.text, get_channel_update_text),
                                       ],
                                       1307: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + text_channel_update_txt + ')$'),
                                                          get_channel_update_text),
                                           MessageHandler(Filters.text, get_channel_update_text),
                                       ],
                                       1400: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                           MessageHandler(Filters.text, add_channel_id),
                                       ],
                                       4999: [
                                           CommandHandler('start', start),
                                           CommandHandler('admin', admin),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                           MessageHandler(Filters.text, get_link_batton),
                                       ],
                                       channel_members: [
                                           CommandHandler('start', start),
                                           CallbackQueryHandler(check_is_subscribed),
                                           MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
                                           MessageHandler(Filters.regex('^(' + back_txt['en'] + ')$'), back_user),
                                       ],
                                   },
                                   fallbacks=[CommandHandler('start', start), CommandHandler('admin', admin),
                                              MessageHandler(Filters.text, user_txt_bug)],
                                   run_async=True)

dispatcher.add_handler(handler=hand_command)
update.start_polling()
print('started polling')
update.idle()
