

import asyncio, time, io, math, os, logging, asyncio, shutil, re, inspect, sys, json
from telethon import events
from pathlib import Path
from asyncio import create_subprocess_shell as asyncsubshell, subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc
from typing import List
from userbot.javes_main.heroku_var import *
from userbot import *
from sys import *
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon import TelegramClient, functions, types
from telethon.tl.types import InputMessagesFilterDocument
import traceback
from userbot.database.sudo_sql import get_all_sudo

R_OWNER = list(OWNER)
del R_OWNER[0]
tee = {0}
getsudo = get_all_sudo()                       
for i in getsudo:    
             asu = str(i.sender)          
             tee.add (int(asu))                     
R_SUDIO = list(tee)
R_OWNER = list(OWNER)
del R_OWNER[0]
del R_SUDO[0]
                    



def J_Client(**args):    
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', True)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    disable_errors = args.get('disable_errors', False)
    sudo = args.get("sudo", None)
    owner = args.get("owner", None)
    tebot2 = args.get("tgbot", None)
    if not owner and not sudo:
        return
    if owner and tebot2:       
        args["from_users"] = R_OWNER
        args["incoming"] = True
        del args["owner"]
        del args["tgbot"]        
    if owner and not tebot2:
            args["from_users"] = R_OWNER
            args["outgoing"] = True    
            del args["owner"]
           
    if sudo and tebot2:
        args["from_users"] = R_SUDO
        args["incoming"] = True    
        del args["sudo"]
        del args["tgbot"]   
        
    if sudo and not tebot2:
            args["from_users"] = R_SUDO
            args["incoming"] = True   
            del args["sudo"]                
    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern
    if "disable_edited" in args:
        del args['disable_edited']
    if "groups_only" in args:
        del args['groups_only']
    if "disable_errors" in args:
        del args['disable_errors']
    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
    def decorator(func):
        async def wrapper(check):
            if LOGSPAMMER:
                send_to = BOTLOG_CHATID
            if not trigger_on_fwd and check.fwd_from:
                return
            if groups_only and not check.is_group:
                await check.respond("`I don't think this is a group.`")
                return            
            try:
                await func(check)            
            except events.StopPropagation:
                raise events.StopPropagation            
            except KeyboardInterrupt:
                pass
            except BaseException:
                if not disable_errors:                    
                    text = "**JAVES ERROR REPORT**\n"
                    text += "Send this to @javes05 if you cant find issue\n"                                      
                    ftext += "--------BEGIN LOG--------\n"
                    ftext += "\nDate: " + date                    
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END  LOG--------"
                    command = "git log --pretty=format:\"%an: %s\" -10"
                    ftext += "\n\n\nLast 10 commits:\n"
                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())
                    ftext += result
                    file = open("javes_error.log", "w+")
                    file.write(ftext)
                    file.close()                    
                    await check.client.send_file(send_to, "javes_error.log", caption=text)
                    remove("javes_error.log")
            else:
                pass                
        if not tebot2:
           client.add_event_handler(wrapper, events.NewMessage(**args))
        if client2 and not tebot2:
            client2.add_event_handler(wrapper, events.NewMessage(**args))
        if client3 and not tebot2:
            client3.add_event_handler(wrapper, events.NewMessage(**args))
        if tebot and tebot2:
        	tebot.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper
    return decorator


