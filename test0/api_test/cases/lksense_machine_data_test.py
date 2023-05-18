from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.pages.lksense_machine_data import Machine_Data_Api
import unittest,requests
class Machine_Data_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_machine_data(self):
        '''
        群组复检根据机台时间获取叠
        :return:
        '''
        params=Machine_Data_Api().build_params()
        res=Machine_Data_Api().machine_data_api(params=params,cookies=self.setUp())
        true_count=Machine_Data_Api().get_true_count(avi_id=params['avi_ids'], start_time=params['start_time'],
                                                  end_time=params['end_time'])
        self.assertEqual(res,true_count,msg='群组复检获取叠接口数量与数据库不符，测试不通过！')
if __name__ == '__main__':
    unittest.main(verbosity=3)