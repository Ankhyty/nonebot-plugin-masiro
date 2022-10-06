# https://masiro.me/admin/auth/login
from playwright.async_api import BrowserContext, async_playwright
import asyncio


async def get_brower() -> BrowserContext:
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=True)
    context = await browser.new_context()
    return context

async def masirosign(useraccount,userpassword):
    context = await get_brower()
    page = await context.new_page()

    # 登陆
    await page.goto("https://masiro.me/admin/userCenterShow")
    await page.locator("text=登录 账号 密码 邮箱验证码 获取验证码 记住密码 Login 忘记密码 ? 去注册 >> [placeholder=\"请输入用户名或邮箱\"]").click()
    await page.locator("text=登录 账号 密码 邮箱验证码 获取验证码 记住密码 Login 忘记密码 ? 去注册 >> [placeholder=\"请输入用户名或邮箱\"]").fill(useraccount)
    await page.locator("text=登录 账号 密码 邮箱验证码 获取验证码 记住密码 Login 忘记密码 ? 去注册 >> [placeholder=\"请输入密码\"]").click()
    await page.locator("text=登录 账号 密码 邮箱验证码 获取验证码 记住密码 Login 忘记密码 ? 去注册 >> [placeholder=\"请输入密码\"]").fill(userpassword)
    await page.locator("input[name=\"remember\"]").uncheck()
    await page.locator("text=Login").click()
    await page.locator("text=OK").click()
    await page.wait_for_url("https://masiro.me/admin/userCenterShow",wait_until='domcontentloaded')

    # 防止过快寄了,等5s
    await page.wait_for_timeout(5000)


    # 获取信息
    # 用户名
    element1 = await page.query_selector('.user-name-info')
    textcontent1 = await element1.inner_text()
    username = textcontent1

    # 金币&经验值
    element2 = await page.query_selector('.middle-area')
    textcontent2 = await element2.inner_text()
    notetext = textcontent2.split()
    userjinbi = notetext[0]
    userjinyanzhi = notetext[1]

    # 用户等级
    element3 = await page.query_selector('.user-lev')
    textcontent3 = await element3.inner_text()
    userlevel = textcontent3


    # 登出（没啥用其实）
    # await page.locator("img[alt=\"User Image\"]").first.click()
    # await page.locator("text=登出").click()
    # await page.wait_for_url("https://masiro.me/admin/auth/login")

    await context.close()

    return username, userlevel, userjinbi, userjinyanzhi

# 测试用
# async def main():
#     a,b,c,d = await masirosign(useraccount,userpassword)
#     print(a,b,c,d)

# asyncio.run(main())