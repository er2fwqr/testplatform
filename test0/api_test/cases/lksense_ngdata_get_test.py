import unittest
import requests
from test0.api_test.pages.lksense_ngdata_get import NG_Data_Api
from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.bases.base import MysqlHelp
from test0.api_test.pages.lksense_get_latest_params import Get_Latest_Data
class Ngdata_Get_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_ngdata_get(self):
        '''
        获取数据库中ng点数
        :return:
        '''
        stack_info=Get_Latest_Data().get_stack_info()
        asset_tbl=stack_info[1]
        board_number=stack_info[3]
        pcb_code=stack_info[6]
        real_ngpoint_count=MysqlHelp().get_data(sql='select count(*) from idetect.%s where ai_result=1 and pcb_code="%s" and number="%s"'%(asset_tbl,pcb_code,board_number))[0][0]
        '''
        对接口发送请求获取ng点数量
        '''
        res = NG_Data_Api().ng_data_api(cookies=self.setUp())
        ngpoint_count=len(res.json()['data']['all_assets'])
        self.assertEqual(real_ngpoint_count,ngpoint_count,msg='ng点数据不匹配')
if __name__ == '__main__':
    unittest.main(verbosity=3)