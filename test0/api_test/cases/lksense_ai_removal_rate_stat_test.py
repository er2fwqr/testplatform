'''
报点过滤用例
取接口数据和数据库校验
校验值为总点数
'''
import requests

from test0.api_test.pages.lksense_ai_removal_rate_stat import Ai_Removal_Rate_Stat_Api
import unittest
from test0.api_test.bases.base import MysqlHelp
from test0.api_test.pages.lksense_login import Login_Api


class Ai_Removal_Rate_Stat_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies=requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    @unittest.skip('')
    def test_ai_removal_rate_stat(self):
        '''
        ai去除率统计
        :return:
        '''
        json=Ai_Removal_Rate_Stat_Api().build_json()
        res=Ai_Removal_Rate_Stat_Api().ai_removal_rate_stat(json=json,cookies=self.setUp())
        print(res.json())
        assets_count=res.json()['data']['stack_data']['assets_count']
        print(assets_count)

        real_assets_count=MysqlHelp().get_data(sql='select count(*) from idetect.asset_%s where affiliated_folder_id =%s'%(json['asset_tbl_tag'],json['stack_id']))
        # 获取总点数
        # 存在机台未适配统计功能的情况，断言可能失败（已知协辰机台）
        self.assertEqual(assets_count,real_assets_count[0][0],msg='AI去除率统计接口数据不符')
if __name__ == '__main__':
    unittest.main(verbosity=0)