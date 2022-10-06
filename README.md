# masiro

_:tada::tada::tada:助力你成为二次元婆罗门！:tada::tada::tada:_

## 简介

本插件可以帮你在真白萌 [masiro](https://masiro.me/)上自动签到，并且返回你的等级、经验值、金币数等信息。

## 特色功能

masiro是一款以漫研为目的开发的插件。

- 使用[playwright](https://github.com/microsoft/playwright)作为无头浏览器，支持异步，效率更高。
- 使用apscheduler进行定时任务设计，它是一个强大的python库。
- 使用json数据格式进行本地数据储存，no数据库！
- 速速升级，然后畅游于厕纸的海洋吧！

## 安装

- 推荐使用脚手架安装

```
pip install nonebot-plugin-masiro
```

- 然后在bot.py文件中添加

```
nonebot.init(apscheduler_config={"apscheduler.timezone": "Asia/Shanghai"})
nonebot.load_plugin('nonebot-plugin-masiro')
```

- 在env文件中添加

```
APSCHEDULER_CONFIG={"apscheduler.timezone": "Asia/Shanghai"}
```

## 功能展示

- 使用 `/masiro` 为开头的一系列指令来触发机器人执行相应任务。

- `/masiro添加` 添加或者修改你的真白萌账密
- `/masiro查询` 查询账号对应的等级、经验值、金币数等信息
- `/masiro删除` 删除不想要的真白萌账号（需管理员权限）
- `/masiro列表` 查看已有的所有真白萌账号（需管理员权限）
- `/masiro清空` 删除所有的真白萌账号（需管理员权限）
- `/masiro签到` 手动尝试签到所有的真白萌账号
- `/masiro自动签到` 开启自动签到功能，默认每天早上8:30尝试签到一次

## 一些问题

- 虽然做了debug措施，但是还是有很多会出bug的情况QAQ。
- 真白萌服务器不稳定，经常会访问失败，导致查询、签到等失败。
- 指令分两步执行有些冗长，但本人太菜，还没怎么学会整合，之后会尝试一下。
- 写定时任务对应功能的时候本人脑子有些抽象，导致开启之后不能关闭~~（除非重启bot）~~、不能自定义自动签到时间等一系列问题，现在还不知道怎么改进~~（等我再学会儿）~~。

## 特别感谢

因为本人太菜了，因此从不少大佬们做好的插件里学习，才写出了现在的masiro插件。

- [NoneBot2](https://github.com/nonebot/nonebot2)：本插件实装的开发框架。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)：稳定完善的 CQHTTP 实现。
- [word-bank2](https://github.com/kexue-z/nonebot-plugin-word-bank2)：从中学到了很多问答库处理、json处理的知识，大佬太强了。

## 支持

大家喜欢的话可以给这个项目点个star

有bug、意见和建议都欢迎提交 [Issues](https://github.com/Ankhyty/nonebot-plugin-masiro/issues) 

## 许可证
本项目使用 [MIT](https://choosealicense.com/licenses/mit/) 作为开源许可证。
