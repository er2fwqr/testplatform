# 登录
from test0.api_test.bases.base import Request
import configparser,os

class Login_Api:
    # __conf = configparser.ConfigParser()
    # if os.path.exists(r'../conf/'):
    #     __conf.read(r'../conf/lksense.ini', encoding='utf8')
    # else:
    #     __conf.read(r'conf/lksense.ini', encoding='utf8')
    # 从配置文件读取接口信息

    login_url=Request().build_url('login','login_url')
    __user=Request().build_url('user','user')
    __password=Request().build_url('user','password')



    def api_login(self,username=__user,password=__password):

        data = {'username': username,
                'password': password}

        url=self.login_url
        req=Request().send_request(method='p',url=url,data=data)

        return req
if __name__ == '__main__':
    print(Login_Api().api_login().cookies)