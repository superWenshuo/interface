#coding=utf-8 
'''
Created on 2019年5月23日

@author: wenshou
'''
from xlutils import copy
import xlrd,time
from common import base
import os
from common.base import RunMethod
# import common.base.RunMethod.test_api

#读取excel值
def read_excel(filename):
    
    try:
        book= xlrd.open_workbook(filename)
        print('读取excel')
        #获取标签页数
        sheets = len(book.sheets())
        if (sheets>0):
            print('excel有内容')
            for i in range(sheets):
                sheet = book.sheet_by_index(i)#取第一个sheet页
                rows= sheet.nrows#取这个sheet页的所有行数  
                print ('进入读取excel,总共行数：',rows)
                case_list = []#保存每一条case  
                for i in range(rows):  
                    if i !=0:  
                        #把每一条测试用例添加到case_list中  
                        case_list.append(sheet.row_values(i))
                print(u'结果',case_list)
                

        #请求接口，并返回报告
#         get_response(case_list,RunMethod().get_case_url())
            get_response(case_list)
        
    except Exception as e:
        print (u'路径不在或者excel不正确',e)
        


       
    
"""
判断接口URL，请求方式，发请求并
存测试结果的list
"""
def get_response(case_list): 
    #存请求报文的list
    request_urls = []  
    #存测试结果的list
    global res_flags
    res_flags = []
    #存返回报文的list
    responses = []
    print(u'读取excel的结果',case_list)
      
    
    for case in case_list: 
        try:  
            ''''' 
            这里捕捉一下异常，如果excel格式不正确的话，就返回异常 
            '''  
            #用例id，提bug的时候用  
            global case_id
            case_id = case[0]  
            #
            interface_name = case[1]
            #功能描述  
            global case_detail
            case_detail = case[2]  
            #url
            url = case[3]
            #请求方式  
            method = case[4]  
            #参数
            data = case[5]  
            #是否带header  
            is_header = case[6]  
            #检查点 
            check_points = case[7]  
         

            #返回结果
            results= RunMethod().test_api(method, data, url, base.RunMethod.headers, is_header)
            responses.append(results);
            #判断测试结果
            if 'T' in check(check_points, responses):
                res_flags.append("pass") 
            else:
                res_flags.append("fail") 
            
            
        except Exception as e:  
            return '测试用例格式不正确！%s'%e 
        
    copy_excel(base.RunMethod().get_case_url(),responses,res_flags)    
        
def copy_excel(file_path,real_results,res_flags):  
    ''''' 
    :param file_path: 测试用例的路径 
    :param res_flags: 测试结果的list 
    :return: 
    '''  
    ''''' 
    这个函数的作用是写excel，把请求报文、返回报文和测试结果写到测试用例的excel中 
    因为xlrd模块只能读excel，不能写，所以用xlutils这个模块，但是python中没有一个模块能 
    直接操作已经写好的excel，所以只能用xlutils模块中的copy方法，copy一个新的excel，才能操作 
    '''  
    #打开原来的excel，获取到这个book对象  
    book = xlrd.open_workbook(file_path)  
    #复制一个new_book  
    new_book = copy.copy(book)  
    #然后获取到这个复制的excel的第一个sheet页  
    sheet = new_book.get_sheet(0)  
    i = 1
    print('12')
    for flag,real_result in zip(res_flags,real_results):  
        ''''' 
            同时遍历请求报文、返回报文和测试结果这3个大的list 
            然后把每一条case执行结果写到excel中，zip函数可以将多个list放在一起遍历 
            因为第一行是表头，所以从第二行开始写，也就是索引位1的位置，i代表行 
            所以i赋值为1，然后每写一条，然后i+1， i+=1同等于i=i+1 
            请求报文、返回报文、测试结果分别在excel的8、9、11列，列是固定的，所以就给写死了 
            后面跟上要写的值，因为excel用的是Unicode字符编码，所以前面带个u表示用Unicode编码 
            否则会有乱码 
        ''' 

        sheet.write(i,8,u'%s'%real_result) 
        sheet.write(i,9,u'%s'%flag) 
        i+=1     
        '''
                保存在excel的包下,p：当前路径的父包，
        os.path.join：进入当前路径的package
        format:
        '''
        p =os.path.abspath('..')
        excel_path=os.path.join(p, "result")
        excel_path1=os.path.join(excel_path, "excel_result")   
        print('{}/{}_测试结果.xls'.format(excel_path1,time.strftime('%Y%m%d%H%M%S')))
        new_book.save('{}/{}_测试结果.xls'.format(excel_path1,time.strftime('%Y%m%d%H%M%S'))) 
        #jenkins附件excel，name固定
        new_book.save('{}/jenkins_case.xls'.format(excel_path1)) 

def check(a,b):
    '''
    a=预期结果，b=实际结果
    b包含a 则接口返回成功
    '''
#     print("%s,%s"%(a,b))
    print(type(b))
    b1=str(b)
    if a in b1:
        print("a:",a)
        print("b:",b)
        return 'T'
    elif a not in b:
#         print("a:",a)
#         print("b:",b)
        return  'F' 
