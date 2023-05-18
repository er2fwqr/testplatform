import requests

from test0.api_test.pages.lksense_stack_data import Stack_Data_Api
from test0.api_test.pages.lksense_login import Login_Api
import unittest
class Stack_Data_test(unittest.TestCase):
    '''
    群组复检打开叠数据
    '''
    def setUp(self) -> None:
        # 登录获取cookie
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_stack_data(self):
        '''
        res1:打开叠之后返回的板数据
        res2:从数据库获取真实的板数量
        断言：将res1中的板数量与res2做对比，相同则测试通过



        '''
        res1=Stack_Data_Api().stack_data_api(cookies=self.setUp())
        res2=Stack_Data_Api().get_board_count()
        self.assertEqual(len(res1['board_pool']),res2,msg='测试不通过，接口板数量与数据库不符！')
if __name__ == '__main__':
    unittest.main(verbosity=3)