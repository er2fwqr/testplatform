import unittest,time,os
from test0.api_test.bases.html_test_runner import HTMLTestRunner

class Runner:
    def runner(self):
        '''收集并运行用例'''
        # 实例化 TestSuite 类，创建测试套件
        suite = unittest.TestSuite()
        # 添加测试用例到测试套件中
        # if os.path.exists('cases'):

        #     dir = 'cases' #相对路径
        # else:
        #     dir = '../cases'
        dir=r'D:\Python38-32\Scripts\lk_test\test0\api_test\cases'
        # 添加多个用例|开始加载TestLoader|怎么加载、在哪加载discover|有什么特征
        suite.addTests(unittest.TestLoader().discover(start_dir=dir,pattern='lk*.py'))
        # 创建报告文件,b是二进制
        # 转换时间戳。
        t = time.strftime('%Y-%m-%d_%H-%M-%S')
        if os.path.exists('results'):
            report_path = 'results/reports/test_report%s.html' % t
        else:
            report_path = '../reports/test_report%s.html' % t
        report_file = open(report_path,'wb')

        # 实例化HTMLTestRunner类，运行用例和把测试结果写入到报告文件
        htm_test_runner = HTMLTestRunner(stream=report_file,
                       title='自动化测试报告',
                       description='报告详细信息')
        # 运行用例
        htm_test_runner.run(suite)
        # 关闭报告文件
        report_file.close()

if __name__ == '__main__':
    Runner().runner()