# encoding=utf-8
import re
from setuptools import setup, find_packages

with open('dingding_bot') as fp:
    version = re.search(r"__version__\s*=\s*'([\w\-.]+)'", fp.read()).group(1)

long_description = u'简易钉钉机器人'
url = u'https://github.com/lpig/dingding_rot'

setup(name="wechat",
      version=version,
      description=long_description,
      maintainer="Lpig",
      maintainer_email="o55662000@yeah.net",
      url=url,
      long_description=long_description,
      install_requires=['requests'],
      packages=find_packages('.'),
      )
