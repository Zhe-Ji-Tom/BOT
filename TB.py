from selenium import webdriver
import datetime
import time

login_address = "https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9RKrfEP&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F"
login_button_class = "icon-qrcode"
cart_address = "https://cart.taobao.com/cart.htm?spm=a21bo.2017.1997525049.1.5af911d9gP7Rhr&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739"
select_all_products_button_id = "J_SelectAll1"
select_all_products_button_text = "全选"
purchase_button_text = "结 算"
purchase_button_id = "J_Go"
submit_order_button_text = "提交订单"
submit_order_button_class = "go-btn"


def login():
    # 打开登录页面
    browser.get(login_address)
    time.sleep(3)
    if browser.find_element_by_class_name(login_button_class):
        # 点击扫码登录
        browser.find_element_by_class_name(login_button_class).click()
        print("请扫码登录")
        time.sleep(15)
        # 切换到购物车页面
        browser.get(cart_address)
        time.sleep(3)


def buy():
    if browser.find_element_by_id(select_all_products_button_id):
        # 全选所有商品
        browser.find_element_by_id(select_all_products_button_id).click()
        print("已选择全部商品")
    while True:
        # 获取当前时间
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        # 判断当前时间
        if now > times:
            while True:
                try:
                    if browser.find_element_by_link_text(purchase_button_text):
                        # 点击结算
                        browser.find_element_by_link_text(purchase_button_text).click()
                        print("结算成功")
                        break
                except:
                    print("结算有误")
            while True:
                try:
                    if browser.find_element_by_link_text(submit_order_button_text):
                        # 点击提交订单
                        browser.find_element_by_link_text(submit_order_button_text).click()
                        print("提交订单成功")
                        time.sleep(1)
                        break
                except:
                    print("提交订单有误")
            break


if __name__ == '__main__':
    times = input("输入购买时间，格式为2020-12-08 12:00:00.000：")
    browser = webdriver.Chrome()
    browser.maximize_window()
    login()
    buy()
