import time

import requests
from test0.api_test.bases.base import MysqlHelp
from test0.api_test.pages.lksense_delete_machine import Delete_Machine_Api
from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.pages.lksense_create_machine import Create_Machine_Api
import unittest, os
from ddt import ddt, data, unpack

from test0.api_test.pages.lksense_update_machine import Update_Machine_Api


class Machine_manage_test(unittest.TestCase):
    avi_name = "test%s" % int(time.time())
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    update_data = {"address": "1",
                   "avi_model_code": "shirai",
                   "avi_model_id": 1,
                   "avi_model_name": "白井机台",
                   "avilog_address": "2",
                   "code": avi_name,
                   "create_time": "2022-11-22T16:11:49",
                   "data_address": "1",
                   "detect_scheme_code": "default",
                   "filtered": 'false',
                   "id": 171,
                   "last_update": "2022-11-22T16:11:49",
                   "name": avi_name,
                   "precision": 1,
                   "procedure_code": "fqc3_ic",
                   "schema_type_id": 1,
                   "stage": 3,
                   "status": "inactive",
                   "version": "1",
                   "zone_scheme_code": "default"}

    def setUp(self) -> None:
        Create_Machine_Api().create_machine_api(avi_name=self.avi_name, cookies=self.cookies)
        machine_id = \
            MysqlHelp().get_data(sql="SELECT * FROM `idetect`.`avi` WHERE `name` = '%s' LIMIT 0,1000;" % self.avi_name)[0][0]
        return machine_id

    def tearDown(self) -> None:
        Delete_Machine_Api().delete_machine_api(cookies=self.cookies, json={"avi_id": self.setUp()})
        MysqlHelp().get_data(sql='delete  from idetect.avi where id =%s'%self.setUp())
    def test_machine_manage(self):
        '''
        机台新建、修改、删除（软删除）、数据库删除
        :return:
        '''
        # print(self.setUp())
        self.update_data['id'] = str(self.setUp())
        print(self.update_data)

        res = Update_Machine_Api().update_machine_api(data=self.update_data,cookies=self.cookies)
        print(res.json())
        self.assertEqual(res.json()['success'], True,msg='新建机台接口测试不通过！')


if __name__ == '__main__':
    unittest.main(verbosity=3)
