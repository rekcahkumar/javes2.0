

import os
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG, WARNING
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession
from userbot.database.value_sql import get_all_sql



basicConfig(format='[%(name)s: %(message)s', level=INFO)
LOGS = getLogger(__name__)

BOTLOG = BOTLOG_CHATID = None
Sql = get_all_sql()                 
for i in Sql:  
               if i.sqlvar == "BOTLOG_CHATID":
                   BOTLOG_CHATID = i.sqlvalue
               if i.sqlvar == "BOTLOG":
                   BOTLOG = i.sqlvalue
               if i.sqlvar == "PM_PROTECTOR":
                   PM_PROTECTOR = i.sqlvalue
               if i.sqlvar == "BOTLOG":
                   BOTLOG = i.sqlvalue
        


API_KEY = "1754367"
API_HASH = "231b8cc6cca12ee51a85cf543321f476"
STRING_SESSION = os.environ.get("STRING_SESSION", None)
STRING_SESSION2 = os.environ.get("STRING_SESSION2", None)
STRING_SESSION3 = os.environ.get("STRING_SESSION3", None)
HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)



   

if STRING_SESSION:
    javes = client = TelegramClient(StringSession(STRING_SESSION),API_KEY,API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
else:
     LOGS.info("Please Add STRING_SESSION Value") ; quit(1)
if BOT_TOKEN:    
    tebot = TelegramClient("bot", API_KEY, API_HASH).start(bot_token=BOT_TOKEN)
else:
    LOGS.info("Please Add BOT_TOKEN Value") ; quit(1)
if STRING_SESSION2:
    client2 = TelegramClient(StringSession(STRING_SESSION2),API_KEY,API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
else:
   client2 = None
if STRING_SESSION2:
    client3 = TelegramClient(StringSession(STRING_SESSION2),API_KEY,API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
else:
    client3 = None


OWNER = {0}
HEAD_AD = {0}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CMD_LIST = {}
LOAD_PLUG = {}
ISAFK = None
AFKREASON = None
INT_PLUG = ""


