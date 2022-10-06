# from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .browser import masirosign
from .database import jobhandle as jb



# 增添or修改账号
async def plusaccount(useraccount,userpassword):
    username, userlevel, userjinbi, userjinyanzhi = await masirosign(useraccount,userpassword)
    jb.plus(useraccount,userpassword,username,userjinyanzhi)


# 删除账号
# 单个
async def deleteaccount(username):
    flag = jb.delete(username)
    if flag:
        return "删除成功喵~"
    else:
        return "查无此人喵！"

# 清空
async def clearallaccount():
    jb.clearall()


# 查询账号列表
async def searchlist():
    if jb.matchlist() == None:
        return "一无所有呢喵~"
    else:
        text0 = jb.matchlist()
        text1 = []
        text = '' 
        for i in text0:
            if i != "null":
                text1.append(f'昵称{i}，主人的账号是{text0[i][0]}~')       
        for i in range(len(text1)):
            if i == len(text1)-1:
                text = text + text1[i]
            else:
                text = text + text1[i] + "\n"
        return text


# 查询账号信息
async def search(username):
    if jb.match(username) != None:
        useraccount, userpassword = jb.match(username)
        infor = await masirosign(useraccount,userpassword)  
        userlevel, userjinbi, userjinyanzhi = infor[1], infor[2], infor[3]
        text = f'主人{username}您好喵！您的账号等级是{userlevel}，{userjinyanzhi}，{userjinbi}喵！'
        return text
    else:
        return '查无此人喵！' 


# 定时工作&手动尝试
async def qiandao():
    if jb.matchlist != None:
        successlist = []
        account = jb.matchlist()
        for i in account:
            if i != "null":
                useraccount, userpassword, userjinyanzhi = account[i][0], account[i][1], account[i][2]
                infor = await masirosign(useraccount,userpassword)
                userjinyanzhi_new = infor[3]
                if userjinyanzhi_new != userjinyanzhi:
                    successlist.append(infor[0])
        return successlist

# 手动            
async def handmake():
    successlist = await qiandao()
    if successlist == []:
        return '全寄了喵！'
    else:
        text = ''
        for i in range(len(successlist)):
            if i == len(successlist)-1:
                text = text + f'{successlist[i]}签到成功了喵！'

            else:
                text = text + f'{successlist[i]}签到成功了喵！' + '\n'
        return text                        


# 自动(好像也没啥用了)
# scheduler = AsyncIOScheduler()
# async def parttime():
#     successlist = await scheduler.add_job(qiandao, 'cron', hour='8')
#     if successlist == []:
#         return '全寄了喵'
#     else:
#         text = ''
#         for i in range(len(successlist)):
#             if i == len(successlist)-1:
#                 text = text + f'{successlist[i]}签到成功！'
#             else:
#                 text = text + f'{successlist[i]}签到成功！' + '\n'
#         return text

