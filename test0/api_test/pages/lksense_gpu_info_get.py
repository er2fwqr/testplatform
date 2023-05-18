# 获取显卡信息
import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class GPU_Info_Get_Api:
    gpu_info_get_url = Request().build_url('gpu_manage', 'gpu_info_get_url')
    login_url = Request().build_url('login', 'login_url')


    def gpu_info_get_api(self,cookies):
        res =Request().send_request(method='g',url=self.gpu_info_get_url,cookies=cookies)
        return res
if __name__ == '__main__':
    cookies=requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    # print(cookies)
    result=GPU_Info_Get_Api().gpu_info_get_api(cookies=cookies)
    print(result.json())