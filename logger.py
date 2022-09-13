#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import logging
from pathlib import Path

# from configparser import ConfigParser



# cfg = ConfigParser()
# cfg.read('./default.ini', encoding='utf-8')
# cfg.read('./custom.ini', encoding='utf-8')

def create_logger(loggername: str = 'logger', levelname: str = 'DEBUG', console_levelname='INFO'):
    levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    logger = logging.getLogger(loggername)
    logger.setLevel(levels[levelname])

    logger_format = logging.Formatter(
        "[%(asctime)s][%(levelname)s][%(filename)s][%(funcName)s][%(lineno)03s]: %(message)s")
    console_format = logging.Formatter("[%(levelname)s] %(message)s")

    handler_console = logging.StreamHandler()
    handler_console.setFormatter(console_format)
    handler_console.setLevel(levels[console_levelname])

    path = Path(__file__).parent/'logs'  # 日志目录
    # path = Path(cfg.get('prefers', 'logging_path'))
    path.mkdir(parents=True, exist_ok=True)
    today = time.strftime("%Y-%m-%d")  # 日志文件名
    common_filename = path / f'{today}.log'
    handler_common = logging.FileHandler(common_filename, mode='a+', encoding='utf-8')
    handler_common.setLevel(levels[levelname])
    handler_common.setFormatter(logger_format)

    logger.addHandler(handler_console)
    logger.addHandler(handler_common)

    return logger


# configs = dict(cfg._sections)
# caps = dict(configs['capability'])
# for key, value in caps.items():
#     if "true" == value.lower():
#         caps[key] = True
#     elif 'false' == value.lower():
#         caps[key] = False
#     else:
#         pass

# prefers = dict(configs['prefers'])
# for key, value in prefers.items():
#     if "true" == value.lower():
#         prefers[key] = True
#     elif 'false' == value.lower():
#         prefers[key] = False
#     else:
#         pass

# rules = dict(configs['rules'])
logger = create_logger('wechat')

if __name__ == "__main__":
    # for k, v in caps.items():
    #     print(k, v)
    pass