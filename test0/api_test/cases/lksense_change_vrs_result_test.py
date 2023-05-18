import unittest
from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.pages.lksense_change_vrs_result import Change_Vrs_Result_Api
import requests, json


class Change_Vrs_Result_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies

    def tearDown(self) -> None:
        pass

    def test_change_vrs_result(self):
        '''
        vrs打点
        :return:
        '''
        asset_data = Change_Vrs_Result_Api().get_point_data()


        assets = [{
            'id': asset_data[0],
            'vrs_result': '2',  # 此处vrs_result值可以自由设定，但在断言中要改为相同值
            'confirm_type': '2'

        }]

        json = {
            'assets': assets,
            'is_scarp': 'false',
            'update_ai_file': 'false',
            'update_true_file': 'true'
        }
        # json参数为最终发送的数据
        # 构建消息体参数

        Change_Vrs_Result_Api().change_vrs_result(json=json, cookies=self.setUp())  # 等价于执行打点操作

        point_data = Change_Vrs_Result_Api().get_point_data()
        # print(point_data)
        self.assertEqual(point_data[1], 2,msg='VRS翻页接口（附带打点）测试不通过！')  # 此处’2‘对应上面构建参数时的vrs_result


if __name__ == '__main__':
    unittest.main(verbosity=3)
