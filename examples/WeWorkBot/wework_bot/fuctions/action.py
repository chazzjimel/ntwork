import ntwork

from wework_bot.fuctions.message import MsgInfo, Cmd
from wework_bot.rule import Rule, __select_rule

wework = ntwork.WeWork()
wework.open(smart=True)


def reply_msg(
        wework_instance: ntwork.WeWork,
        message,
        rule: Rule,
        cmd: str,
        reply: any
):
    """根据命令返回一条消息"""
    # 消息类实例化
    conversation = MsgInfo(
        wework_instance,
        message
    ).get_conversation_id()  # 实例化消息属性类并获取会话id

    cmd_param = Cmd(
        wework_instance,
        message
    ).cmd_starts(cmd)  # 实例化自定义命令类
    check = __select_rule(
        wework_instance,
        message,
        rule=rule
    )
    if check and cmd_param:
        wework.send_text(
            conversation,
            str(reply)
        )  # 符合条件则向指定会话发送指定消息
