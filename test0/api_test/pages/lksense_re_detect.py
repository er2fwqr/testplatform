'''
群组复检中批量重检接口

'''
import random

import requests

from test0.api_test.bases.base import Request, MysqlHelp
from test0.api_test.pages.lksense_login import Login_Api
from test0.api_test.pages.lksense_get_latest_params import Get_Latest_Data


class Re_Detect_Api:
    re_detect_url = Request().build_url('vrs', 're_detect_url')
    login_url = Request().build_url('login', 'login_url')

    def get_post_json(self):
        '''
        重检请求信息格式：
        {'asset_folder_id':_,
        'numbers':_,
        'sides':['a1','b1'...],
        'table_tag':_
        }
        :return:
        '''
        stack_info=Get_Latest_Data().get_stack_info()
        json={
            'asset_folder_id':stack_info[2],
            'numbers':stack_info[3],
            'sides':[],
            'table_tag':stack_info[0]
        }
        board_tables = MysqlHelp().get_data(
            sql='SELECT DISTINCT table_name FROM information_schema.columns WHERE column_name = "side_status"')
        print(board_tables)
        target_tab = []

        for tab in board_tables:
            print(tab[0])
            table_data = MysqlHelp().get_data(
                sql='select side_status from idetect.%s where side_status like "%a1_status": 4%"' % tab[0])
            if table_data != []:
                target_tab.append(tab)
        print(target_tab)
        k = 0

        available_data = []
        '''
        遍历所有board表，直到有可用数据（a1_status=4）
        根据该数据构建消息体
        发送请求
        
        
        
        '''
        while not k:
            target_table = random.choice(target_tab)[0]
            # print(target_table)
            sql = 'select * from idetect.%s ' % target_table
            # print(sql)
            table_data = MysqlHelp().get_data(sql=sql)
            '''
            table_data是整张表的数据
            t为其中一条，也就是一块板的数据
            '''
            global t
            for t in table_data:
                print(str(t[6]))

                if str(t[6]).split('{"a1_status": ')[1].split(', "a2_status":')[0] == str(4) and t != [] and type(
                        t[6]) != 'int' and len(t) > 6 and t[6] != () and '{"a1_status": 4' in str(
                    t[6]) and ', "a2_status":' in str(t[6]):

                    k = 1

                    available_data.append(t)
                    print(len(available_data), k)
                    break
                else:
                    continue
                break

            # print(available_data)
            # source_data = t
        post_data = {
            'asset_folder_id': t[2],
            'numbers': t[3],
            'sides': {
                0: "a1",
                1: "b1"},
            'table_tag': target_table}

        return post_data

    def re_detect_api(self, json, **kwargs):

        res = Request().send_request(method='p', url=self.re_detect_url, json=json, **kwargs)
        return res


if __name__ == '__main__':
    json = Re_Detect_Api().get_post_json()
    cookies = requests.utils.dict_from_cookiejar(Login_Api().api_login().cookies)
    print(Re_Detect_Api().re_detect_api(json=json, cookies=cookies).status_code)
