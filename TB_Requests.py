import requests
import re

login_check_username_address = 'https://login.taobao.com/newlogin/account/check.do?appName=taobao&fromSite=0'
username = '15804771016'
password = '5256fca1aa8770327c64cefc408a5100821a72a0df35468cdb1504bff215fe7992c40507e3e9d0134fafb57f2ffaf44660e9389073b109ba1ddf8cf2f66f8ce43ffa3270f1f6af25583a18444243ad5fe12a4f1c068c8470d2646a9de92fb6bbfd22a5d40f1a5b392463d0be884789167cea622b61e5f9db88d963ec7dbbf849'
login_ua = '137#n5B9hE9o9CCqQQ/RpcJyLhcGInQeeQ0WEPNBUtQhoB+Tl5THTjJFSe2f8Ki3q2x/blSdCZF5Oo8fp4E97Ej+rN7po5zACRTmiUsmbRN3m5+9Sf5MwrvMvykxEcp6ErT3YV59VOjh5OMOmaJDTGpyp4ZpDoxhFAJ/lWezhuNTGAr+8+RHTuW0uKAN4bfLsfwg4uPCWZCAXIct9iWXeT1ho3X8Yqd9o0vXmMeXgsl6qn45pgET899L+GDIAyAueh70HaHoYRNa5jFTNql9+lnqOnDcj2sdrAN83LGIRdE20a5NUgepsza5+jAme0m0xyt2hv9zubvJAE8rCs3vD5hpY7tZ9GSwR6LHvGxw73QHPxJr9A+AM0e70T0Xi7PC+SPbfiJkz5eqwSwwieml14BUBu9RFFAhk0Jc1IeivtksbSJSklIPpId7QeQI+GDV9uJm1ie964SYYTJS1lQypXicQobJ+ZXW0mMS0eeidtpVYSUS1lgihtGKYeUJ8vxk/xOrCodTI0iV5oSk1LFAqppmQofJ+GQ9pkUm1AEy+pXpYSJS1lQipXpcQeno+ZXVucvIrK7p9+VUzDvGaeIcaS/UqOhDH8ZIUCpQYjouD3lsYqwcj7XzgHyw4YYCyW3X2yVWGPdOgJOWWMwrxTYhuFXiY/lQI94B5GI6fOajv64nkirCqTw+ZLTAyX+7KR/rlJiegXvRAfuaVHHPi7lb3Nsq+/rMLRz1GljhOhsF4J4sb41uz3a479XkQed8p1qxqYE4x3jMvcfXk2soJrXcPuoO8SG262Gplc3y5sGWGCgoDHDZBmns1LumRwTmmTC9UhN+7K8oXV4PywHSrjT4i1KnkCLHsW9tD1axzU1ZZtT0652I24NbYgqPICM9CDFPTkmwK/RhHe4X8joL9trcMK5ns85McGEVHe8JD0mRNEf8gzVxajNi0QIdDd27pRIsF6Bpny241Vk5hvvshU4mw8oZfal/tUVgrQ/Pe1ja6qLRY1sBUFlO7G6/K98KzgSfNHpHC7G8xtmI1MOKpGeQQOTBvlRZNhnQm4ZuO1JaZsP3tuM8EzpxEAupvkwLt5YP0mxAUNfXPjp2vFeWKxwP2oRwnNpM8w9edl8WuRy2BuwYAI/+WUyor0I7Pqrwvc4/kPrez8pCF3p8ocfX'
login_address = 'https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0'
pre_purchase_address = 'https://cart.taobao.com/json/AsyncUpdateCart.do'
purchase_address = 'https://buy.tmall.com/login/buy.do?from=cart'

common_headers = {
    # 'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'h-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}


def check_username():
    check_username_data = {
        'loginId': username,
        'ua': login_ua,
    }
    response = s.post(login_check_username_address, data=check_username_data)
    need_code = response.json()['needCode']


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
    # 登录
    response = s.post(login_address, headers=login_headers, data=login_data)
    print(response.text)
    st_token_url = re.compile('"redirectUrl":"(.*)",').findall(response.text)
    # 获得登陆成功后跳转url
    my_tb_url = st_token_url[0]
    # 跳转淘宝首页
    response = s.get(my_tb_url, headers=common_headers)
    print('登录成功，我的淘宝首页' + my_tb_url)
    return response


def my_cart(response):
    st_token_url = re.compile('href="//cart.taobao.com/cart.htm\?nekot=(.*)" target="_blank').findall(response.text)
    # 获得我的购物车url
    my_cart_url = "https://cart.taobao.com/cart.htm?nekot=" + st_token_url[0]
    # 跳转我的购物车页面
    response = s.get(my_cart_url, headers=common_headers)
    print("成功跳转我的购物车页面" + my_cart_url)
    return response


def purchase(response, quantity):
    shop_id = re.compile('"bundles":\["(.*)"],').findall(response.text)[0]
    cart_id = re.compile('"cartId":"(.*)","checked"').findall(response.text)[0]
    sku_id = re.compile('"skuId":"(.*)","skuStatus"').findall(response.text)[0]
    item_id = re.compile('"itemId":"(.*)","leafCategory"').findall(response.text)[0]
    time = re.compile('"currentTime":(.*),"diffTairCount"').findall(response.text)[0]

    cart_headers = {
        # 'Connection': 'keep-alive',
        # 'Cache-Control': 'max-age=0',
        # 'Origin': 'https://cart.taobao.com',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        # 'Content-Type': 'application/x-www-form-urlencoded',
        "referer": 'https://cart.taobao.com/cart.htm?spm=a1z02.1.1997525049.1.jg86dk&from=mini&pm_id=1501036000a02c5c3739',
    }

    cart_data = {
        '_input_charset': 'utf-8',
        'tk': '3b3579653de81',
        'data': [{
            'shopId': shop_id,
            'comboId': '0',
            'shopActId': '0',
            'cart': [{
                'quantity': quantity,
                'cartId': cart_id,
                'skuId': sku_id,
                'itemId': item_id
            }],
            'operate': [],
            'type': 'check'
        }],
        'shop_id': '0',
        't': time,
        'type': 'check',
        'ct': 'f2c8b39be0bab415eb154e365daa0345',
        'page': '1',
        '_thwlang': 'zh_CN',
    }

    s.post(pre_purchase_address, headers=cart_headers, data=cart_data)
    response = s.get(purchase_address, headers=common_headers)
    return response


if __name__ == '__main__':
    s = requests.session()
    # check_username()
    res = login()
    res = my_cart(res)
    res = purchase(res, '1')
