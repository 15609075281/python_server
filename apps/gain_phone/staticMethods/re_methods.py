# coding=utf-8
import re


# 筛选正确的url
# True为正常的下载地址False为错误
def reUrl(url):
    print('筛选正确的url')
    if url != None:
        if reApk(url) == True:
            if re.match(r'^https?:/{2}\w.+$', url):
                print("This looks valid.")
                boolean_url = True
            else:
                print("This looks invalid.")
                boolean_url = False
        else:
            print('为apk下载地址')
            boolean_url = False
    else:
        print('地址为null', url)
        boolean_url = False

    return boolean_url


# 判断url是不是apk下载地址
# True为正常地址Flase为apk下载地址
def reApk(apk_url):
    r = r'.apk'
    s = re.findall(r, apk_url, re.M | re.S | re.I)
    print(s)
    if len(s) == 0:
        boolean_apk = True
    else:
        boolean_apk = False
    return boolean_apk


# 判断是否是手机号,三大运营商的号段
# 联通
# 130，131，132，155，156，185，186，145，176
# 移动
# 134, 135 , 136, 137, 138, 139, 147, 150, 151,# 152, 157, 158, 159, 178, 182, 183, 184, 187, 188；
# 电信
# 133,153,189
# 返回False为错误
def rePhone(phone):
    print('判断是否是手机号')
    r = r'^1[3|4|5|7|8][0|1|2|3|4|5|6|7|8|9]\d{8}$'  # ^开始符号$结束符号
    p_phone = re.match(r, phone)  # match:按照顺序匹配，如有一个不匹配即为错误。错误返回None
    if p_phone != None:
        boolean_phone = True
    else:
        boolean_phone = False
    return boolean_phone


# 筛选网站的手机号
# 返回未去重复的集合数据
# html_url传入html源码
def refindurlallphone(html_url):
    r = r'1[3|4|5|7|8][0|1|2|3|4|5|6|7|8|9]\d{8}'
    data = re.findall(r, html_url, re.M | re.S | re.I)
    return data


if __name__ == '__main__':
    print('正则开始测试')
    # rePhone('15609075281')
    # reApk('html.url')
    # reUrl('htstp://www.baidu.ssss')
    refindurlallphone('''<div>
    <p>18902030605</p>
    <p>18902030605</p>
    <p>18902043435</p>
    <p>18905404565</p>
    <p>18902030605</p>
</div>''')
