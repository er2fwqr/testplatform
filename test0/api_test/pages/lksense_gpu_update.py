# 绑定显卡
import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_login import Login_Api


class GPU_Update_Api:
    gpu_update_url = Request().build_url('gpu_manage', 'gpu_update_url')
    login_url = Request().build_url('login', 'login_url')

    def gpu_update_api(self, json, cookies):
        res = Request().send_request(method='p', url=self.gpu_update_url, json=json, cookies=cookies)
        return res


if __name__ == '__main__':
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    json = {"avi_ids": [160, 169, 195, 197, 200, 204],
            "gpu_id": 3,
            "id": 3,
            "number": 0}
    res = GPU_Update_Api().gpu_update_api(json=json,cookies=cookies)
    print(res.json())
