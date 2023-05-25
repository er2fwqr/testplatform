'''
群组复检界面打开后根据机台和时间段获取料号的接口

'''

import requests, datetime

from test0.api_test.bases.base import Request, MysqlHelp
from test0.api_test.pages.lksense_login import Login_Api


class Machine_Data_Api():
    # 取配置文件中的url
    url = Request().build_url('vrs', 'machine_data_url')
    login_url = Request().build_url('login', 'login_url')

    # 对接口发送请求的方法，返回值为从接口返回数据中取的料号数量
    def machine_data_api(self, params, **kwargs):
        res = Request().send_request('g', url=self.url, params=params, **kwargs)
        res_json=res.json
        return len(res_json()['data'])

    def machine_data(self,params,**kwargs):
        res = Request().send_request('g', url=self.url, params=params, **kwargs)
        print(res.json())
    # 从数据库中取真实值作为校验，此处取值为满足条件的料号数量
    def get_true_count(self, avi_id, start_time, end_time):
        true_count = MysqlHelp().get_data(
            sql='SELECT count(pcb_code) FROM idetect.asset_folder where avi_id="%s" AND create_time BETWEEN "%s" and "%s" and level=3' % (
            avi_id, start_time, end_time))

        return true_count[0][0]

    # 创建请求参数
    def build_params(self):
        avi_id = \
        MysqlHelp().get_data(sql='select distinct avi_id from idetect.asset_folder order by avi_id desc limit 1')[0][0]
        start_time = '2022-01-01'
        end_time = str(datetime.date.today())
        params = {
            'avi_ids': avi_id,
            'start_time': start_time,
            'end_time': end_time
        }
        return params


if __name__ == '__main__':
    params = Machine_Data_Api().build_params()
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    Machine_Data_Api().machine_data(params=params, cookies=cookies)
    res = Machine_Data_Api().machine_data_api(params=params, cookies=cookies)
    print(res)
    lot_count = Machine_Data_Api().get_true_count(avi_id=params['avi_ids'], start_time=params['start_time'],
                                                  end_time=params['end_time'])
    print(lot_count)
    print(Machine_Data_Api().build_params())