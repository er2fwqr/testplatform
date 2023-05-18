# 创建机台接口
from test0.api_test.bases.base import Request

from test0.api_test.pages.lksense_login import Login_Api
import requests,time
class Create_Machine_Api:

    create_machine_url = Request().build_url('machine_manage', 'create_machine_url')
    login_url = Request().build_url('login', 'login_url')

    def create_machine_api(self,avi_name,**kwargs):

        data = {
            'address': '1',
            'avi_model_id': '1',
            'avilog_address': "1",
            'code': "test%s"%int(time.time()),
            'data_address': "1",
            'detect_mode': 1,
            'detect_scheme_code': "default",
            'filtered': 'false',
            'name': avi_name,
            'precision': "1",
            'procedure_code': "fqc3_ic",
            'schema_type_id': 1,
            'status': "inactive",
            'version': "1",
            'zone_scheme_code': "default"
        }
        res=Request().send_request('p',url=self.create_machine_url,data=data,**kwargs)
        return res
if __name__ == '__main__':
    cookies=requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)


    res=Create_Machine_Api().create_machine_api(avi_name="test%s"%int(time.time()), cookies=cookies)
    print(res.json()['success'])

