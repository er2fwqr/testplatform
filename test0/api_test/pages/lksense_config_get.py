# 获取机台配置
#
import configparser
import os,time
import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class Config_Get_Api:

    config_get_url = Request().build_url('vrs', 'config_get_url')
    login_url = Request().build_url('login', 'login_url')

    def config_get_api(self,avi_id,**kwargs):
        res=Request().send_request('g',url=self.config_get_url+'?avi_id='+str(avi_id)+'&_='+str(time.time()),**kwargs)
        return res



if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    res=Config_Get_Api().config_get_api(avi_id=158,cookies=cookies)
    print(res.json())
