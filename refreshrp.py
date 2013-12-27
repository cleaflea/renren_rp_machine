# -*- coding: UTF-8 -*-
import re
import sys
from renrenapi import RenRen
from accounts import accounts
from BeautifulSoup import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

allrp_pattern = re.compile(r"<b id='bTotalRpNum'>.*?</b>")
todayrp_pattern = re.compile(r"<b id='bTodayRpNum'>.*?</b>")
cookiePath = './login_cookie'

def getRP(content):
    html = str(content)
    #print html
    soup = BeautifulSoup(html)
    rp = soup.findAll('span', {'class': 'totalRp'})
    #print len(rp)
    rp_all = soup.findAll('b', id='bTotalRpNum')
    rp_today = soup.findAll('b', id='bTodayRpNum')
    #print len(rp_all)
    #print len(rp_today)
    #print rp_all[0].text
    #print rp_today[0].text
    rp_all_num = rp_all[0].text
    rp_today_num = rp_today[0].text
    return rp_all_num, rp_today_num

def refresh():
    if 'refreshrp.py' in sys.argv[0]:
        print 'condition1'
        bots = []
        for account in accounts:
            bot = RenRen()
            bot.login(account[0], account[1])
            #print bot.email, 'login'
            homepage = bot.getHomePage()
            all_rp, today_rp = getRP(homepage)
            print "%s login and all_rp is %d, today_rp is %d" % (str(bot.email), int(all_rp), int(today_rp))
            bots.append(bot)
        return bots
    else:
        print 'condition2'
        bot = RenRen()
        if os.path.isfile(cookiePath):
            bot.loginByCookie(cookies)
            bot.email = ''
            homepage = bot.getHomePage()
            all_rp, today_rp = getRP(homepage)
            print "%s login and all_rp is %d, today_rp is %d" % (str(bot.email), int(all_rp), int(today_rp))
        else:
            account = accounts[0]
            bot.login(account[0], account[1])
            homepage = bot.getHomePage()
            all_rp, today_rp = getRP(homepage)
            print "%s login and all_rp is %d, today_rp is %d" % (str(bot.email), int(all_rp), int(today_rp))
        return [bot] if bot.token else []
   

if __name__ == '__main__':
    refresh()


