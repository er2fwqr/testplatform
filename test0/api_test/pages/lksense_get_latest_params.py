'''
获取最新一天
'''
from test0.api_test.bases.base import MysqlHelp


class Get_Latest_Data:
    '''
    获取最近有数据的asset表名和其中的第一叠板id
    数据取第一叠不取最后一叠原因：
    若测试过程中ai仍在持续检板，最新数据会随时变化，影响测试数据的稳定性
    '''

    def get_stack_info(self):
        '''
        0asset_tbl_tag:asset表日期,
        1asset_tbl：表名,
        2stack_id，叠id,
        3board_number：板号,
        4avi_id，机台id,
        5par_code：解析方案代码,
        6pcb_code：叠代号,
        7asset_id：点id

        '''
        sql1 = 'SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = %s AND table_rows > 0 and table_name RLIKE %s ORDER BY table_name DESC LIMIT 1;' % (
            '"idetect"', '"asset_[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"')#取最近的非空asset表
        global asset_tbl_tag
        asset_tbl = MysqlHelp().get_data(
            sql=sql1)[0][0]
        asset_tbl_tag = asset_tbl[6:14]

        sql2 = 'select affiliated_folder_id from idetect.%s ' % asset_tbl#取其中所有stack_id
        stack_list = MysqlHelp().get_data(sql=sql2)

        stack_id = stack_list[0][0]#取第一叠的stack_id
        sql3 = 'select number,avi_code,par_code,pcb_code,id from idetect.%s where affiliated_folder_id=%s order by id limit 1 ' % (
        asset_tbl, stack_id)#取该叠第一张板第一个点的所有相关信息
        board_number, avi_code, par_code,pcb_code,asset_id = MysqlHelp().get_data(sql=sql3)[0][0], MysqlHelp().get_data(sql=sql3)[0][1], \
                                           MysqlHelp().get_data(sql=sql3)[0][2],MysqlHelp().get_data(sql=sql3)[0][3],MysqlHelp().get_data(sql=sql3)[0][4]
        avi_id = MysqlHelp().get_data(sql='select id from idetect.avi where code="%s";' % avi_code)[0][0]
        return asset_tbl_tag, asset_tbl, stack_id, board_number, avi_id,par_code,pcb_code,asset_id
        '''
        :return:(0：表日期，1：表名，2：叠号，3：板号，4：机台id，5：解析方案代码，6：叠代号，7：点id)
        '''

if __name__ == '__main__':
    stack_info = Get_Latest_Data().get_stack_info()
    print(stack_info)
