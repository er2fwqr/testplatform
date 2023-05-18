# 获取用户信息
import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class User_Get_Api:
    user_get_url = Request().build_url('user_info', 'get_user_url')
    login_url = Request().build_url('login', 'login_url')

    def user_get_api(self,params,**kwargs):
        res=Request().send_request(method='g',url=self.user_get_url,params=params,**kwargs)
        return res
if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    s=User_Get_Api().user_get_api(params={
        'user_id':1
    },cookies=cookies)
    print(s.json())