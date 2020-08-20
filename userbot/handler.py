
import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc
from telethon import events
from userbot import *
from userbot.database.sudo_sql import get_all_sudo
import itertools







tee = {0}
getsudo = get_all_sudo()                       
for i in getsudo:    
             asu = str(i.sender)          
             tee.add (int(asu))                     
R_SUDO = list(tee)
R_OWNER = list(OWNER)
R_HA = list(HEAD_AD)
del R_OWNER[0]
del R_HA[0]
del R_SUDO[0]
                    
for i in R_HA:
  HEAD = int(i)



osudo = []
for i in range(len(R_OWNER)):
    osudo.append(R_OWNER[i])
    if i < len(R_SUDO):
        osudo.append(R_SUDO[i])
#sowner = [i for i in itertools.chain(*itertools.izip_longest(R_SUDO,R_OWNER)) if i is not None]
#sowner = osudo
sowner = R_OWNER + R_SUDI
ssudo = R_SUDO
oowner = R_OWNER
headowner = R_HA

def J_Client(**args):    
    pattern = args.get('pattern', None)
    allow_edited = args.get('allow_edited', False)
    groups_only = args.get('groups_only', False)
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
    elif owner and not tebot2:
            args["from_users"] = R_OWNER
            args["outgoing"] = True    
            del args["owner"]         
    if sudo and tebot2:
        args["from_users"] = R_SUDO
        args["incoming"] = True    
        del args["sudo"]
        del args["tgbot"]           
    elif sudo and not tebot2:
            args["from_users"] = R_SUDO
            args["incoming"] = True   
            del args["sudo"]                
    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern
    if "allow_edited" in args:
        del args['allow_edited']
    if "groups_only" in args:
        del args['groups_only']
    if "disable_errors" in args:
        del args['disable_errors']
    
    def decorator(func):
        async def wrapper(check): 
            if not check.sender_id in ssudo and not check.sender_id in oowner:
               LOGS.info(f"Warning!! adnormal request from {check.sender_id} has been blocked!!")
               file = open("security.log", "w+")
               file.write(f"Adnormal Request has been blocked, Debug Info\n\n{check.sender} \n\n Blocked Access message \n{check.text}")
               file.close() 
               await tebot.send_file(HEAD, "security.log", caption="Please report this in our support chat!!")                        
               return remove("security.log")                          
            if allow_edited:
                if check.edit_date and check.is_channel and not check.is_group:     
                    return  
            if check.fwd_from:
                return
            if groups_only and not check.is_group:
                await check.respond("`Sorry This Command For groups only!.`")
                return            
            try:
                await func(check)            
            except events.StopPropagation:
                raise events.StopPropagation            
            except KeyboardInterrupt:
                pass
            except BaseException:
                if not disable_errors:                    
                    text = "`I got crashed please Check my error report!`\n"                                                                            
                    ftext = "\n\nCommand You Tried:\n"
                    ftext += str(check.text)
                    ftext += "\n\nError I got:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\nDetailed Error:\n"
                    ftext += str(format_exc())  
                    ftext += "\n\nIf you cant find any issue please report it in https://t.me/JavesSupport\n"            
                    command = "git log --pretty=format:\"%an: %s\" -10"
                    ftext += "\n\n\nLast 10 updates:\n"
                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())
                    ftext += result
                    
                    if BOTLOG: 
                        file = open("javes_error.log", "w+")
                        file.write(ftext)
                        file.close() 
                        await tebot.send_file(HEAD, "javes_error.log", caption=text)
                        LOGS.info (" Sent some errors that i got recently please check your bot's private message ")
                        try:
                          return remove("javes_error.log")
                        except:
                          return
                    else:
                        LOGS.info(str(format_exc()))
                        return
        if not tebot2:
           if allow_edited:
               client.add_event_handler(wrapper, events.MessageEdited(**args))
           client.add_event_handler(wrapper, events.NewMessage(**args))
        if client2 and not tebot2:
            if allow_edited:
               client2.add_event_handler(wrapper, events.MessageEdited(**args))
            client2.add_event_handler(wrapper, events.NewMessage(**args))
        if client3 and not tebot2:
            if allow_edited:
               client3.add_event_handler(wrapper, events.MessageEdited(**args))
            client3.add_event_handler(wrapper, events.NewMessage(**args))
        if tebot2:
            if allow_edited:
               tebot.add_event_handler(wrapper, events.MessageEdited(**args))
            tebot.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper
    return decorator


