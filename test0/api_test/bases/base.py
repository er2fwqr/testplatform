import configparser
import os

import paramiko
import pymysql
import requests,csv,socket
from requests import Session


class Request:
    def build_url(self,section,api,config_path=r'D:\Python38-32\Scripts\lk_test\test0\api_test\conf\lksense.ini'):
        conf = configparser.ConfigParser()

        conf.read(config_path, encoding='utf8')
        url=conf.get(section,api).replace('192.168.0.177',conf.get('server','ip'))
        return url




    def send_request(self,method,url,params=None,data=None,json=None,**kwargs):
        '''
         统一get、post请求
        :param method: 请求方法
        :param url: 请求url
        :param params: get方法需要的参数，通常是字典格式的键值对、或者符合url规则的字符串
        :param data: post方法需要的参数，通常是字典格式的键值对，充当表单数据
        :param json: post方法需要的参数，通常是严格的json数据模型，充当消息体
        :param kwargs: get、post需要请求头、cookies等关键参数
        :return: Response
        '''
        if method in ('g','get','G','GET'):
            res = requests.get(url=url,params=params,**kwargs)
        elif method in ('put','PUT'):
            res=requests.put(url=url,data=data,json=json,**kwargs)
        elif method in ('p','post','P','POST'):
            res = requests.post(url=url,data=data,json=json,**kwargs)
        elif method in ('d','delete','D','DELETE'):
            res=requests.delete(url=url,**kwargs)
        else:
            raise Exception('暂不支持其他请求')
        return res

    def session(self):
        return Session()

class CsvHelp:

    def get_csv_data(self,file,mode='r',encoding='utf8',del_title=True):
        '''
        封装csv，得到python常用的参数传递模型[(),(),()...]
        :param file: 文件路径
        :param mode: 读取模式。open函数需要的参数
        :param encoding: 以何种编码格式读取文件。open函数需要的参数
        :param del_title: 是否删除首行，默认删除
        :return: python常用的参数传递模型[(),(),()...]
        '''
        l = []
        f = open(file,mode=mode,encoding=encoding)
        csv_data = csv.reader(f)
        for i in csv_data:
            l.append(tuple(i))
        f.close()
        if del_title:
            l.pop(0)
        return l
class Internet_Help:
    def get_ip(self):
        local_ip = socket.gethostbyname(socket.gethostname())

        return local_ip
class MysqlHelp:
    __conf = configparser.ConfigParser()

    # if os.path.exists('D:\Python38-32\Scripts\lk_test\test0\api_test\conf\lksense.ini'):
    #     print('got data')
    #     __conf.read('D:\Python38-32\Scripts\lk_test\test0\api_test\conf\lksense.ini', encoding='utf8')
    #
    # else:
    #     __conf.read(r'conf/lksense.ini', encoding='utf8')
    __conf.read(r'D:\Python38-32\Scripts\lk_test\test0\api_test\conf\lksense.ini', encoding='utf8')
    host=__conf.get('server','ip')
    user=__conf.get('server','user')
    # print(host,user)
    password=__conf.get('server','mysqlpassword')

    def get_data(self, sql, host=host, port=3306, user=user, password=password):
        l = []
        # 连接mysql数据库的四个基本参数:数据库的ip或域名、端口、用户名/密码
        db = pymysql.Connect(host=host, port=port, user=user, password=password, autocommit=True)
        # autocommit:执行sql后自动提交
        # 根据数据库的连接，得到游标对象

        cursor = db.cursor()

        # 通过游标执行sql语句
        cursor.execute(sql)
        # 接收执行后的返回结果
        data = cursor.fetchall()
        db.commit()
        for i in data:
            # print(i)
            l.append(tuple(i))
            # **关闭资源
            # 先关游标，再关连接
        cursor.close()
        db.close()
        return l
class Ssh_server:
    __conf = configparser.ConfigParser()

    # if os.path.exists(r'../conf/'):
    #     __conf.read(r'../conf/lksense.ini', encoding='utf8')
    # else:
    #     __conf.read(r'conf/lksense.ini', encoding='utf8')
    __conf.read(r'D:\Python38-32\Scripts\lk_test\test0\api_test\conf\lksense.ini', encoding='utf8')
    hostname=__conf.get('server','ip')
    username=__conf.get('server','user')
    password=__conf.get('server','password')
    def __init__(self, hostname=hostname, port=22, username=username, password=password):
        self.hostname = hostname
        self.password = password
        self.port = int(port)
        self.username = username
        self.ssh = paramiko.SSHClient()  # 创建SSH对象
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
        self.ssh.connect(self.hostname, self.port, self.username, self.password)  # 连接服务器
        self.ssh_sftp = self.ssh.open_sftp()

    def run_cmd(self, cmd):  # cmd为传入的命令
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read()

    def put(self, localpath, remotepath):  # 上传方法
        self.ssh_sftp.put(localpath, remotepath)

    def get(self, remotepath, localpath):  # 下载方法
        self.ssh_sftp.get(remotepath, localpath)

    def close(self):  # 关闭连接
        self.ssh_sftp.close()
        self.ssh.close()



