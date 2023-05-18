'''
群组复检界面报点过滤情况界面接口
取叠、板数据仍来自于最近一天的asset表
使用get_stack_info方法获取数据
'''
import os

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_get_latest_params import Get_Latest_Data
from test0.api_test.pages.lksense_login import Login_Api
import requests
import time
from configparser import ConfigParser
class Ai_Removal_Rate_Stat_Api:
    if os.path.exists(r'../conf/lksense.ini'):
        cp=ConfigParser()
        cp.read(r'../conf/lksense.ini', encoding='utf8')
        with open(r'../conf/lksense.ini', 'w', encoding='utf-8') as file:
            # print(file)
            cp.write(file)
            os.fsync(file.fileno())
    else:
        cp = ConfigParser()
        cp.read(r'conf/lksense.ini', encoding='utf8')
        with open(r'conf/lksense.ini', 'w', encoding='utf-8') as file:
            # print(file)
            cp.write(file)
            os.fsync(file.fileno())


    ai_removal_rate_stat_url=Request().build_url('vrs','ai_removal_rate_stat_url')
    print(ai_removal_rate_stat_url)
    login_url = Request().build_url('login', 'login_url')

    def ai_removal_rate_stat(self,json,**kwargs):
        res=Request().send_request(method='p',url=self.ai_removal_rate_stat_url,json=json,**kwargs)
        return res
    def build_json(self):
        # 根据stack_info构建消息体数据
        stack_info=Get_Latest_Data().get_stack_info()
        asset_tbl_tag=stack_info[0]
        stack_id=stack_info[2]
        number=stack_info[3]
        json={
            'asset_tbl_tag': asset_tbl_tag,
            'mode': 1,
            'number': number,
            'stack_id': stack_id
        }
        # print(json)
        return json
if __name__ == '__main__':
    cookies=requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    rate=Ai_Removal_Rate_Stat_Api().ai_removal_rate_stat(json=Ai_Removal_Rate_Stat_Api().build_json(),cookies=cookies)
    print(rate.json())





