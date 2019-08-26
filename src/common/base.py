'''
Created on 2019年5月26日
request请求服务，并判断是否需要加headers
@author: 文硕
'''
# -*- coding:utf-8 -*-
import requests,os
import json
class RunMethod:
    

    
    #header增加token，保持接口登陆状态，未完成
    headers = {
       # 'userToken': ''
       'Content-Type':'application/x-www-form-urlencoded',
       'cookie':'PHPSESSID=5iao0q0j0l8gg7l4c6s1j7u725; UM_distinctid=1621dc977657a8-05adedf8ee1783-5d4e211f-1fa400-1621dc9776659d; uuid=fef3873b2a83b439d0a0031e0a0ace11948d619d302f0c14ed531186baad6e9ea%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22uuid%22%3Bi%3A1%3Bs%3A32%3A%22d4d8ac38adbe97f22b66bc3bd286fe59%22%3B%7D; shop_list_url_cookie=8c08e0988995b5d75ca1e58371b312b4c4da9c71ebafd1b55e1e5126a6cec6eaa%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22shop_list_url_cookie%22%3Bi%3A1%3Bs%3A0%3A%22%22%3B%7D; __guid=134753697.2524998419452972500.1520934497173.8892; openid=aa93d6b6648b4c2fc95f89220c211eecb7388ae2b816e136cd051f744d0e21eca%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22openid%22%3Bi%3A1%3Bs%3A32%3A%22C80E076DD6F96F1F011A62038BDB2317%22%3B%7D; jumpurl=cb6b4e22ce2528a1c3496e7185537bcfe07ea45ae00c9e4801a3cff90dd1ad5da%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22jumpurl%22%3Bi%3A1%3Bs%3A46%3A%22https%3A%2F%2Fwww.lepu.cn%2Fbeijing%2Fshop%2Fdetail-607160%22%3B%7D; user_id=a5b6907173ad4f3838410d118ad9dcb11a483b8efdd42768971ae2cffb4074b0a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22user_id%22%3Bi%3A1%3Bi%3A67252%3B%7D; monitor_count=2; city_id=011ace3fdbdbcd2d73247c46d0b00b766f558f4221b013e120a29c2924c6b1e1a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22city_id%22%3Bi%3A1%3Bi%3A1%3B%7D; city=127b097aea6a32a636ed2915bae4f1fb76e105ff8dbdecab015b114b13c71c11a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22city%22%3Bi%3A1%3Bi%3A1%3B%7D; Hm_lvt_71f10bf513bb45a54c36988ce8479afb=1520918165; Hm_lpvt_71f10bf513bb45a54c36988ce8479afb=1520936812'
    }
    
    def test_api(self,method,data,url,headers,is_header):
        
        """
        :param method: 请求方法
        :param url: 接口地址
        :param data: 请求参数
        :param headers: headers
        :param is_header: 是否有header
        :return: result -- 接口返回的结果
        1、判断接口请求方式、选择对应的请求
        2、判断是否有header，选择对应请求
        """
        print('进入test_api')
        print(url,data,is_header,'{' in data)
        if method == 'POST' or method == 'post':    # post请求
            if is_header == 'YES' or is_header == 'yes' and data.find('{')!=-1:
                print('222222222')
                res = requests.post(url, json.loads(data), headers=headers)
            elif is_header == 'no' or is_header == 'NO' and data.find('{')!=-1:
                print(json.loads(data))       # 无header
                res = requests.post(url, json.loads(data))
            elif is_header == 'no' or is_header == 'NO' and data.find('{')==-1:
                res = requests.post(url, data)
                print('1111')
            elif is_header == 'YES' or is_header == 'yes' and  data.find('{')==-1:
                print('222222222')
                res = requests.post(url, data, headers=headers)
            result = res.json()
            print(result)
        else:       # get请求
            #如果需要header
            if is_header == 'YES' or is_header == 'yes':
                res = requests.get(url, data,headers=headers)
                result = res.json()
                print(result)
            #不需要header
            else:
                res = requests.get(url, data)
                result = res.json()
                print(result)
        return result
#         except Exception as e:
#             logger().error('请求时失败：{}'.format(e))

    
    def get_case_url(self):
        #当前路径的父包
        p =os.path.abspath('..')
        print(p)
        excelPath=lambda x:os.path.join(p, "data", x)
        print(excelPath('DaoLend_case1.xlsx'))
        return excelPath('DaoLend_case1.xlsx')
  