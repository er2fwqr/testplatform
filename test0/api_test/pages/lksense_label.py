'''
点击打点接口
'''
import json

from test0.api_test.bases.base import Request, MysqlHelp
import requests
from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.pages.lksense_get_latest_params import Get_Latest_Data


class Label_Api:
    label_url = Request().build_url('vrs', 'label_url')
    login_url = Request().build_url('login', 'login_url')

    def build_data(self):
        stack_info=Get_Latest_Data().get_stack_info()
        stack_id=stack_info[2]
        asset_id=stack_info[7]
        asset_tbl_tag=stack_info[0]
        avi_id=stack_info[4]
        board_no=stack_info[3]
        number=board_no
        par_code=stack_info[5]

        data = {
            'stack_id': stack_id,
            'sampling_mode': 1,
            'asset_id': asset_id,
            'asset_tbl_tag': asset_tbl_tag,
            'avi_id': avi_id,

            'board_no': board_no,
            'board_option': 4,
            'is_deny_handle': False,
            'is_refresh_ngpoint': True,
            'lev1_code': '',
            'number': number,
            'page': 1,
            'pages': 1,
            'par_code': par_code,
            'parent_id': '',
            'pcb_version': '',
            'per_page': 1,
            'random_check': True,
            'vrs_result': 1,
            'vrs_results': [],
            'vrs_reverse': '',
            'zone_code': ""
        }
        # data = json.dumps(data)
        return data

    def label(self, json, **kwargs):
        res = Request().send_request(method='p', url=self.label_url, json=json, **kwargs)
        return res


if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)

    data = Label_Api().build_data()
    print(type(data))
    s = Label_Api().label(json=data, cookies=cookies)
    print(s.json())
