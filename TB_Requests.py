import requests
from bs4 import BeautifulSoup
import re

login_address = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9RKrfEP&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
login_check_username_address = 'https://login.taobao.com/newlogin/account/check.do?appName=taobao&fromSite=0'
username = '15804771016'
password = '5256fca1aa8770327c64cefc408a5100821a72a0df35468cdb1504bff215fe7992c40507e3e9d0134fafb57f2ffaf44660e9389073b109ba1ddf8cf2f66f8ce43ffa3270f1f6af25583a18444243ad5fe12a4f1c068c8470d2646a9de92fb6bbfd22a5d40f1a5b392463d0be884789167cea622b61e5f9db88d963ec7dbbf849'
login_ua = '137#gtc9hE9o96iPAWm0C9HcVwg6IQr7+qvGaplk0Ubwe6ayrERqJzMaDVa1E/0zlT3CY3ADtOGJdiiUMbH1TIyTJ/7Ymk7O5CexyjoOseVygReABJdFNTg0WqKpgfEo67SICWroSUl2sl8YwXu6+piKqwObft7HpvDmX94D22zhPf7t22gqX9+7KtfG588Vdb2cJGRrxFBjVX09inxWP88R6dDF6NnDXyq6LjcKikoviCP3NJCZGvLGJerhSs0hdWikIC/SMWsuZ/czGm7bMGMGnx+Y/pYJjQppNkl7i4RyQ9QChJ2U7eqSu8vJ+fz5jJxuAYWij69p01NlWH368Me/0lgqjeafHgGURUbjW2qApo6wBubgkbDDhWFNgRWreJqlrr2DcxboJoedB1AsMxssuANjuLId4j8RWzOlj3HOPEL4Xxwp5XR3AezPNzToOqvtmhI7/f0CGUNDYfCtZo+JIQoAE8ZCJSQ/Eylwb3gbQM+l+MSTmSWau6MD19dYLyX1VwDDRvtG0bhkNJ1GyRo9ovVwxeaEwselnp7zPcJ5FeJmv0AQChzMOUqmQofJ+GxVKGCH1olRPBqVaSOx1leCd1NZQLR29cxppkJEgHtAutppYSUS1lQypXiwQonoBf6b5nVc1IBi+piVYSUx1lLyodicQoneOpgSyRUjD4KyAYqnYSJS1qQipBqmQofJ+GXpVkJc1Iey+tpVYTUx1lgippyr9G1EdkP9iIS2KKOdtt9B/Y360kdpbYdliEUzQNTK0utT7Y0O91PHjHWZurkEYmVJMtOwrtsr66wPtG67BGH9beSeDX/YK42sJHqW8RdX1Z6y2a1RunGzU7FSF3rrE3yvYrQTCc0q4e6FCc2+95SPSGDXiwFFj8EupBUYOYVQXZhyzhqCrbAwKdgC6gHij7AqiLXd6Eh1j1NPj8Ff3+DMudLtfHxamqNc5A5hk2z39oMU66aIEN2BtyJwQAxYVsTCklb1VlvZvaC6b9wRyhYdNof3D6lEbe2XXcHadS02n//NwHjmmP4H+a6+ntI/bqRsAvzyxncCm0jEhuMUtJOCCalRf9NuLemtxJYrISJLLlQxWSkTHfmvMsfANPMWyRTKjoNaBPPI9aYZ/2hxRzV0j/rVByBspgRbu3V9aDL6MX11+FquIQXBeLJ1/PNAo121J98kZ7u2fRMs4vsCmkebnEBh7GDtdF03kA7czwP6uQp3s93PT0IIZVkqr8NM7T4JHmfNWsNEBByDPAhjGakGwtDUpIkwFk8HcE84o+vGSGuLA/Qg9VDp'
login_check_address = 'https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0'

headers = {
    # 'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'h-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}


def login():
    login_headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://login.taobao.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        "Referer": 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9VirIGi&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F',
    }
    login_data = {
        'loginId': username,
        'password2': password,
        'keepLogin': 'false',
        'ua': login_ua,
        'umidGetStatusVal': '255',
        'screenPixel': '1280x720',
        'navlanguage': 'zh - CN',
        'navUserAgent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36',
        'navPlatform': 'Win32',
        'appName': 'taobao',
        'appEntrance': 'taobao_pc',
        '_csrf_token': 'SZy43THjYps2bf9HnR7Gr6',
        'umidToken': '799dcee8122ea02f0613aa936062f9921dd2a1c8',
        'hsiz': '107a29d13fae6dfacdf429a56f1126f2',
        # 'bizParams':
        'style': 'default',
        'appkey': '00000000',
        'from': 'tbTop',
        'isMobile': 'false',
        'lang': 'zh_CN',
        'returnUrl': 'https: // www.taobao.com /',
        'fromSite': '0',
    }
    response = s.post(login_check_address, headers=login_headers, data=login_data)
    print(response.text)
    st_token_url = re.compile('"redirectUrl":"(.*)",').findall(response.text)
    my_taobao_url = st_token_url[0]
    print(my_taobao_url)
    response = s.get(my_taobao_url, headers=headers)
    st_token_url = re.compile('href="//cart.taobao.com/cart.htm\?nekot=(.*)" target="_blank').findall(response.text)
    my_cart_url = "https://cart.taobao.com/cart.htm?nekot=" + st_token_url[0]
    print(my_cart_url)
    response = s.get(my_cart_url, headers=headers)
        # re.compile('"//cart.taobao.com/cart.htm?nekot=(.*)"')
# //cart.taobao.com/cart.htm?nekot=
# < a
# href = "//cart.taobao.com/cart.htm?nekot=1470211439694"
# target = "_blank"
# role = "menuitem"
# data - spm = "d1000367" > 我的购物车 < / a >
# href="//cart.taobao.com/cart.htm?nekot=1470211439694" target="_blank" role="menuitem"

def check_username():
    check_username_data = {
        'loginId': username,
        'ua': login_ua,
    }
    response = s.post(login_check_username_address, data=check_username_data)
    need_code = response.json()['needCode']


if __name__ == '__main__':
    s = requests.session()
    # check_username()
    login()
