import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

from os import execl, getenv
from telethon import events
from datetime import datetime




@X1.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» __HO RHA HAI ADD SUDO MAI RUKO..__")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» REPLY KRKE KARO !!")
            return

        if str(target) in sudousers:
            await ok.delete()
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.delete()
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» BSDK SIRF BOT OWNER SUDO DE SKTA HAI...")
