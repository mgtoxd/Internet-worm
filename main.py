import threading
import time
from datetime import timedelta, date, datetime
import do
import os
from qiandao.main import doit

flag = 0


def go(id, pwd, seat, st, ed):
    while True:
        now = datetime.now().minute
        nowh = datetime.now().hour
        # print(str(id) + ' waitt ' + str(now) + ' hour ' + str(nowh))
        if now == 0 and nowh == 0:
            # time.sleep(2)
            for i in range(50):
                res = do.start_subscribe(id, pwd, seat, st, ed)
                print(res['msg'])
                time.sleep(0.5)
                if '当前时间预约冲突' in res['msg'] or '操作成功' in res['msg'] or '积分不足' in res['msg']:
                    return
        time.sleep(0.5)


def yy():
    print('go')
    tomorrow = (date.today() + timedelta(days=2)).strftime("%Y-%m-%d")
    t1 = threading.Thread(target=go,
                          args=(
                              '172100530', '212430', '100460413',
                              tomorrow + ' 8:00', tomorrow + ' 12:00',
                          ))
    t4 = threading.Thread(target=go,
                          args=(
                              '172100534', '151813', '100460413',
                              tomorrow + ' 16:00', tomorrow + ' 20:00',
                          ))

    #尤文萱
    t11 = threading.Thread(target=go,
                           args=(
                               '172050723', '243784', '100460287',
                               tomorrow + ' 8:00', tomorrow + ' 12:00',
                           ))
    t41 = threading.Thread(target=go,
                           args=(
                               '172050444', '200715', '100460287',
                               tomorrow + ' 16:00', tomorrow + ' 20:00',
                           ))
    #王涵
    t21 = threading.Thread(target=go,
                           args=(
                               '172100517', '213827', '100460415',
                               tomorrow + ' 8:00', tomorrow + ' 12:00',
                           ))
    t22 = threading.Thread(target=go,
                           args=(
                               '172120222', '161046', '100460415',
                               tomorrow + ' 16:00', tomorrow + ' 20:00',
                           ))
    t1.start()
    t4.start()
    t11.start()
    t41.start()
    t21.start()
    t22.start()


def qdd():
    doit()


# id, pwd, seat, st, ed, stt, edt
if __name__ == '__main__':

    while True:
        now = datetime.now().minute
        nowh = datetime.now().hour
        # print(' waitttttttttt ' + str(now) + ' hour ' + str(nowh))
        time.sleep(1)
        if now == 40 and nowh == 7:
            print(' 740 ' + str(now) + ' hour ' + str(nowh))
            qdd()
            time.sleep(60)
            continue
        elif now == 55 and nowh == 15:
            print(' 1555 ' + str(now) + ' hour ' + str(nowh))
            qdd()
            time.sleep(60)
            continue
        elif now == 55 and nowh == 23:
            print(' 2355 ' + str(now) + ' hour ' + str(nowh))
            yy()
            time.sleep(60)
            continue
