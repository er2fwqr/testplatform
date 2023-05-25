
from django.shortcuts import render
from django.http import HttpResponse
import unittest
from HtmlTestRunner import HTMLTestRunner
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from test0.api_test.cases.lksense_login_test import Login_test
from test0.api_test.cases.lksense_avi_get_test import Avi_Get_test
from test0.api_test.cases.lksense_asset_get_test import Asset_Get_test
# from test0.api_test.cases.lksense_ai_removal_rate_stat_test import Ai_Removal_Rate_Stat_test
from test0.api_test.cases.lksense_asset_average_test import Asset_Average_test
from test0.api_test.cases.lksense_basic_vrsconfig_test import Basic_Vrsconfig
from test0.api_test.cases.lksense_change_vrs_result_test import Change_Vrs_Result_test
from test0.api_test.cases.lksense_config_get_test import Congfig_Get_test
from test0.api_test.cases.lksense_get_user_test import Get_User_test
from test0.api_test.cases.lksense_gpu_info_get_test import GPU_Info_Get_test
from test0.api_test.cases.lksense_gpu_update_test import GPU_Update_test
from test0.api_test.cases.lksense_label_test import Label_test
from test0.api_test.cases.lksense_machine_data_test import Machine_Data_test
from test0.api_test.cases.lksense_machine_manage_test import Machine_manage_test
# from test0.api_test.cases.lksense_main_page_test import Main_Page_test
from test0.api_test.cases.lksense_ngdata_get_test import Ngdata_Get_test
from test0.api_test.cases.lksense_page_permission_test import Page_Permission_test
from test0.api_test.cases.lksense_stack_data_test import Stack_Data_test
from test0.api_test.cases.lksense_turn_page_test import Turn_Page_test
from test0.api_test.bases.base import Request
import configparser

class MyTest(unittest.TestCase):
    def build_param(self,server):
        conf=configparser.ConfigParser()
        conf.read(r'./test0/api_test/lksense.ini')

        pass



    def test_login(self):
        res = requests.post(url='http://192.168.0.177/auth/xlogin',
                            data={'username': 'linksense', 'password': 'lksense@2018'})
        self.assertEqual(res.json()['success'], True)




def run_tests():
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()

    test_classes = [Login_test, Avi_Get_test, Asset_Get_test, Asset_Average_test, Basic_Vrsconfig,
                    Change_Vrs_Result_test, Congfig_Get_test, GPU_Update_test, Get_User_test, GPU_Info_Get_test,
                    Label_test, Machine_Data_test, Machine_manage_test, Ngdata_Get_test,
                    Page_Permission_test, Stack_Data_test, Turn_Page_test]

    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))
    # suite.addTests(loader.discover(r'D:\Python38-32\Scripts\lk_test\test0\api_test\cases'))
    with open('test_report.html', 'w') as f:
        runner = HTMLTestRunner(stream=f, combine_reports=True)
        runner.run(suite)

    # report_file = open('report.html', 'wb')
    # html_test_runner = HTMLTestRunner(stream=report_file,
    #                                  )
    # # 运行用例
    # html_test_runner.run(suite)
    # # 关闭报告文件
    # report_file.close()


def index(request):
    config_files = glob.glob('server_configs/*.ini')

    # 从配置文件中提取服务器名称
    servers = [os.path.splitext(os.path.basename(file))[0] for file in config_files]

    # 将服务器列表传递给模板
    context = {
        'server_configs': servers
    }

    if request.method == 'POST':

        # selected_server = request.POST.get('server')

        #

        run_tests()
        return HttpResponse('Tests executed successfully.')
    else:
        return render(request, 'index.html', context)


import glob


def get_all_reports():
    report_dir = os.path.join(os.getcwd(), 'reports')
    all_reports = glob.glob(os.path.join(report_dir, '*.html'))
    return all_reports


@login_required
def history_report(request):
    all_reports = get_all_reports()
    # 在此处进行适当的处理和筛选以获取所需的历史报告列表
    # 例如，按时间顺序对报告列表进行排序或者根据特定条件进行筛选

    # 执行适当的操作来获取历史报告的列表 `history_reports`
    history_reports = all_reports
    return render(request, 'history_report.html', {'history_reports': history_reports})


def get_latest_report():
    report_dir = os.path.join(os.getcwd(), 'reports')
    list_of_reports = glob.glob(os.path.join(report_dir, '*.html'))
    latest_report = max(list_of_reports, key=os.path.getctime)
    return latest_report


import os
from django.http import HttpResponse


@login_required
def test_report(request):
    file_path = get_latest_report()
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type='text/html')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response


# views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import  redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'index.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def history_report_item(request, report_path):
    with open(report_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type='text/html')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(report_path)
        return response

# import configparser
# class New_Request(Request):
#     def __init__(self, server):
#         self.server = server
#
#     def build_url(self, section, api, config_path=r'D:\Python38-32\Scripts\lk_test\test0\api_test\conf\lksense.ini'):
#         config=configparser.ConfigParser()
#         config.read(r'./api_test/conf/lksense.ini')
#         config.set('server','ip',self.server)
#         with open(r'./api_test/conf/lksense.ini', 'w') as configfile:
#             config.write(configfile)
# Create your views here.

