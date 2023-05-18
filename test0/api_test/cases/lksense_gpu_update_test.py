import unittest

import requests

from test0.api_test.pages.lksense_gpu_info_get import GPU_Info_Get_Api
from test0.api_test.pages.lksense_gpu_update import GPU_Update_Api

from test0.api_test.pages.lksense_login import Login_Api
class GPU_Update_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        data=GPU_Info_Get_Api().gpu_info_get_api(cookies=cookies).json()
        # print(data)
        avi_list=data['data'][0]['avis']
        # print(avi_list)
        avi_id_list=[]
        for i in avi_list:
            avi_id_list.append(i['id'])
        # print(avi_id_list)
        gpu_id=data['data'][0]['gpu_id']
        id=data['data'][0]['id']
        number=data['data'][0]['number']
        return {'avi_ids':avi_id_list,
                'gpu_id':gpu_id,
                'id':id,
                'number':number}
    def tearDown(self) -> None:
        pass
    def test_gpu_update(self):
        '''
        显卡绑定
        :return:
        '''
        cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        res=GPU_Update_Api().gpu_update_api(json=self.setUp(),cookies=cookies)
        self.assertEqual(res.json()['success'],True,msg='显卡绑定接口测试不通过！')
if __name__ == '__main__':
    unittest.main(verbosity=3)