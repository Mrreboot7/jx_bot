#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
>> 文件作者: Elliot.Ma
>> 开发日期: 2021-04-25 15:58:49
>> 修改时间: 2021-04-25 17:10:03
>> 文件描述: 文件描述
"""

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.jx_api import JXApi


class ActionFlowerPrice(Action):
    def name(self) -> Text:
        return "action_flower_price"

    def query_price(self, server: str, maps: str, types: str = None):
        c = JXApi()
        res = c.flower(server=server, maps=maps, types=types)
        res_text = f"今日【{server}】（{maps}）{types if types else ''}\n"
        for data in res["data"]:
            lines_text = "当前最高分线: "
            for line in data["branch"]:
                lines_text += str(line["number"]) + "线、"
            res_text += data["name"] + "：\n" + lines_text + "\n"
        return res_text

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        wx_text = self.query_price(server="破阵子", maps="广陵邑")
        dispatcher.utter_message(text=wx_text)

        return []
