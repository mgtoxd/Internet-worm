import threading
import time
from datetime import timedelta, date, datetime
import sys

sys.path.append('C:/Users/mtx/Desktop/Internet-worm')
from qiandao.qd import qiandaoya
from qiandao.send_email import sendEmail
import os

mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "mtcode1024@163.com"  # 用户名
mail_pass = "CDDEHUGOTSNVOXQV"  # 授权密码，非登录密码


def doit():
    while True:
        now = datetime.now().minute
        nowh = datetime.now().hour
        # print(' wait ' + str(now) + ' hour ' + str(nowh))

        if now == 45 and nowh == 7:
            sendEmail('上午签到', qiandaoya(True, True), ['2359971480@qq.com', 'mtcode1024@163.com'])
            return

        if now == 0 and nowh == 16:
            sendEmail('下午签到', qiandaoya(False, True), ['2359971480@qq.com', 'mtcode1024@163.com'])
            return
        time.sleep(2)


if __name__ == '__main__':
    doit()
