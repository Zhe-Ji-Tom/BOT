import requests
import re
import time

login_check_username_address = 'https://login.taobao.com/newlogin/account/check.do?appName=taobao&fromSite=0'
username = '15804771016'
password = '5256fca1aa8770327c64cefc408a5100821a72a0df35468cdb1504bff215fe7992c40507e3e9d0134fafb57f2ffaf44660e9389073b109ba1ddf8cf2f66f8ce43ffa3270f1f6af25583a18444243ad5fe12a4f1c068c8470d2646a9de92fb6bbfd22a5d40f1a5b392463d0be884789167cea622b61e5f9db88d963ec7dbbf849'
login_ua = '137#grE9hE9o9Vm1mpAtCBHFRNg6IQr70ZOwhCFpUt68BE2/XsZMYS1Qof5gHBQQ6CCmQdUzUhb5qI/sJxclPdpk164o4ir9PiCnhzs7IDJXJOAxvrcePoX8g2inBEssgeaMmvbNYpBEmFQ1YdIZalH6Qd1QqZ9FQQo7iG9ZGujnqMqP/g7aifbvFe9l25fKCk99G7iR9aDow+MO0DezpbITh6Gn/W7u/8RgR7WuFKvHGEcVQLK9rvZOadhGmuySXxFXhzuJJmc27T3qhAKvw9BpSPyEXlLmjjZQoTlrjhFludx5EOuvekenwqBCUGaxawkwQFX3yUVJ2eC8xXty+BEIjP1b9BaFeZWAkXEIQrrJnGGTR0NbsFigQZUxd7v/jsnNfA4SDZ22ZgbG7yL8lcpqr3E4+Bo2myfgyCel9zSulXZWaTObnor+PVejsjBxiL5PvVZU4mo2Rnclj1Y55Uvtr4nRUer80Uj2nrQ/Eylwb3gbQMvp5J6DWXR6q4y1xhOjx1ciA5GxoFz81/jIE4/ShsLxTMoN7p/b7/8eZJfhR5/QYTUx1lg8pLucQAfo+l2dUu+mMgK4HXCf6y+xtXNW9tpmQFLhIAmVpkJc1Aey+tiVYSmS1lX90tASxInodG6VpRUc1AEy+tBEYSUS13gy7EQ0QSbay+mxc9bc1Iei+pppYrJS1qQipXPfQeno+ZDVpkUm1AEy+pipYvcq0M2WpBqXEnTYmrwXjV5vnGZBAjQBS2Btp/53U/TXHQnYBn7r7qWEymlay6bYLhAqCoEU1drukR43RGOo3VH3k2EJ3GgXn/mAqxJGS2GWECPE6mEeveh9mp6Y0An4jMofBH5/yziw35pamjKx4CkwYXWQsgIsASOYZfJQTnDnv5v6LlW8MpbOVPY6S5PYS+sxdfekHp/kXFFtYU0HmzlaPqLFEDLuWKpuYlhyO3ddYVBjRE6PR/pDVIzvPbRZQ92/eCcKECLaShq/sC5+tqnbRaRPnrXveReZ7QC5X2T2YVtVqgKaOml6lwqLMH072rxSiQNkbp361CyjhqYfKjsMvZLqziqjRQPOBvdGmL0NY+LCJRo74FI0NImFjU0oJP2h3p3+PBr2ISFUd35N99njOVTg8gppbrRv+Kv+XBRbMg6VjwsCGo+pAbDL1ftFz0IBdVNwVO2gdOdojp/Fxs6L38FKZTV0N9eqGiSofKWhjSiNnqFHBwwuBbtdqNuAFsEQgS+KzQf6BcVG765t7vdpYCLHjs7kyoy3bOyXTldxebRMAgmqyhmruNy5xfrLzG0B7YYwstPAYaG0vKk5YusdGM8pitngTwOy'
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
    # 验证账号密码
    response = s.post(login_address, headers=login_headers, data=login_data)
    print(response.text)

    # # 获取st码申请地址
    # st_token_url = re.compile('"asyncUrls":\["(.*)"\]').findall(response.text)[0]
    # response = s.get(st_token_url, headers=common_headers)
    # # 获取st码
    # st = re.compile('"data":{"st":"(.*)"}').findall(response.text)[0]
    # print(st)
    #
    # headers = {
    #     'Host': 'login.taobao.com',
    #     'Connection': 'Keep-Alive',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    # }
    #
    # response = s.get('https://login.taobao.com/member/vst.htm?st={}'.format(st), headers=headers)

    # 获得登陆成功后跳转url
    my_tb_url = re.compile('"redirectUrl":"(.*)",').findall(response.text)[0]
    # 跳转淘宝首页
    response = s.get(my_tb_url, headers=common_headers)
    print('登录成功，我的淘宝首页' + my_tb_url)

    return response


def my_cart(response):
    # 获得我的购物车url
    my_cart_url = "https://cart.taobao.com/cart.htm" + re.compile('href="//cart.taobao.com/cart.htm(.*)" target="_top"').findall(response.text)[0]
    # 跳转我的购物车页面
    response = s.get(my_cart_url, headers=common_headers)
    print("成功跳转我的购物车页面" + my_cart_url)
    return response

def detail(response):
    detail_url = "https://detail.tmall.com/item.htm?id=" + re.compile('"//detail.tmall.com/item.htm\?id=(.*)","weight"').findall(response.text)[0]
    response = s.get(detail_url, headers=common_headers)
    print("成功跳转到商品详情页面" + detail_url)

    detail_params = {
        'from': 'itemDetail',
        'var': 'login_indicator',
        'id': re.compile('"itemId":"(.*)","validatorUrl"').findall(response.text)[0],
        'shop_id': re.compile('shopId:"(.*)",startTime').findall(response.text)[0],
        'cart_ids':'',
        't': re.compile("renderTime:\'(.*)\',").findall(response.text)[0]+'000',
    }

    detail_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'referer': detail_url,
    }

    item_id = re.compile('itemId=(.*)&showShopProm').findall(response.text)[0]
    u_id = re.compile('userid=(.*)&at_isb').findall(response.text)[0]
    purchase_url = 'https://buy.tmall.com/order/confirm_order.htm?x-itemid={}&x-uid={}'.format(item_id, u_id)

    purchase_data = {
        'seller_id': re.compile('ownerid=(.*)&').findall(response.text)[0],
        'quantity': '1',
        'item_id_num': item_id,
        'item_id': item_id,
        'auction_id': item_id,
        'destination': '330100',
    }
    purchase_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'referer': 'https: // detail.tmall.com / item.htm?spm = a1z0d.6639537.1997196601.4.4e337484vs97Dj & id = 607745631129 & skuId = 4261072948810',
        'origin': 'https://detail.tmall.com',
        'upgrade-insecure-requests': '1',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = s.get('https://buy.tmall.com/login/buy.do', headers=detail_headers, params=detail_params)
    response = s.post(purchase_url, headers=purchase_headers, data=purchase_data)

def purchase(response, quantity):
    shop_id = re.compile('"bundles":\["(.*)"],').findall(response.text)[0]
    cart_id = re.compile('"cartId":"(.*)","checked"').findall(response.text)[0]
    sku_id = re.compile('"skuId":"(.*)","skuStatus"').findall(response.text)[0]
    item_id = re.compile('"itemId":"(.*)","leafCategory"').findall(response.text)[0]
    # time = re.compile('"currentTime":(.*),"diffTairCount"').findall(response.text)[0]

    cart_headers = {
        # 'Connection': 'keep-alive',
        # 'Cache-Control': 'max-age=0',
        # 'Origin': 'https://cart.taobao.com',
        # 'Upgrade-Insecure-Requests': '1',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        # 'Content-Type': 'application/x-www-form-urlencoded',
        "referer": 'https://cart.taobao.com/cart.htm?spm=a1z0d.6639537.1997525049.1.abcd74844nvvnd&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739',
        # 'accept': 'application / json, text / javascript, * / *; q = 0.01',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'zh - CN, zh;q = 0.9',
        # 'content-length': '432',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same - origin',
        # 'x-requested-with': 'XMLHttpRequest',
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
        't': str(time.time()),
        'type': 'check',
        'ct': 'f2c8b39be0bab415eb154e365daa0345',
        'page': '1',
        '_thwlang': 'zh_CN',
    }

    headers = {
        'referer': 'https://cart.taobao.com/',
    }
    response = s.get('https://gm.mmstat.com/tbcart.8.6?cache=' + str(time.time()), headers=headers)
    response.raise_for_status()
    response = s.post(pre_purchase_address, headers=cart_headers, data=cart_data)
    response = s.get(purchase_address)
    response = s.get("https://buy.taobao.com/auction/fastbuy/loginSuccess.vm?from=cart")
    return response


if __name__ == '__main__':
    s = requests.session()
    # check_username()
    res = login()
    res = my_cart(res)
    res = purchase(res, '1')
    # res = detail(res)
