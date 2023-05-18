'''
vrs打点
'''
import random

import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_get_latest_params import Get_Latest_Data
from test0.api_test.bases.base import MysqlHelp
from test0.api_test.pages.lksense_login import Login_Api

'''
总流程：
构建url；
取合适的测试点；
构建json消息体数据；
发送请求；


confirm_type代表very_ng相关的是否为人工确认的点
值为2代表人工打点

'''


class Change_Vrs_Result_Api:
    change_vrs_result_url = Request().build_url('vrs', 'turn_page_url')
    login_url = Request().build_url('login', 'login_url')

    stack_info = Get_Latest_Data().get_stack_info()

    '''
    获取数据库中点id和vrs_result
    后续
    '''

    def build_complete_url(self):
        '''
        stack_info[2]:对应asset表中的affiliated_folder_id
        拼接url

        '''

        complete_url = self.change_vrs_result_url + '/%s/%s/%s' % (self.stack_info[2], self.stack_info[3], self.stack_info[0])
        # print(complete_url)
        return complete_url



    '''
    获取要打的点信息：点id、vrs_result(用于后续校验)
    '''
    def get_point_data(self):
        sql = 'select id,vrs_result from idetect.%s where affiliated_folder_id=%s and number=%s' % (
        self.stack_info[1], self.stack_info[2],self.stack_info[3])
        asset_list = MysqlHelp().get_data(sql=sql)

        # asset_data格式：
        asset_data = asset_list[0]
        # print(asset_list)
        # print(asset_data)
        return asset_data


    '''
    发送请求
    '''
    def change_vrs_result(self, json, **kwargs):
        res = Request().send_request('put', url=self.build_complete_url(), json=json, **kwargs)
        # print(res.json())
        return res

    def recover_point(self):
        initial_vrs_result=self.get_point_data()[1]


if __name__ == '__main__':
    asset_data = Change_Vrs_Result_Api().get_point_data()
    print(asset_data)
    assets = [{
        'id': asset_data[0],
        'vrs_result': '1',
        'confirm_type': '2'

    }]
    # print(assets)
    json = {
        'assets': assets,
        'is_scarp': 'false',
        'update_ai_file': 'false',
        'update_true_file': 'true'
    }
    # print(json)
    print(Change_Vrs_Result_Api().stack_info)
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    res=Change_Vrs_Result_Api().change_vrs_result(json=json, cookies=cookies)
    point_data2=Change_Vrs_Result_Api().get_point_data()[1]
    print(res.json())  #res.json为返回数据
    print(point_data2)
