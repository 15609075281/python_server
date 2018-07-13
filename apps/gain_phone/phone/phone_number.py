# coding=utf-8

import requests
from bs4 import BeautifulSoup
from apps.gain_phone.staticMethods import re_methods


# 模拟浏览器
headers = {
    'UserAgent': 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'
}

# 第一网页上的所有url存储器
list_url = []


# 从首页上面获取所有的url
def get_home_url(http_url):
    print('开始执行获取首页url')
    # 设置不显示https的ssl认证警告
    requests.packages.urllib3.disable_warnings()
    # 设置代理ip
    # proxy = {'http': ''}
    one_html = requests.get(http_url, headers=headers, verify=False)  # verify=False设置跳过ssl验证
    one_soup = BeautifulSoup(one_html.text, 'html.parser')
    for one_var in one_soup.select('a'):
        ar_url = one_var.get('href')
        if len(list_url) < 100:
            if re_methods.reUrl(ar_url):
                # True地址正确
                list_url.append(ar_url)
                print('地址正确:', ar_url)
            else:
                # False地址错误
                print('地址错误:', ar_url)
        else:
            print('我还有哟')
    print('首页url地址获取完毕')
    # 进入首页获取的url的详情页，获取详情页上面的电话号码
    for phone_var_url in list_url:
        get_phone_number(phone_var_url)


# 通过输入url直接获取当前url上的所有手机号
def get_phone_number(phone_url):
    phone_html = requests.get(phone_url,headers=headers, verify=False)
    phone_html.encoding=phone_html.apparent_encoding
    phone_html=phone_html.text
    phone_list = re_methods.refindurlallphone(phone_html)
    phone_list = set(phone_list)
    print('获得手机号有', phone_list)


if __name__ == '__main__':
    print('获取网站的url')
    get_home_url('http://baidu.com/')
