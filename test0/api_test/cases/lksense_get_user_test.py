import random

import requests

from test0.api_test.pages.lksense_get_user import User_Get_Api
from test0.api_test.pages.lksense_login import Login_Api
import unittest
from test0.api_test.bases.base import MysqlHelp

class Get_User_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_get_user(self):
        '''
        获取用户信息
        :return:
        '''
        user_id=random.choice(MysqlHelp().get_data(sql='select id from idetect.user'))[0]
        res=User_Get_Api().user_get_api(params={'user_id':user_id},cookies=self.setUp())
        print(res.json())
        self.assertIn(res.json()['msg'],['success','找不到用户'],msg='用户信息获取失败，测试不通过！')
if __name__ == '__main__':
    unittest.main(verbosity=3)