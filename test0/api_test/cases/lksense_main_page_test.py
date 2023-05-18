from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.pages.lksense_main_page import Main_Page_Api
import unittest,requests
class Main_Page_test(unittest.TestCase):
    def setUp(self) -> None:
        cookies=requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
        return cookies
    def tearDown(self) -> None:
        pass
    def test_main_page(self):
        '''
        主界面html获取
        :return:
        '''
        res =Main_Page_Api().main_page_api(cookies=self.setUp())
        print(res.text)
        self.assertTrue(len(res.text)>200,msg='主界面加载失败，测试不通过！')
if __name__ == '__main__':
    unittest.main(verbosity=3)
    print(Main_Page_Api().main_page_url)