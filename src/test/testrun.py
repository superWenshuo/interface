#coding=utf-8  
#jenkins运行项目需要添加sys.path.append
import sys
sys.path.append('/root/.jenkins/workspace/test')
import unittest
from common.excel import read_excel
from common import base

class TestRun(unittest.TestCase):
    

    def run(self):
        read_excel(base.RunMethod().get_case_url())
        #执行测试用例
        
 
if __name__ == '__main__':
    a = TestRun()
    print('testRun()过了')
    a.run()

    

