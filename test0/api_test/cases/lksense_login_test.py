from ddt import ddt,data,unpack

from test0.api_test.bases.base import CsvHelp
from test0.api_test.pages.lksense_login import Login_Api
import unittest,os

@ddt
class Login_test(unittest.TestCase):


    if os.path.exists(r'data'):
        test_data = CsvHelp().get_csv_data(r'data/account.csv')
    else:
        test_data = CsvHelp().get_csv_data(r'D:\Python38-32\Scripts\lk_test\test0\api_test\data\account.csv')

    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    @data(*test_data)
    @unpack
    def test_login(self,user,password,expected_result):
        '''
        登录
        :param user:
        :param password:
        :param expected_result:
        :return:
        '''
        res=Login_Api().api_login(username=user,password=password)
        self.assertEqual(str(res.json()['success']),expected_result,'登录失败，测试不通过！')

if __name__ == '__main__':
    unittest.main(verbosity=3)