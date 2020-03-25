import importlib
import sys
import os

DEBUG = True

PLUGINS = [
    'mmpy_bot.plugins',
    'plugins'
]
PLUGINS_ONLY_DOC_STRING = False

# Default settings
MATTERMOST_API_VERSION = 4
BOT_URL = 'http://vega.fcyb.mirea.ru/mattermost/api/v4'
BOT_LOGIN = 'remindbot@mail.ru'
BOT_PASSWORD = 'OIuRMp22rpe)'
BOT_TOKEN = None
BOT_TEAM = 'BotTest'
SSL_VERIFY = True
WS_ORIGIN = None
WEBHOOK_ID = None  # if not specified mmpy_bot will attempt to create one

IGNORE_NOTIFIES = ['@here', '@channel', '@all']
IGNORE_USERS = []
WORKERS_NUM = 10

DEFAULT_REPLY_MODULE = None
DEFAULT_REPLY = None

"""
If you use Mattermost Web API to send messages (with send_webapi()
or reply_webapi()), you can customize the bot logo by providing Icon or Emoji.
If you use Mattermost API to send messages (with send() or reply()),
the used icon comes from bot settings and Icon or Emoji has no effect.
"""
# BOT_ICON = 'http://lorempixel.com/64/64/abstract/7/'
# BOT_EMOJI = ':godmode:'

"""
Period to trigger jobs in sechduler. Measures in seconds.
If JOB_TRIGGER_PERIOD is not set, mmpy_bot will set default priod 5 seconds.
"""
JOB_TRIGGER_PERIOD = 5

"""
Load local settings
"""
for key in os.environ:
    if key[:15] == 'MATTERMOST_BOT_':
        globals()[key[11:]] = os.environ[key]
