'''
vrs平均报点获取接口
'''
import requests,pymysql


from test0.api_test.bases.base import Request, MysqlHelp
from test0.api_test.pages.lksense_login import Login_Api


class Asset_Average_Api:
    asset_average_url = Request().build_url('vrs', 'asset_average_url')
    login_url = Request().build_url('login', 'login_url')



    '''
    build_params方法，用于构造用于测试接口的参数，从数据库取出最新的stack_id并构建一系列参数
    '''

    def build_params(self):
        sql1 = 'SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = %s AND table_rows > 0 and table_name RLIKE %s ORDER BY table_name DESC LIMIT 1;' % (
        '"idetect"', '"asset_[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"')
        # sql2=
        asset_tbl = MysqlHelp().get_data(
            sql=sql1)[0][0]
        asset_tbl_tag=asset_tbl[6:14]
        sql2='select affiliated_folder_id from idetect.%s '%asset_tbl
        stack_list=MysqlHelp().get_data(sql=sql2)

        stack_id=stack_list[0][0]
        sql3='select avi_code from idetect.%s where affiliated_folder_id=%s  '%(asset_tbl,stack_id)
        avi_code=MysqlHelp().get_data(sql=sql3)[0][0]
        avi_id=MysqlHelp().get_data(sql='select id from idetect.avi where code="%s"'%avi_code)[0][0]
        # print(avi_id)
        params = {
            'stack_id':stack_id,
            'asset_tbl_tag': asset_tbl_tag,
            'avi_id':avi_id

        }
        return params



    '''
    asset_average_api方法，根据构造好的参数发送请求
    得到接口返回值
    '''
    def asset_average_api(self, params, **kwargs):
        res = Request().send_request('g', url=self.asset_average_url, params=params, **kwargs)
        return res



    '''
    get_total_asset方法，从数据库直接获取总报点数
    用于跟接口返回值做检验，验证接口返回值的正确性
    '''
    def get_total_asset(self):
        params=self.build_params()
        total_asset=MysqlHelp().get_data(sql='SELECT * FROM idetect.asset_%s WHERE affiliated_folder_id="%s"'%(params['asset_tbl_tag'],params['stack_id']))
        return len(total_asset)



if __name__ == '__main__':
    params = Asset_Average_Api().build_params()
    print(params)

    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    res = Asset_Average_Api().asset_average_api(params=params, cookies=cookies)
    print(res.json())


