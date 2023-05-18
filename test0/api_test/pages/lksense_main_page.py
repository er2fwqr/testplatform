import configparser
import os,time
import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class Main_Page_Api:
    # __conf = configparser.ConfigParser()
    # if os.path.exists(r'../conf/'):
    #     __conf.read(r'../conf/lksense.ini', encoding='utf8')
    # else:
    #     __conf.read(r'conf/lksense.ini', encoding='utf8')
    main_page_url = Request().build_url('main_page', 'main_page_url')
    login_url = Request().build_url('login', 'login_url')

    def main_page_api(self,**kwargs):
        res=Request().send_request('g',url=self.main_page_url,**kwargs)
        return res
if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    res=Main_Page_Api().main_page_api(cookies=cookies)
    print(res.text)