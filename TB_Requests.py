import requests
import re

login_check_username_address = 'https://login.taobao.com/newlogin/account/check.do?appName=taobao&fromSite=0'
username = '15804771016'
password = '5256fca1aa8770327c64cefc408a5100821a72a0df35468cdb1504bff215fe7992c40507e3e9d0134fafb57f2ffaf44660e9389073b109ba1ddf8cf2f66f8ce43ffa3270f1f6af25583a18444243ad5fe12a4f1c068c8470d2646a9de92fb6bbfd22a5d40f1a5b392463d0be884789167cea622b61e5f9db88d963ec7dbbf849'
login_ua = '137#Lzc9hE9o9iDh9a6khcOYsH9GIn9bVM1bwUuKtlKESP0CLn5LoR2OXC7N+RfxR5JwLoXitUCzLa/UGdM0P44xRhwntukL2VTMMTzhQ0Rg+l3oVX99xQs437xCKM5sy/KCwDefr+DVcJgb75dU3rkxAvABEg9rsCwTIJUlVhtOTJocudPJf3PIFxjf0aI875Qj0QG6o7tVX8IU9rTWQxVg7jzzMP7t7hlxHBrhsqg60FB+R5j9lggW64m1N13z9BbGiCxYJ5xqCJjsPUKzDc6DT0D5SpR8MN4G0Ux1Eado1+FT/pqEC1MqHMPJqy8zusGHByv8gvrTD4I1m7SDg7uzk9HXGjbSv8fcJQmcC40t97UWkRiUjDge93YE6ifr9A+AM0e70T0ZxkE1TeSuyuyZ2eyGG4JWQTrVaMDblsyzkcJKMOb195A0R3nEYTUx1lg8pD7jQARk0G7Vak1h1pgM0dIXMSOx1qeIpppE24hFLS7ppRUc1Aey+tIvYSUxKh7F5XWcQeVo+ZDVpRUm1ATyutiVYSUF2+DEyXij3HmJsRlnpRJc1Iei+cqpYSJS1qQiVppcQenJ+ZXVpkUm1AEy+pyp9GrTTtP9iIS2aOe0zfJw6gAHXAbksSx7cCyKkWpbnUtl+eUd8TdHEfnBangQlE7JG/YhjSOmp/uhNAI6PJHqdUJR2Utfio6D0gvHna1e0/53jy0IJ6tMJSL2EoyPOiBO1VuuArekgUeoT9z/EtZy/5pjCYRLZRtS2ZqvkdXLQc2C6UBHMoHK6+P43TlNghSBVaAj/2FQ54SJTf+Lf8Vj/XVa0fYr1ceJj18JuywaX8exzmVj2UdR75HQ6cq0X6+tYNerelQEH1oMouI/DoHuWtHrub0tGIur48qCxoNCBpB4uflukIEYHZoDRaMlFr53quuspftydUjk6+Mv0lfJCAFe132juICs+Qr/zaRi9oJqWWTl+eQNldXw1p3PnWJa+h4PQHD/y4aHJ5WtJVMZYj3+z5hLPaj7gcRXolNLb7g+f2LQ0TBKJQAdGOXUvOhrfNfkAWXQIVhZBTfWRa5QalOHefHeQ3Wy4cW7nmLBjJ/zOflQEJXnd8vVydwXWxOT8LIZmFh2rFmuQio5jR2o+9AjSK/r+IkHSIm3XCPZ2VRTp334ZXbR0eIlBhBK2DIM6yVn50KdoVVhZuuYAjCiiB=='
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


def detail(response):
    detail_url = "https://detail.tmall.com/item.htm?id=" + re.compile('"//detail.tmall.com/item.htm\?id=(.*)","weight"').findall(response.text)[0]
    response = s.get(detail_url, headers=common_headers)
    print("成功跳转到商品详情页面" + detail_url)

    detail_data = {
        'from': 'itemDetail',
        'var': 'login_indicator',
        'id': re.compile('"itemId":"(.*)","validatorUrl"').findall(response.text)[0],
        'shop_id': re.compile('shopId:"(.*)",startTime').findall(response.text)[0],
        'cart_ids':'',
        't': re.compile("renderTime:\'(.*)\',").findall(response.text)[0]+'000',
    }
    response = s.get('https://buy.tmall.com/login/buy.do', headers=common_headers,data=detail_data)

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
    # res = purchase(res, '1')
    res = detail(res)
