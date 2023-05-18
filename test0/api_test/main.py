'''
执行代码入口
未实现：打出测试服务器
'''
import time
from configparser import ConfigParser
import os
import configparser

from runner.runner_test import Runner
from bases.base import Request
class Lksense:
    # def __init__(self,user_info):
    #     self.user_info=user_info


    def run(self):
        Runner().runner()

if __name__ == '__main__':
    user_info = input()
    wuser,wpassword,ip,suser,spassword,ppassword=user_info.split(',')[0],user_info.split(',')[1],user_info.split(',')[2],user_info.split(',')[3],user_info.split(',')[4],user_info.split(',')[5]


    # 使用输入的数据对配置文件进行替换
    cp=ConfigParser()
    cp.read(r'conf/lksense.ini', encoding='utf8')
    cp.set('user','user',wuser)
    cp.set('user','password',wpassword)
    cp.set('server','ip',ip)
    cp.set('server','user',suser)
    cp.set('server','password',spassword)
    cp.set('server','mysqlpassword',ppassword)
    cp.write(open(r'conf/lksense.ini','w',encoding='utf-8'))

    with open(r'conf/lksense.ini', 'w', encoding='utf-8') as file:
        cp.write(file)
        os.fsync(file.fileno())

    server = Request().build_url('server', 'ip')
    print('正在测试%s服务器'%server+'\n'+'"."代表用例通过，"E"代表代码执行错误，"F"代表用例不通过')
    Lksense().run()
    print('用例执行完毕')
    # linksense,lksense@2018,192.168.0.177,root,lktime-dev,P@ss1234
    # wangyiran,wangyiran,192.168.0.174,root,lktime-t,P@ss1234