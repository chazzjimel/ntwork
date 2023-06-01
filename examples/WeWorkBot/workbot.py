# -*- coding: utf-8 -*-
import ntwork

from wework_bot.fuctions.action import reply_msg, wework
from wework_bot.rule import Rule
from wework_bot import run


@wework.msg_register(ntwork.MT_RECV_TEXT_MSG)
def msg_handler(wework_instance: ntwork.WeWork, message):
    #  菜单命令
    reply_msg(
        wework_instance,
        message,
        rule=Rule.PRIVATE,
        cmd='/菜单',
        reply=(
            ' [玫瑰]欢迎使用[玫瑰]\n'
            ' [玫瑰]今日问候[玫瑰]\n'
            ' [玫瑰]客户服务[玫瑰]\n'
            ' [玫瑰]数据查询[玫瑰]\n'
            ' [玫瑰]发送日报[玫瑰]\n'
            ' [玫瑰]其他功能[玫瑰]'
        )
    )


if __name__ == '__main__':
    run.forever()
