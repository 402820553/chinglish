# -*- coding: utf-8 -*-
import json
import random


def input_sentense(in_sentense1='好久不见'):
    print(in_sentense1)
    return in_sentense1


def split_sentense(in_sentense1):
    char_list1 = []
    for i in in_sentense1:
        char_list1.append(i)
    # print(char_list1)
    return char_list1


def tyranslate_char_to_en(char_list1):
    with open('../data/char_en', 'r') as f:
        dict_str_list = f.readlines()
    # print(dict_str_list)
    dict = {}
    for i in dict_str_list:
        trans_json = json.loads(i)
        dict.update(trans_json)
    # print(dict)
    translate_list1 = []
    for i in char_list1:
        if i in dict:
            trans_en = dict[i]
            trans_en_list = trans_en.split(',')
            trans_en_word = random.choice(trans_en_list)
            translate_list1.append(trans_en_word)
        else:
            translate_list1.append(i)
    # print(translate_list1)
    return translate_list1


def output_sentense(translate_list):
    out_sentense1 = ' '.join(translate_list)
    print(out_sentense1)
    return out_sentense1


if __name__ == '__main__':
    # 输入一句话
    in_sentense = input_sentense()

    # 分字
    char_list = split_sentense(in_sentense)

    # 逐字翻译
    translate_list = tyranslate_char_to_en(char_list)

    # 拼接成字符串，输出结果
    out_sentense = output_sentense(translate_list)