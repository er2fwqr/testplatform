import unittest

import requests

from test0.api_test.pages.lksense_gpu_info_get import GPU_Info_Get_Api
from test0.api_test.pages.lksense_login import Login_Api


class GPU_Info_Get_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_gpu_info_get(self):
        '''
        获取显卡信息
        :return:
        '''
        res=GPU_Info_Get_Api().gpu_info_get_api(cookies=self.setUp())
        self.assertEqual(res.json()['success'],True,msg='显卡信息获取接口测试不通过！')
if __name__ == '__main__':
    unittest.main(verbosity=3)