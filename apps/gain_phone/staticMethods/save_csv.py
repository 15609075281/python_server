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
        with open(path, 'a+', newline='', encoding='utf-8-sig') as save_c:
            wr_csv = csv.writer(save_c)
            wr_csv.writerows(arr_data)
            print('存在+存储成功')
            save_c.close()
    else:
        with open(path, 'w', newline='', encoding='utf-8-sig') as save_c:
            wr_csv = csv.writer(save_c)
            wr_csv.writerow(arr_)  # 存储数据样式['','']
            wr_csv.writerows(arr_data)  # 存储的数据[{},{}]
            print('不存在+创建存储成功')
            save_c.close()


# 读取本地文件里的数据
def get_read_local_file(path):
    read_file_arr = []
    # 判断文件是否存在
    if os.access(path, os.F_OK):
        # 判断文件是否可读
        if os.access(path, os.R_OK):
            # 对文件进行读写
            with open(path, 'r', newline='', encoding='utf-8-sig') as read1:
                reader_csv = csv.reader(read1)
                for row in reader_csv:
                    read_file_arr.append(row)
                read1.close()
        else:
            # 文件权限限制，不能进行读取
            read_file_arr.append('文件权限限制，不能进行读取')
    else:
        # 文件不存在，不能进行读取
        read_file_arr.append('文件不存在，不能进行读取')
    return read_file_arr


if __name__ == '__main__':
    print('存储数据到本地csv文件')
    # print(get_read_local_file('E:\四川成都\阿土伯四川成都 锦江2018-07-09初始网址.csv'))
