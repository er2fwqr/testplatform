import configparser
import os

import requests,random


from test0.api_test.bases.base import Request,MysqlHelp
from test0.api_test.pages.lksense_login import Login_Api

from test0.api_test.pages.lksense_get_latest_params import Get_Latest_Data
class NG_Data_Api:
    '''
    需要的参数：
    asset_tbl_tag(从asset表获取）
    avi_id(根据parcode从avi表获取)
    parcode(asset表获取)
    stack_id(从board表affiliated_folder_id获取)
    '''
    stack_info=Get_Latest_Data().get_stack_info()
    asset_tbl_tag=stack_info[0]
    avi_id=stack_info[4]
    stack_id=stack_info[2]
    par_code=stack_info[5]
    board_no=stack_info[3]
    ng_data_url = Request().build_url('vrs', 'ng_data_url')
    login_url = Request().build_url('login', 'login_url')
    json = {
        "ai_result": "1",
        "asset_tbl_tag": asset_tbl_tag,
        "avi_id": avi_id,
        "board_no": board_no,
        "board_option": 4,
        "is_refresh_ngpoint":True,
        "page": 1111,
        "pages": 1111,
        "par_code": par_code,
        "per_page": 8,
        "sampling_mode": 1,
        "stack_id": stack_id,
        "vrs_result": "",
        "vrs_results": [],
        "vrs_reverse": 0,
        "zone_code": ""
    }
    '''
    page\pages参数只起校验作用，具体值随便传
    '''

    # 后续需要新建获取data的方法

    def ng_data_api(self, **kwargs):
        res = Request().send_request('p', url=self.ng_data_url, json=self.json, **kwargs)
        return res


if __name__ == '__main__':
    print(NG_Data_Api().stack_info)
    print(NG_Data_Api().json)
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    print(cookies)
    res = NG_Data_Api().ng_data_api(cookies=cookies)
    # print(len(res.json()['data']['all_assets']))
    print(res.json())
