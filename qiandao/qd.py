# http://update.unifound.net/wxnotice/s.aspx?c=100455363_Seat_100460084_1CR
# http://update.unifound.net/wxnotice/s.aspx?c=100455363_Seat_100460082_1CR
# CDDEHUGOTSNVOXQV
import requests
from urllib import parse
infoMS = {
    'user': '172100530',
    'pwd': '212430',
    'url': 'http://update.unifound.net/wxnotice/s.aspx?c=100455363_Seat_100460413_1CR'
}
infoWS = {
    'user': '172020926',
    'pwd': '080323',
    'url': 'http://update.unifound.net/wxnotice/s.aspx?c=100455363_Seat_100460084_1CR'
}
infoMX = {
    'user': '172100534',
    'pwd': '151813',
    'url': 'http://update.unifound.net/wxnotice/s.aspx?c=100455363_Seat_100460413_1CR'
}
infoWX = {
    'user': '172100527',
    'pwd': '206911',
    'url': 'http://update.unifound.net/wxnotice/s.aspx?c=100455363_Seat_100460084_1CR'
}


# 上午为true，马为true
def qiandaoya(time, person):
    info = {}
    if time:
        if person:
            info = infoMS
        else:
            info = infoWS
    else:
        if person:
            info = infoMX
        else:
            info = infoWX
    cookie = {
        'ASP.NET_SessionId': '5jqs3h3xw5xtnl55exhenv2l',
        '_d_id': 'c0e0148fd2dc377b61098cceec85ce'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63'
    }
    # print(info['url'])
    response = requests.get(info['url'],
                            headers=headers,
                            allow_redirects=False)
    #print('2')
    #print(response.text)
    params = parse.parse_qs(parse.urlparse(response.headers['Location']).query)
    requests.get(response.headers['Location'], headers=headers, cookies=cookie)

    data2 = {
        'DoLogon': 'true',
        'sysidform': '1CR',
        'aluseridform': str(params['msn']),
        'wxuseridform': '',
        'szLogonName': info['user'],
        'szPassword': info['pwd'],
    }
    response = requests.post('http://lib.imufe.edu.cn:8080/Pages/WxSeatSign.aspx', headers=headers, data=data2,
                             allow_redirects=True, cookies=cookie)
    #print(response.text)
    if '已签到' in response.text:
        msg = '已经签到啦，不用再签到啦'
    elif '请选择使用时长' in response.text:
        data = {
            'DoUserIn': 'true',
            'dwUseMin': '240'
        }
        response = requests.post('http://lib.imufe.edu.cn:8080/Pages/WxSeatSign.aspx', headers=headers, data=data,
                                 cookies=cookie)
        if '使用截止时间' in response.text:
            msg = '现场签到成功啦'
        else:
            msg = '现场没签到成功啊，快手动签到啊啊啊'
    elif '预约已生效' in response.text:
        response = requests.get('http://lib.imufe.edu.cn:8080/Pages/WxSeatSign.aspx?Userin=true', headers=headers,
                                cookies=cookie)
        if '签到成功' in response.text:
            msg = '签到成功啦'
    elif '设备已分配给他人使用' in response.text:
        print('go')
        msg = '嘿，不是这个号约的座位啊'
    else:
        msg = '不知道出啥错啦'
    return info['user'] + msg
