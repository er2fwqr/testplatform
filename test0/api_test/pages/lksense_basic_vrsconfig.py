'''
vrs配置获取
'''
import configparser
import os,time
import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class Basic_Vrsconfig_Api:

    basic_vrsconfig_url = Request().build_url('vrs', 'vrs_config_url')
    login_url = Request().build_url('login', 'login_url')

    def basic_vrsconfig_api(self,**kwargs):

        res=Request().send_request('g',url=self.basic_vrsconfig_url,**kwargs)
        return res
if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    res=Basic_Vrsconfig_Api().basic_vrsconfig_api(cookies=cookies)
    print(res.json())