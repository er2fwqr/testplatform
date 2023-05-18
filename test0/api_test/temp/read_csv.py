import csv,os
from ddt import ddt,data,unpack
from bases.base import CsvHelp
@ddt()
class Read:
    if os.path.exists(r'../data/'):
        testcsv=CsvHelp().get_csv_data(r'../data/account.csv')
    @data(*testcsv)
    @unpack
    def rd(self,a1,a2,a3):
        print(a1,a2,a3)

s=Read()
s.rd()

