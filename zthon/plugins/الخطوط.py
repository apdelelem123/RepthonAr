# Repthon - Roger
# © Repthon Team 2023
# ها شعدك داخل ع الملف تريد تخمط ؟ ابو زربة لهل درجة فاشل  
from telethon import events
from zthon import zedub
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete
from telethon import functions
from telethon.errors.rpcerrorlist import MessageIdInvalidError


@zedub.on(admin_cmd(pattern="(خط الغامق|خط غامق)"))
async def btext(event):
    isbold = gvarstatus("bold")
    if not isbold:
        addgvar ("bold", "on")
        await edit_delete(event, "**⎉╎ تم تفعيل خط الغامق بنجاح ✓**")
        return

    if isbold:
        delgvar("bold")
        await edit_delete(event, "**⎉╎ تم اطفاء خط الغامق بنجاح ✓ **")
        return

@zedub.on(admin_cmd(pattern="(خط رمز|خط الرمز)"))
async def btext(event):
    isramz = gvarstatus("ramz")
    if not isramz:
        addgvar ("ramz", "on")
        await edit_delete(event, "**⎉╎ تم تفعيل خط الرمز بنجاح ✓**")
        return

    if isramz:
        delgvar("ramz")
        await edit_delete(event, "**⎉╎ تم اطفاء خط الرمز بنجاح ✓ **")
        return

@zedub.on(admin_cmd(pattern="(خط مائل|الخط المائل"))    
async def btext(event):
    isitalic = gvarstatus("italic")
    if not isitalic:
        addgvar ("italic", "on")
        await edit_delete(event, "**⎉╎ تم تفعيل خط مائل بنجاح ✓**")
        return      
  
    if italic:
        delgvar("italic")
        await edit_delete(event, "**⎉╎ تم إطفاء خط مائل بنجاح ✓**")
        return

@zedub.on(events.NewMessage(outgoing=True))
async def baqir(event):
    isbold = gvarstatus("bold")
    if isbold:
        try:
            await event.edit(f"**{event.message.message}**")
        except MessageIdInvalidError:
            pass
    isramz = gvarstatus("ramz")
    if isramz:
        try:
            await event.edit(f"`{event.message.message}`")
        except MessageIdInvalidError:
            pass
  isitalic = gvarstatus("italic")
  if isitalic:
    try:
      await event.edit(f"__{event.message.message}__")
    except MessageIdInvalidError:
        pass
