# -*- coding: utf-8 -*-

# 获取title值，即同一拼音的所有汉字
# 请求py链接后，得到汉字列表，记录到文件
# py，hans
import random
import re
import time
from bs4 import BeautifulSoup
from src import utils


if __name__ == '__main__':
    base_url = utils.base_url
    py_url = 'zd/py/py/?py='

    with open('../data/py', 'r') as f:
        py = f.readlines()
        with open('../data/hans', 'w+', encoding='utf-8') as file:
            for i in py:
                i = re.search('.*', i).group()
                url = base_url + py_url + i

                try:
                    # 访问链接，获得汉字列表
                    html = utils.getUrlData(url)
                    soup = BeautifulSoup(html, "html.parser")
                    hans_list = soup.select('li > A')
                    for hans in hans_list:
                        if hans.select('img'):
                            print(hans)
                            continue
                        record = i + ',' + hans['href']
                        file.writelines(record + '\n')
                        print(record)

                except Exception as e:
                    print(e)

                time.sleep(random.uniform(0.1, 0.2))
