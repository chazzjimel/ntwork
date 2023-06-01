from wework_bot.fuctions.message import MsgRules


class Rule(object):
    """消息响应规则类型选择器"""

    GROUP = 'group'
    PRIVATE = 'private'
    BOTH = 'both'


def __select_rule(
        wework_instance,
        message,
        rule: Rule
):
    rule_ = MsgRules(wework_instance, message)
    if rule == Rule.PRIVATE:
        return rule_.only_private()
    elif rule == Rule.GROUP:
        return rule_.only_group()
    elif rule == Rule.BOTH:
        return rule_.both()
    else:
        raise TypeError('仅能为 class:Rule')
