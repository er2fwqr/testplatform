'''
vrs平均报点获取
校验方式：与数据库中取到的总报点对比
'''
import requests,unittest
from test0.api_test.pages.lksense_asset_average import Asset_Average_Api
from test0.api_test.pages.lksense_login import Login_Api


class Asset_Average_test(unittest.TestCase):
    def setUp(self) -> None:
        params=Asset_Average_Api().build_params()
        return params
    def test_asset_average(self):
        '''
        vrs平均报点
        :return:
        '''
        # total_asset:数据库中总报点数量
        total_asset=Asset_Average_Api().get_total_asset()
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        res=Asset_Average_Api().asset_average_api(params=self.setUp(),cookies=cookies)
        self.assertEqual(res.json()['data']['total_asset_count'],total_asset,msg='平均报点接口数据与数据库不符，测试不通过！')
    def tearDown(self) -> None:
        pass
if __name__ == '__main__':
    unittest.main(verbosity=3)