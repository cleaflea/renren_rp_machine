# -*- coding: UTF-8 -*-
import re
import sys
from renrenapi import RenRen
from accounts import accounts
from ntype import NTYPES

cookiePath = './login_cookie'

def refresh():
    if 'refreshrp.py' in sys.argv[0]:
        print 'condition1'
        bots = []
        for account in accounts:
            bot = RenRen()
            bot.login(account[0], account[1])
            print bot.email, 'login'
            bots.append(bot)
        return bots
    else:
        print 'condition2'
        bot = RenRen()
        if os.path.isfile(cookiePath):
            bot.loginByCookie(cookies)
            bot.email = ''
        else:
            account = accounts[0]
            bot.login(account[0], account[1])
        return [bot] if bot.token else []
   

if __name__ == '__main__':
    refresh()


