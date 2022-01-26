# from telegram.ext.updater import Updater
# from telegram.update import Update
# from telegram.ext.callbackcontext import CallbackContext
# from telegram.ext.commandhandler import CommandHandler
# from telegram.ext.messagehandler import MessageHandler
# from telegram.ext.filters import Filters
#
# #апішка телеграм бота
# updater = Updater("5042937321:AAEAkBoQlHwrViTMSnMXrrtE2_V87ozKe6Q",
#                   use_context=True)
#
# #загальний функціонал
# def start(update: Update, context: CallbackContext):
#     update.message.reply_text("""Availible commands:
#     /help - start chatting about your issue
#     /admin - enter chat as an admin
#     """)
#
# #загальна допомога а-ля може людина дійсно затупила (це обговорити з Нікітою потім)
# def help(update: Update, context: CallbackContext):
#     update.message.reply_text("""Common issues:
#
# ● CANNOT FIGURE OUT HOW
#   STAKING WORKS? ●
#
# Check out this detailed guide of how
# to stake! :
#
# https://ksmstarter.medium.com/kst-staking-is-live-72a65b422c5c
#
# ● LOST WITH UPCOMING IDOS? ●
#
# Make sure to go ahead and enter
# their chats!
# Enter /upcoming to get the list of
# telegram chats
# Or you can just join the
# announcement channel here:
#
# https://t.me/KSM_starterANN
#
# ● HAVING TROUBLES WITH WEBSITE WORKING POORLY? ●
#
# Try clearing cache and refreshing the
# webpage, if still doesn't help then
# check the instructions below!
# Who knows maybe you'll find out the
# answer!
#
#
#
# If these weren't helpful please enter
# your issue.
#
# Your feedback MUST include:
#
# 1. Type of problem ( metamask,
#    staking etc.)
# 2. Detailed description.
# 3. OPTIONAL: a screenshot of the
#    issue itself.
#     """)
#
# #тут ми беремо те що людина ввела,я не сторила,бо може прийдеться кудись передавати
# def get_issue(update: Update, context: CallbackContext):
#     # txt = update.message.text
#     update.message.reply_text("""Thanks for your feedback! We will make sure to fix it as quick as possible!""")
#
# #тимчасово поки ми не вирішили куди то буде іти,я додала а-ля секція для адмінів,до якої має бути пароль і яка по суті
# # має виводити всі issues + ніки людей в тг
# # def admin (update: Update, context: CallbackContext):
#     # password = update.message.text
#     # if password = "1111":
#     #         update.message.reply_text(txt)
#     # else:
#     #     update.message.reply_text("""Oops! It looks like you've entered incorrect password. Try again""")
#
# #ще одна секція інфоблоку
# def upcoming(update: Update, context: CallbackContext):
#     update.message.reply_text("""
#     ● CHEESUS ●
#     https://t.me/KSM_starter/119294
#     """)
#
# #catch неправильних команд
# def unknown(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Sorry '%s' is not a valid command" % update.message.text)
#
# #тут ще буде команда leave chat
#
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('help', help))
# # updater.dispatcher.add_handler(CommandHandler('admin', admin))
# updater.dispatcher.add_handler(CommandHandler('upcoming', upcoming))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, get_issue))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
# updater.dispatcher.add_handler(MessageHandler(
#     Filters.command, unknown))
#
# updater.start_polling()
#
# # /Users/md/PycharmProjects/ksmtelegram