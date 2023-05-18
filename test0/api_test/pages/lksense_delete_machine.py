# 删除机台接口

import configparser
import os

import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class Delete_Machine_Api:

    delete_machine_url = Request().build_url('machine_manage', 'delete_machine_url')
    login_url = Request().build_url('login', 'login_url')

    def delete_machine_api(self,  **kwargs):
        res = requests.delete(url=self.delete_machine_url,**kwargs)
        return res


if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    # # print(cookies)
    # headers=Login_Api().api_login().headers
    # headers = {
    #     "Cookie": "access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjY5MTczMDQ4Ljk0NTEyODR9.zWngFDfiKEyuYlQLxSYtKsXYADwmxks9tZyLMAs9Lic",
    #     }
    # data = {'avi_id': 166}
    res = Delete_Machine_Api().delete_machine_api(cookies=cookies,json={"avi_id":143})
    print(res.json())
