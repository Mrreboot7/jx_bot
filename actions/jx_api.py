#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
>> 文件作者: Elliot.Ma
>> 开发日期: 2021-04-25 16:16:57
>> 修改时间: 2021-04-25 17:10:54
>> 文件描述: 文件描述
"""

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class JXApi:
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
        }

    def flower(self, server: str, maps: str, types: str = None):
        url = "https://spider.jx3box.com/flower"
        params = {"server": server, "map": maps, "type": types}
        res = requests.get(url=url, headers=self.headers, params=params, verify=False)
        return res.json()


def main():
    # c = JXApi()
    # res = c.flower(server="破阵子", maps="广陵邑")
    # print(res)
    # for data in res["data"]:
    #     lines_text = "当前最高分线: "
    #     for line in data["branch"]:
    #         lines_text += str(line["number"]) + "线、"
    #     print(data["name"], lines_text)
    url = "http://localhost:5005/webhooks/rest/webhook"
    data = {
        "sender": "wx_chat",
        "message": "今日花价",
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    res = requests.post(url=url, headers=headers, json=data)
    print(res.json()[0]['text'])
    return res.json()


if __name__ == "__main__":
    main()
