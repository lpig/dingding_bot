# encoding=utf-8
import sys

from etc.dingding_logging import *
from api.bot import DingDingBot

__title__ = 'dingding_bot'
__version__ = '0.0.2'
__author__ = 'Lpig'
__license__ = 'MIT'

version_details = 'wxpy {ver} from {path} (python {pv.major}.{pv.minor}.{pv.micro})'.format(
    ver=__version__, path=__path__[0], pv=sys.version_info)

VERSION = __version__
