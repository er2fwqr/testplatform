'''
获取机台信息接口
'''
import requests
import time
from test0.api_test.bases.base import Request,MysqlHelp
from test0.api_test.pages.lksense_login import Login_Api
import time

class Avi_Get_Api:

    avi_get_url = Request().build_url('vrs', 'avi_get_url')
    login_url = Request().build_url('login', 'login_url')

    def avi_get_api(self, params, **kwargs):
        res = Request().send_request(method='g', url=self.avi_get_url, params=params, **kwargs)
        return res

    def get_avi_list(self):
        '''
        获取数据库avi表中真实的机台数量
        此处sql查询了非删除状态的机台，并且过滤掉了重检机台
        :return:
        '''
        sql='select * from idetect.avi where status!="deleted" and code not like "%_re_%"'
        avi_list=MysqlHelp().get_data(sql=sql)
        return avi_list

if __name__ == '__main__':
    params = {"page": 1,
              "page_size": 999,
              "type": 1,
              "_": int(time.time())}
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    s = Avi_Get_Api().avi_get_api(params=params, cookies=cookies)
    print(len(s.json()['data']['avi_list']))
    print(len(Avi_Get_Api().get_avi_list()))