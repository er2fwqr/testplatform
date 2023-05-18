# -- coding: utf-8 --**
'''
群组复检翻页接口
'''
import requests

from test0.api_test.bases.base import Request
from test0.api_test.pages.lksense_get_latest_params import Get_Latest_Data
from test0.api_test.pages.lksense_login import Login_Api
class Turn_Page_Api:
    __turn_page_url = Request().build_url('vrs', 'turn_page_url')
    login_url = Request().build_url('login', 'login_url')
    asset_tbl_tag,stack_id,asset_id,board_no=Get_Latest_Data().get_stack_info()[0],Get_Latest_Data().get_stack_info()[2],Get_Latest_Data().get_stack_info()[7],Get_Latest_Data().get_stack_info()[3]
    '''
    翻页接口的url格式为
    http://192.168.0.177/vrs/api/v2/board  + /stack_id/board_no/asset_tbl_tag
    build_complete_url方法对url拼接获取完整
    '''
    def __build_complete_url(self):
        # global complete_url
        complete_url=self.__turn_page_url+'/%s/%s/%s'%(self.stack_id,self.board_no,self.asset_tbl_tag)
        return complete_url
    def turn_page(self,json,**kwargs):
        res=Request().send_request('put',url=self.__build_complete_url(),json=json,**kwargs)
        return res

    def build_assets_data(self):
        '''
        构建需要进行打点的数据
        点数量可以有多个
        :return:[{id: ,vrs_result:1,confirm_type:2},...]
        '''
        return [{'id':self.asset_id,'vrs_result':1,'confirm_type':2}]


if __name__ == '__main__':
    json={
        'assets': Turn_Page_Api().build_assets_data(),
        'is_scarp':False,
        'update_ai_file': False,
        'update_true_file': True
    }
    print(Turn_Page_Api().asset_tbl_tag,Turn_Page_Api().stack_id)
    cookies=requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    url=Turn_Page_Api().turn_page(json=json,cookies=cookies).url
    print(url)
    print(Turn_Page_Api().turn_page(json=json,cookies=cookies).json())
    print(cookies)
