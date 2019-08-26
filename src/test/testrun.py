#coding=utf-8  
#jenkins运行项目需要添加sys.path.append
import sys
# print (sys.path)
# sys.path.append('/root/.jenkins/workspace/test/src/test')
# sys.path.append('/usr/local/python3.5/lib/python35.zip')
# sys.path.append('/usr/local/python3.5/lib/python3.5')
# sys.path.append('/usr/local/python3.5/lib/python3.5/plat-linux')
# sys.path.append('/usr/local/python3.5/lib/python3.5/lib-dynload')
# sys.path.append('/usr/local/python3.5/lib/python3.5/site-packages')






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

    

