import unittest

import requests

from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.pages.lksense_page_permission import Page_Permission_Api
class Page_Permission_test(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_page_permission(self):
        '''
        获取页面权限列表
        :return:
        '''
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        res=Page_Permission_Api().page_permission_api(cookies=cookies)
        self.assertEqual(res.json()['msg'],'ok',msg='页面权限接口测试不通过')
if __name__ == '__main__':
    unittest.main(verbosity=3)