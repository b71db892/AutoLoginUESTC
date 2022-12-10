#!/usr/bin/env python
# -*- coding:utf-8 -*-
import ctypes
import os, sys
import time
import platform
from logger import logger
from BitSrunLogin.LoginManager import LoginManager
from config import *

# 获取计算机名
host_name = platform.node()
try:
    #  disable the QuickEdit and Insert mode for the current console
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)
except:
    pass

def is_connect_internet(test_ip):
    if platform.system().lower().startswith('windows'):
        cmd = u"ping {} -n 1".format(test_ip)
    else:
        cmd = u"ping {} -c 1".format(test_ip)
    status = os.system(cmd)
    return status == 0

def always_login(user=None, test_ip=None, delay=2, max_failed=3, **kwargs):
    time_now = lambda: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    org_delay = delay
    failed = 0
    logger.info(f'[{time_now()}] [{host_name}] NetWork Monitor StartUp.')
    while True:
        if not is_connect_internet(test_ip):
            failed += 1
            delay = max(0., delay / 2)
            if failed >= max_failed:
                logger.info(f'[{time_now()}] [{host_name}] offline.')
                LoginManager(**kwargs).login(username=user.user_id, password=user.passwd)
        else:
            if failed >= max_failed:
                logger.info(f'[{time_now()}] [{host_name}] online now.')
            failed = 0
            delay = org_delay
        time.sleep(delay)
    


if __name__ == "__main__":
    id = os.environ.get('LOGIN_ID')
    passwd = os.environ.get("LOGIN_PASSWORD")
    service_provider = os.environ.get("SERVICE_PROVIDER")
    location = os.environ.get("LOCATION")
    testip = os.environ.get("PINGIP")
    if id is None or passwd is None or service_provider is None or location is None:
        print("请配置环境变量LOGIN_ID LOGIN_PASSWORD SERVICE_PROVIDER LOCATION PINGIP", flush=True)
        sys.exit(1)
    login_options['user'] = User(id, passwd, None)
    login_options['ac_id'] = location
    login_options['domain'] = '@' + service_provider
    login_options['test_ip'] = testip
    while True:
        try:
            always_login(**login_options)
        except:
            import traceback

            error = traceback.format_exc()
            logger.error(error)
            time.sleep(15)
