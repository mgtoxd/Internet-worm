import requests
import json
from qiandao.send_email import send_email2


mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "mtcode1024@163.com"  # 用户名
mail_pass = "CDDEHUGOTSNVOXQV"  # 授权密码，非登录密码
def start_subscribe(id, pwd, seat, st, ed):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63'
    }
    data = {
        'id': id,
        'pwd': pwd,
        'act': 'login'
    }
    response = requests.post('http://211.82.175.12:8080/ClientWeb/pro/ajax/login.aspx', headers=headers, data=data)
    cookie = response.cookies

    data = {
        'dialogid': '',
        'dev_id': seat,
        'lab_id': '',
        'kind_id': '',
        'room_id': '',
        'type': 'dev',
        'prop': '',
        'test_id': '',
        'term': '',
        'number': '',
        'classkind': '',
        'resv_kind': '',
        'test_name': '',
        'start': st,
        'end': ed,
        'start_time': '',
        'end_time': '',
        'up_file': '',
        'memo': '',
        'act': 'set_resv',
        '_': '1602208025087'
    }
    response = requests.get('http://211.82.175.12:8080/ClientWeb/pro/ajax/reserve.aspx', headers=headers,
                            cookies=cookie,
                            data=data)
    
    return json.loads(response.text)