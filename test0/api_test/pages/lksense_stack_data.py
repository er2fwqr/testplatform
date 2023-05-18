'''
群组复检界面打开叠数据接口
可能存在的问题：
由于board_count的取值来自于单日的board表，在处理跨天数据时取值可能不准确

'''
import requests, time

from test0.api_test.bases.base import Request, MysqlHelp
from test0.api_test.pages.lksense_login import Login_Api


class Stack_Data_Api:
    stack_data_url = Request().build_url('vrs', 'stack_data_url')
    login_url = Request().build_url('login', 'login_url')

    '''
    需要参数仅为叠id，从数据库中取当日第一叠的id
    不取最新检出叠的原因：若处于检板状态，新数据持续产生，前后校验可能不准
    '''

    def __build_params(self):
        sql1 = 'SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = %s AND table_rows > 0 and table_name RLIKE %s ORDER BY table_name DESC LIMIT 1;' % (
            '"idetect"', '"asset_[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"')
        global asset_tbl_tag
        asset_tbl = MysqlHelp().get_data(
            sql=sql1)[0][0]
        asset_tbl_tag = asset_tbl[6:14]

        sql2 = 'select affiliated_folder_id from idetect.%s ' % asset_tbl
        stack_list = MysqlHelp().get_data(sql=sql2)

        stack_id = stack_list[0][0]
        params = {'stack_id': stack_id}
        return params

    def stack_data_api(self, **kwargs):
        params = self.__build_params()
        res = Request().send_request(method='g', url=self.stack_data_url, params=params, **kwargs)
        return res.json()

    '''
    获取数据库中该叠号下真实的板数量，用于跟接口获取的数据做校验
    '''

    def get_board_count(self):
        stack_id = self.__build_params()['stack_id']
        board_count = MysqlHelp().get_data(
            sql='select count(*) from idetect.board_%s where affiliated_folder_id=%s' % (asset_tbl_tag, stack_id))
        return board_count[0][0]


if __name__ == '__main__':
    params = {'stack_id': 2884}
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    result = Stack_Data_Api().stack_data_api(cookies=cookies)
    print(len(result['board_pool']))
    # print(Stack_Data_Api().get_board_count())
