from nonebot.adapters.onebot.v11 import Message
from nonebot import require
require("nonebot_plugin_apscheduler")

from nonebot.plugin import on_command
from nonebot_plugin_apscheduler import scheduler
from nonebot.params import State
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN, GROUP_OWNER, PRIVATE_FRIEND
PERM_EDIT = GROUP_ADMIN | GROUP_OWNER | SUPERUSER
PERM_GLOBAL = SUPERUSER


from . import jobhandle as jbhd


msrzdqd = on_command("masiro自动签到", priority=10,permission=PERM_EDIT)
@msrzdqd.handle()
async def zdqd():
    await msrzdqd.send('自动签到已开启！')
    @scheduler.scheduled_job('cron', hour='8', minute='30')
    async def yunxing():
        zdqd = await jbhd.handmake()
        await msrzdqd.send(zdqd)
    scheduler.add_job(yunxing,'cron', hour='8', minute='30',start_date='2022-10-5 3:30:00')



msrqd = on_command("masiro签到", priority=12)
@msrqd.handle()
async def qd():
    qd = await jbhd.handmake()
    await msrqd.finish(qd)



msrcx = on_command("masiro查询", priority=12)
@msrcx.got("username", prompt='请输入用户名~')
async def msrchaxun(state:T_State = State()):
    username = str(state['username'])
    text = await jbhd.search(username)
    await msrcx.finish(text)



msrlb = on_command("masiro列表", priority=12,permission=PERM_EDIT)
@msrlb.handle()
async def msrliebiao():
    text = await jbhd.searchlist()
    await msrlb.finish(text)



msrtj = on_command("masiro添加", priority=12)
@msrtj.got("account",prompt='请输入账密，中间用空格隔开~')
async def msrtianjia(state:T_State = State()):
    account0 = str(state['account'])
    account = account0.split()
    useraccount, userpassword = account[0], account[1]
    await jbhd.plusaccount(useraccount,userpassword)
    await msrtj.finish('添加成功了喵！') 



msrsc = on_command("masiro删除", priority=12,permission=PERM_EDIT)
@msrsc.got("deleteaccount",prompt='请输入用户名~')
async def msrshanchu(state:T_State = State()):
    deleteaccount = str(state['deleteaccount'])
    text = await jbhd.deleteaccount(deleteaccount)
    await msrsc.finish(text)



msrqk = on_command("masiro清空", priority=12,permission=PERM_EDIT)
@msrqk.handle()
async def msrqingkong():
    await jbhd.clearallaccount()
    await msrqk.finish('清除完成了喵！')