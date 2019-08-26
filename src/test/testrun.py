#coding=utf-8  
#jenkins运行项目需要添加sys.path.append
import sys
sys.path.append('/root/.jenkins/workspace/test/src')
import unittest
# import common
from common import base,excel

class TestRun(unittest.TestCase):
    

    def run(self):
        excel.read_excel(base.RunMethod().get_case_url())
        #执行测试用例
        
 
if __name__ == '__main__':
    a = TestRun()
    print('testRun()过了')
    a.run()

    

