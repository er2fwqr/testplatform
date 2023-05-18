from test0.api_test.bases.base import Request
import configparser, os
from test0.api_test.pages.lksense_login import Login_Api
import requests, time


class Update_Machine_Api:
   
    update_machine_url = Request().build_url('machine_manage', 'update_machine_url')
    login_url = Request().build_url('login', 'login_url')





    def update_machine_api(self,data,**kwargs):


        # print(len(data))
        res = Request().send_request('put', url=self.update_machine_url, data=data, **kwargs)
        return res
if __name__ == '__main__':
    update_data = {
        "address": "changeaddress",
        "avi_model_code": "shirai",
        "avi_model_id": 1,
        "avi_model_name": "白井机台",
        "avilog_address": "111",
        "code": "1668499514",
        "create_time": "2022-11-15T16:06:51",
        "data_address": "/opt/testdata/ref",
        "detect_scheme_code": "default",
        "filtered": 'true',
        "id": 161,
        "last_update": "2022-11-15T16:06:51",
        "name": "1668499514",
        "precision": 1,
        "procedure_code": "fqc1",
        "schema_type_id": 1,
        "stage": 3,
        "status": "inactive",
        "version": "1",
        "zone_scheme_code": "default"
    }

    cookies=requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)


    res=Update_Machine_Api().update_machine_api(data=update_data,cookies=cookies)
    print(res.json())
