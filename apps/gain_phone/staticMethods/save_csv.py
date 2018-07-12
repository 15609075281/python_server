# coding=utf-8
import csv
import os
import datetime
import time


# 存储到本地csv文件夹里
def save_csv(path, arr_, arr_data):
    print('存储到本地csv文件夹里')
    # 判断文件是否存在
    if os.access(path, os.F_OK):
        with open(path, 'a+', newline='', encoding='utf-8-sign') as save_c:
            wr_csv = csv.writer(save_c)
            wr_csv.writerows(arr_data)
            print('存在+存储成功')
            save_c.close()
    else:
        with open(path, 'w', newline='', encoding='utf-8-sign') as save_c:
            wr_csv = csv.writer(save_c)
            wr_csv.writerow(arr_)  # 存储数据样式['','']
            wr_csv.writerows(arr_data)  # 存储的数据[{},{}]
            print('不存在+创建存储成功')
            save_c.close()


if __name__ == '__main__':
    print('存储数据到本地csv文件')
