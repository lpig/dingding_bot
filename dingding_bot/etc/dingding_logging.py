# encoding=utf-8

import requests
import logging

from dingding_bot.api.bot import DingDingBot

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


def get_dingding_logger(access_token, name=None, level=logging.WARNING):
    _logger = logging.getLogger(name=name)
    _logger.setLevel(level)
    _logger.addHandler(BotLoggingHandler(access_token))

    return _logger
