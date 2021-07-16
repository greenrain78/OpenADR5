import json
from logging import getLogger
from logging.config import dictConfig


log = getLogger(__name__)


def create_log_setting():
    # 로그 생성
    with open('Controller/loggers.json') as f:
        config = json.load(f)
        dictConfig(config)
    log.debug("create logger setting")
