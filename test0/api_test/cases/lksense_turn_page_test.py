'''
两个场景

1.test_turn_page:
翻页接口测试，assets参数为空时
不改动vrs_result的翻页
因为未改动数据库数据
所以通过与返回值中code值对比做校验
2.test_point:
打点测试，当assets参数为点相关数据时，会对相应的点进行打点
取数据库相应点vrs_result进行校验
'''
import requests,unittest
from test0.api_test.pages.lksense_get_latest_params import Get_Latest_Data
from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.pages.lksense_turn_page import Turn_Page_Api
from test0.api_test.bases.base import MysqlHelp
class Turn_Page_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies=requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_turn_page(self):
        '''
        翻页需要的参数（不包含打点）
        :return:
        '''
        json = {
            'assets': [],
            'is_scarp': False,
            'update_ai_file': False,
            'update_true_file': True
        }
        res=Turn_Page_Api().turn_page(json=json,cookies=self.setUp())
        self.assertEqual(res.json()['code'],0)
    def test_point(self):
        '''
        assets参数不为空时，可以对其中的点进行打点

        :return:
        '''
        json= {
            'assets': Turn_Page_Api().build_assets_data(),
            'is_scarp': False,
            'update_ai_file': False,
            'update_true_file': True
        }
        res = Turn_Page_Api().turn_page(json=json, cookies=self.setUp())
        print(json)
        print(res.json())
        stack_info=Get_Latest_Data().get_stack_info()
        real_vrs_result=MysqlHelp().get_data(sql='select vrs_result from idetect.%s where id=%s'%(stack_info[1],stack_info[7]))[0][0]
        # 打点后取数据库对应点的vrs_result
        self.assertEqual(real_vrs_result,1,msg='打点接口打点失败')
if __name__ == '__main__':
    unittest.main(verbosity=3)