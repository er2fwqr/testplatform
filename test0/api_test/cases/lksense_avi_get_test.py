import requests

from test0.api_test.pages.lksense_avi_get import Avi_Get_Api
from test0.api_test.pages.lksense_login import Login_Api
import unittest
class Avi_Get_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_avi_get(self):
        '''
        获取机台列表
        :return:
        '''
        params={"page": 1,
              "page_size": 999,
              "type": 1,
              "_": 1669167816795}
        res=Avi_Get_Api().avi_get_api(params=params,cookies=self.setUp())
        avi_count=len(res.json()['data']['avi_list'])

        real_avi_count=len(Avi_Get_Api().get_avi_list())
        self.assertEqual(avi_count,real_avi_count,'机台列表获取接口测试不通过！')

if __name__ == '__main__':
    unittest.main(verbosity=3)