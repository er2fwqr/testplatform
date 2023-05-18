import requests

from test0.api_test.pages.lksense_basic_vrsconfig import Basic_Vrsconfig_Api
import unittest

from test0.api_test.pages.lksense_login import Login_Api


class Basic_Vrsconfig(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_basic_config(self):
        '''
        读取vrs配置
        :return:
        '''
        s=Basic_Vrsconfig_Api().basic_vrsconfig_api(cookies=self.setUp())
        # print(s.json())
        self.assertEqual(s.json()['success'],True,msg='VRS配置获取接口测试不通过')
if __name__ == '__main__':
    unittest.main(verbosity=3)
