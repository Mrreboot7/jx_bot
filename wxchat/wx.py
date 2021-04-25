#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
>> 文件作者: Elliot.Ma
>> 开发日期: 2021-04-25 14:30:33
>> 修改时间: 2021-04-25 17:09:52
>> 文件描述: 文件描述
"""


import requests
from wxpy import Bot, Group
from wxpy import get_wechat_logger


bot = Bot(cache_path=True)
bot.enable_puid("wxpy_puid.pkl")


def rasa_webhook(message):
    url = "http://localhost:5005/webhooks/rest/webhook"
    data = {
        "sender": "wx_chat",
        "message": message,
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    res = requests.post(url=url, headers=headers, json=data)
    return res.json()


@bot.register()
def auto_reply(msg):
    logger = get_wechat_logger(receiver=bot)

    # 接收捕获的异常
    try:

        # 如果是群聊，但没有被 @，则不回复
        if isinstance(msg.chat, Group) and not msg.is_at:
            return
        else:
            # 回复消息内容和类型
            res_msg = rasa_webhook(msg.text)
            logger.exception(f"{res_msg}")
            return res_msg[0]['text']
    except Exception as e:
        logger.exception(f"{e}")


bot.join()
