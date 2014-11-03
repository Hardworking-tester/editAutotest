# encoding:utf-8
from test_login import Login
from object import LocateLoginObject
import Browser,time
from selenium import webdriver
class PublicLogin():
    """本类作为公共方法，简化了正确登录方法并在最后获得会员中心页面的句柄，最后返回一个webdriver对象"""

    def publicLogin(self):
        br=Browser.Browser().init_browser()
        br.find_element_by_link_text(u"请登录").click()
        time.sleep(2)
        br.find_element_by_id('userName').send_keys('wwg54421@163.com')
        time.sleep(2)
        br.find_element_by_id('password').send_keys('wwg123456')
        br.find_element_by_id('imgLogin').click()
        time.sleep(2)
        br.switch_to.alert.accept()
        time.sleep(5)
        return br

