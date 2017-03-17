## 钉钉机器人简易版

钉钉机器人简单整合，封装了一下钉钉群聊机器人的接口，可以发送文字、链接和markdown格式，支持logger方式发送文字，监控代码日志。


安装
----------------
`git clone git@github.com:lpig/dingding_bot.git`
`python setup.py install`



使用
----------------


发送消息::

    from dingding_bot import DingDingBot
    bot=DingDingBot(access_token)
    bot.send_text("这是文字消息")


logger模块::

    from dingding_bot import get_dingding_logger
    logger=get_dingding_logger(access_token)
    logger.info("日志输出")


###TODO

 - 支持django框架使用
 - etc.