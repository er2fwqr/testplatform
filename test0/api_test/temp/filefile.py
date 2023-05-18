from bases.base import MysqlHelp
from pages.lksense_get_latest_params import Get_Latest_Data
tbl_tag=Get_Latest_Data().get_stack_info()[1]
print(tbl_tag)
data=MysqlHelp().get_data(sql='select id,number from idetect.%s where affiliated_folder_id =1328801'%tbl_tag)
# print(data)
for i in data:
    print('1328801,%s,20230220,%s'%(i[0],i[1]))

