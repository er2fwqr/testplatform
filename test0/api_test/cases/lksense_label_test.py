'''
取最近asset表中最新一天的第一个点
打点后再连接数据库查询，根据查到的vrs_result校验进行断言
'''
import requests

from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.bases.base import MysqlHelp
from test0.api_test.pages.lksense_label import Label_Api
from test0.api_test.pages.lksense_get_latest_params import Get_Latest_Data
import unittest
class Label_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_label(self):
        '''
        打点
        :return:
        '''
        # 先根据构建的点数据向接口发送请求
        la=Label_Api()
        json=la.build_data()
        print(type(json))
        cookie = self.setUp()
        la.label(json=json,cookies=cookie)
        # 后获取数据库中对应点vrs_result的真实值
        stack_info=Get_Latest_Data().get_stack_info()
        real_vrs_result=MysqlHelp().get_data(sql='select vrs_result from idetect.%s where id=%s'%(stack_info[1],stack_info[7]))
        # 对比校验获取测试结果
        self.assertEqual(real_vrs_result[0][0],1,'VRS打点接口打点失败，测试不通过')
if __name__ == '__main__':
    unittest.main(verbosity=3)
