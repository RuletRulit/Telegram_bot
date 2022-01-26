import telebot
import fastapi
import logging
import uvicorn

import telebot.apihelper
from telebot import types


API_TOKEN = '5053429740:AAFXTkrXNZLwjAdsYlS3SjFC4aXCgOrLkzM'

WEBHOOK_HOST = '<ip/domain>'  # docker localhost(most likely)
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key

# Quick'n'dirty SSL certificate generation:
#
# openssl genrsa -out webhook_pkey.pem 2048
# openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
#
# When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
# with the same value in you put in WEBHOOK_HOST

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(API_TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)

app = fastapi.FastAPI()


@app.post(f'/{API_TOKEN}/')
def process_webhook(update: dict):
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message, text="""Common issues:
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


@bot.message_handler(commands=['update'])
def coming_soon(message):
    bot.send_message(message, text="""
#     ● CHEESUS ●
#     https://t.me/KSM_starter/119294
#     """)


# @bot.message_handler(commands=['send_bug'])
def send_bug(message, report):
    telebot.apihelper.send_message(message, chat_id='-682420808', text=report)


bot.polling(none_stop=True)


bot.remove_webhook()


bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

uvicorn.run(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
    ssl_certfile=WEBHOOK_SSL_CERT,
    ssl_keyfile=WEBHOOK_SSL_PRIV
)
