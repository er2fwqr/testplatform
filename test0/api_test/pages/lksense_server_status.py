import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class Server_Status_Api:
    server_status_url = Request().build_url('server_status', 'server_status_url')
    login_url = Request().build_url('login', 'login_url')


    def server_status_api(self,json,**kwargs):
        res=Request().send_request(method='p',url=self.server_status_url,json=json,**kwargs)
        return res
if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    s=Server_Status_Api().server_status_api(json={'row_num':2},cookies=cookies)
    print(s.json())