import unittest,random

import requests

from test0.api_test.pages.lksense_asset_get import Asset_Get_Api
from test0.api_test.bases.base import MysqlHelp
from test0.api_test.pages.lksense_login import Login_Api


class Asset_Get_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_asset_get(self):
        '''
        根据pcb_id获取机台信息
        :return:
        '''
        pcb_id_list1=MysqlHelp().get_data(sql='select id from idetect.pcb')
        pcb_id_list2=[]
        for i in pcb_id_list1:
            pcb_id_list2.append(i[0])

        s=Asset_Get_Api().asset_get_api(pcb_id=random.choice(pcb_id_list2),cookies=self.setUp())

        self.assertIn('true',s.text,msg='获取机台信息接口测试不通过！')

if __name__ == '__main__':
    unittest.main(verbosity=3)