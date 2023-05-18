import requests,time

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class Warn_Get_Api:
    warn_get_url = Request().build_url('vrs', 'warn_get_url')
    login_url = Request().build_url('login', 'login_url')

    def warn_get_api(self,params,**kwargs):
        res=Request().send_request(method='g',url=self.warn_get_url,params=params,**kwargs)
        return res
if __name__ == '__main__':
    time=int(time.time())
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    s=Warn_Get_Api().warn_get_api(params={
        '_':time
    },cookies=cookies)
    print(s.json())