# -*- coding: utf-8 -*-
import os
import random
import re
import time
import urllib
from bs4 import BeautifulSoup
from src import utils, hansMinus

# 获取hans的值，即一个汉字的链接，打开页面
# 读取解析页面enbox，存储到文件
# hans，enbox


def run_app():
    base_url = utils.base_url
    py_base_url = 'zd/py/py/?py='
    # print(base_url)

    with open('../data/hans', 'r') as f:
        hans_list = f.readlines()
        hans_list = list(set(hans_list))

        # 对照hans-，去除已采
        hans_minus_list = hansMinus.fresh_hans_minus()
        hans_minus_list = list(set(hans_minus_list))
        print('len of hans_list:')
        print(len(hans_list))
        print('len of hans_minus_list:')
        print(len(hans_minus_list))
        hans_list2 = []
        for hans1 in hans_list:
            hans_ = hans1.split(',')[1].split('/')[-1]
            if hans_ not in hans_minus_list:
                hans_list2.append(hans1)
        print('len of hans_list_after:')
        print(len(hans_list2))
        hans_list = hans_list2

        with open('../data/char', 'w+', encoding='utf-8') as char_file:

            for i in hans_list:
                # 处理，拼接网址
                i_spl = i.split(',')
                py = i_spl[0]
                hans = i_spl[-1]
                hans = re.search('.*', hans.split('/')[-1]).group()
                # print(str([i_spl, py, hans]))
                hans_ = urllib.parse.quote(hans)
                py_url = base_url + py_base_url + py
                hans_url = base_url + 'hans/' + hans_
                print(py_url + '\n' + hans_url)

                # 访问网页，网页有防盗链机制，跳转到其他页面，所以先访问拼音页面，再访问一次对应汉字页面
                utils.getUrlData(py_url)
                html = utils.getUrlData(hans_url)
                # # print(html)

                # 存储网页
                path = '../data/%s' % py[0]
                print(path)
                if not os.path.exists(path):
                    os.makedirs(path)
                file_path = path + '/%s.html' % hans
                print(file_path)
                if not os.path.exists(file_path):
                    with open(file_path, 'w+') as html_file:
                        html_file.write(html)

                    # 解析网页
                    soup = BeautifulSoup(html, 'html.parser')
                    en_box = soup.select('.enbox > p > p')
                    if en_box:
                        en = en_box[0].string
                        # print(en)
                        record = str([i, hans, en])
                        print(record)
                        char_file.writelines(record + '\n')

                time.sleep(random.uniform(0.1, 0.2))


if __name__ == '__main__':
    # run_app()
    while True:
        try:
            run_app()
        except Exception as e:
            print(e)
            print(e.__class__)
            print(e.__doc__)

            sec = 20
            print('sleep for %s seconds.' % str(sec))
            time.sleep(sec)
            continue





