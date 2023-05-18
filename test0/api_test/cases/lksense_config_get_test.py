import random

import requests

from test0.api_test.pages.lksense_config_get import Config_Get_Api
from test0.api_test.pages.lksense_login import Login_Api
import unittest
from test0.api_test.bases.base import MysqlHelp

class Congfig_Get_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_config_get(self):
        '''
        获取机台配置
        :return:
        '''
        avi_list=MysqlHelp().get_data(sql='select id from idetect.avi')
        eg_avi=random.choice(avi_list)[0]
        res=Config_Get_Api().config_get_api(avi_id=str(eg_avi),cookies=self.setUp())
        self.assertIn(res.json()['msg'],['ok','机台号未绑定方案'],msg='机台配置获取接口测试不通过！')
        print(res.json())
if __name__ == '__main__':
    unittest.main(verbosity=3)

