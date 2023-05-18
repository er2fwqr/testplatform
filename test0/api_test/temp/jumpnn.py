from bases.base import MysqlHelp
import openpyxl
import pandas as pd
from datetime import datetime
s='''SELECT aid,number, GROUP_CONCAT(bid) AS ids,affiliated_folder_id
FROM (
  SELECT avi.id as aid,affiliated_folder_id,asset_20230220.id as bid, number, ROW_NUMBER() OVER (PARTITION BY number ORDER BY RAND()) AS rn
  FROM idetect.asset_20230220 LEFT JOIN idetect.avi on par_code=code where affiliated_folder_id=1324933
) AS subquery
WHERE rn <= 5
GROUP BY number
'''
data=MysqlHelp().get_data(sql=s)
with open('./asset_data.csv', 'w', encoding='UTF-8') as fp:
    for i in data:
        page_txt = fp.write('%s,%s,%s,%s\n'%(i[0],i[1],i[2],i[3]))

