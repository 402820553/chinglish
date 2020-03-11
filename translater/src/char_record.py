# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# 发现漏采了很多翻译，对已经下载的汉字页面进行读取，重新解析
# 生成字典


def run_app():
    with open('../data/char', 'r') as f:
        char_list = f.readlines()
        print(char_list)

    with open('../data/char', 'w+', encoding='utf-8') as char_file:
        char_list = list(set(char_list))
        char_file.writelines(char_list)

        # 获取../data目录下的文件
        data_root = '../data'
        filelist = os.listdir(data_root)
        # print(filelist)
        filelist.sort()
        for i in filelist:
            dir_ = data_root + '/' + i
            print(dir_)
            # 判断是否文件夹
            if Path(dir_).is_dir():
                # 获得字母文件夹下的汉字html文件
                filelist_2 = os.listdir(dir_)
                # print(dir_)
                print(filelist_2)
                for filename in filelist_2:
                    filename = re.search('.*', filename).group()
                    filepath = dir_ + '/' + filename
                    print(filepath)
                    # 读取文件内容
                    with open(dir_ + '/' + filename, 'r') as html:
                        # print(html)
                        # 解析网页
                        soup = BeautifulSoup(html.read(), 'html.parser')
                        # print(soup)
                        en_box = soup.select('.enbox > p')
                        # print(en_box)
                        if en_box:
                            en = en_box[0].text
                            if en:
                                en = en.replace('英语 ', '')
                                # print(en)
                                hans = filename.split('.')[0]
                                record = str([i, hans, en])

                                record = record + '\n'
                                print(record)
                                if record not in char_list:
                                    char_file.writelines(record)


if __name__ == '__main__':
    run_app()
    # while True:
    #     try:
    #         run_app()
    #     except Exception as e:
    #         print(e)
    #         print(e.__class__)
    #         print(e.__doc__)
    #
    #         sec = 20
    #         print('sleep for %s seconds.' % str(sec))
    #         time.sleep(sec)
    #         continue





