# 基于ntwork的消息发送方法构造

## 自动回复如此简便，快速构建你的业务逻辑

```python
import ntwork

from wework_bot.fuctions.action import reply_msg, wework
from wework_bot.rule import Rule
from wework_bot import run


@wework.msg_register(ntwork.MT_RECV_TEXT_MSG)
def msg_handler(wework_instance: ntwork.WeWork, message):
    #  回复一条消息
    reply_msg(
        wework_instance,
        message,
        rule=Rule.PRIVATE, # 仅私聊触发
        cmd='你好',
        reply='你好呀'
    )

if __name__ == '__main__':
    run.forever()
```
更多玩法请参考源码