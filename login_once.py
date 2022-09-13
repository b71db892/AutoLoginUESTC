# !/usr/bin/env python
# -*- coding:utf-8 -*-
from BitSrunLogin.LoginManager import LoginManager
from config import login_options

if __name__ == '__main__':
    user = login_options['user']
    LoginManager(**login_options).login(username=user.user_id, password=user.passwd)
