# encoding=utf-8

import requests
import logging

from .tools import json

logger = logging.getLogger(__name__)

API_URL = 'https://oapi.dingtalk.com/robot/'


class APIError(object):
    def __init__(self, code, msg):
        self.code = code
        self.message = msg


class DingDingBot(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def _process_response(self, rsp):
        data = {
            "code": 0,
            "msg": "success",
        }

        if rsp.status_code != 200:
            data['code'] = rsp.status_code
            data['msg'] = u'Http Error'
        try:
            content = rsp.json()
            if 'errcode' in content and content['errcode'] != 0:
                data['code'] = content.get('errcode', 9999)
                data['msg'] = content.get('errmsg', u'')
        except:
            data['code'] = 9999
            data['msg'] = u'Invalid Rsp'

        return data

    def _post(self, path, data, ctype='json'):
        headers = {'Content-type': 'application/json'}

        path = API_URL + path

        if '?' in path:
            path += '&access_token=' + self.access_token
        else:
            path += '?access_token=' + self.access_token
        if ctype == 'json':
            data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        rsp = requests.post(path, data=data, headers=headers, verify=True)
        return self._process_response(rsp)

    def send_text(self, text, at=None, is_all=False):
        if at and isinstance(at, list):
            raise TypeError(u'at must be a list!')

        at = at if at else []

        data = {
            "msgtype": "text",
            "text": {
                "content": text,
            },
            "at": {
                "atMobiles": at,
                "isAtAll": is_all
            }
        }

        rsp = self._post('send', data)
