'''
获取页面权限接口
无参数
'''

import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class Page_Permission_Api:
    page_permission_url = Request().build_url('page_permission', 'page_permission_url')
    login_url = Request().build_url('login', 'login_url')


    def page_permission_api(self,**kwargs):
        res=Request().send_request(method='g',url=self.page_permission_url,**kwargs)
        return res
if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)

    s=Page_Permission_Api().page_permission_api(cookies=cookies)
    print(s.json())