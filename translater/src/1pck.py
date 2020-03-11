# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from src import utils

# 爬取 https://www.zdic.net/zd/py/ 下所有的 <dt><a class="pck" title="a">a</a></dt>
# 获取title的值，即拼音，记录到文件
# py


if __name__ == '__main__':

    base_url = utils.base_url
    py_url = 'zd/py/'

    html = utils.getUrlData(base_url + py_url)
    soup = BeautifulSoup(html, "html.parser")
    pys = soup.select('dt > a')

    with open('../data/py', 'w+', encoding='utf-8') as f:
        for a in pys:
            f.writelines(a.string + '\n')

        f.close()
