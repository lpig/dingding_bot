# encoding=utf-8

import requests
import logging

from dingding_rot.api.bot import DingDingBot

_logger = logging.getLogger(__name__)

__all__ = ['get_dingding_logger']


class BotLoggingHandler(logging.Handler):
    def __init__(self, access_token):
        self.access_token = access_token

        super(BotLoggingHandler, self).__init__()

    def emit(self, record):

        bot = DingDingBot(self.access_token)

        try:
            bot.send_text(self.format(record))
        except:
            _logger.exception(u'发送消息出错')


def get_dingding_logger(access_token, name=None, level=logging.INFO):
    _logger = logging.getLogger(name=name)
    _logger.setLevel(level)
    _logger.addHandler(BotLoggingHandler(access_token))

    return _logger


if __name__ == "__main__":
    logger = get_dingding_logger('825cf681c0f7a9db1444934cce79326b8f2a6eadb7cfef53422ee3f6c6f6f8a3')
    logger.warning("test")
    try:
        1 / 0
    except:
        logger.exception(u"出错了")
