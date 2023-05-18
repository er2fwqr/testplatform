'''
根据给定的机台类型、数据源
'''
from bases.base import Ssh_server
from pages.lksense_create_machine import Create_Machine_Api
class Auto_run_data:
    def set_algend(self,hostname, port, username, password,al_path):
        #     基于算法路径安装算法
        wing=Ssh_server(hostname,port,username,password)
        res=wing.run_cmd('/opt/virtualenvs/defect_detect/bin/pip install -U %s'%al_path)
        wing.close()
        if 'success' or 'already' in res.decode('utf-8'):
            return 'success'
        else:
            return 'failed'
    def set_model(self):
        pass
    def set_machine(self):
        pass
    def set_aftercure(self):
        pass
    def check_and_set_enviroment(self,hostname, port, username, password):
        '''
        连接服务器使用supervisor检查是否有机台检测进程
        :return:
        '''
        checker=Ssh_server(hostname,port,username,password)
        prcs=checker.run_cmd('supervisorctl')
        checker.close()
        if '机台对应进程' in prcs.decode('utf-8'):
            pass
        else:
            '''
            使用ln -s在supercisor添加相应进程
            缓缓飘落的枫叶像思念
            '''
            adder=Ssh_server(hostname,port,username,password)
            adder.run_cmd('ln -s /opt/software/detection/%s /etc/supervisord.d '%'机台对应进程')
            adder.run_cmd('supervisorctl update')
            add_res=adder.run_cmd('supervisorctl')
            if '机台对应进程' in add_res.decode('utf-8'):
                pass
            else:
                return 'add process failed'
            adder.close()

