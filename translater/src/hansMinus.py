# -*- coding: utf-8 -*
import os
from pathlib import Path

# 读取已采集文件列表，生成已采文件清单，返回清单


def fresh_hans_minus():
    with open('../data/hans-', 'w+') as f:
        data_root = '../data'
        filelist = os.listdir(data_root)
        # print(filelist)
        for i in filelist:
            dir_ = data_root + '/' + i
            if Path(dir_).is_dir():
                filelist_2 = os.listdir(dir_)
                # print(filelist_2)
                for filename in filelist_2:
                    hanschar = filename.split('.')[0] + '\n'
                    f.writelines(hanschar)
    hans_minus_list = open('../data/hans-', 'r').readlines()
    print('hans_minus_list:')
    print(hans_minus_list)
    print('len of hans_minus_list:')
    print(len(hans_minus_list))
    return hans_minus_list


if __name__ == '__main__':
    fresh_hans_minus()
