'''
获取报点接口
'''
import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class Asset_Get_Api:

    asset_get_url = Request().build_url('vrs', 'asset_get_url')
    login_url = Request().build_url('login', 'login_url')


    def asset_get_api(self,pcb_id,**kwargs):
        res=Request().send_request('g',url=self.asset_get_url+'?pcb_id='+str(pcb_id),**kwargs)
        return res
if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    res=Asset_Get_Api().asset_get_api(pcb_id=160,cookies=cookies)
    print(res.text)