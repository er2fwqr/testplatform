'''
翻页（附带整页打点）
'''
from test0.api_test.bases.base import MysqlHelp,Request
from test0.api_test.pages.lksense_login import Login_Api
class Update_Vrs_Result_Api:
    update_vrs_result_url=Request().build_url('vrs','update_vrs_result_url')
    login_url = Request().build_url('login', 'login_url')
    def update_vrs_result(self,data,**kwargs):
        res = Request().send_request(method='p',url=self.update_vrs_result_url,data=data,**kwargs)
        return res
    def build_data(self):
        data={}
        '''
        asset_tbl_tag: "20230118"
        avi_id: "160"
        board_no: 11
        board_option: 4     上一页、下一页选项参数
        is_deny_handle: false
        ?报废板相关，
        is_refresh_ngpoint: true
        ?
        lev1_code: "20230118"
        number: 11
        page: 3
        弃用
        pages: 1
        弃用
        par_code: "bj2m_bmp"
        parent_id: 2884
        pcb_version: "22046498"
        per_page: 1
        random_check: true
        抽检模式：抽看 \全看
        sampling_mode: 1
        stack_id: 2884
        vrs_result: "3"
        vrs_results: []
        vrs_reverse: 1
        zone_code: ""
        
        '''
        return data
if __name__ == '__main__':
    pass

