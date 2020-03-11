# -*- coding: utf-8 -*
import json

# 有的中英翻译中有多个单词组成的翻译，将这些翻译剔除。


def fresh_hans_minus():
    # 读取全部翻译
    with open('../data/char', 'r') as f:
        char_list = f.readlines()

    with open('../data/char_en', 'r') as en_file_:
        en_file_list = en_file_.readlines()

    with open('../data/char_en', 'w+') as en_file:
        # 处理字符串
        for char_str in char_list:
            # print(char_str)
            char_spl = char_str.split('\',')
            # print(char_spl)
            char = char_spl[1]
            en = char_spl[2]
            char = char.replace('\'', '').replace(' ', '')
            en = en.replace('\'', '').replace(']', '').replace('\n', '')
            print(char)
            print(en)

            # 筛选掉非单个英语单词的翻译
            en_list = en.split(',')
            en_list2 = []
            for en2 in en_list:
                en_list2.append(en2.split(';'))

                # 将enlist2展平
            en_list2 = sum(en_list2, [])
            # print(en_list2)

            for en3 in en_list2:
                en_spl = en3.split(' ')
                # print(en_spl)
                if len(en_spl) > 2:
                    en_list2.pop(en_list2.index(en3))
                    # print('pop')
                    # print(en3)
            en_list3 = []
            for i in en_list2:
                en_list3.append(i.replace(' ', ''))
            if len(en_list3) > 0:
                en_str = ','.join(en_list3)
                print(en_str)
                data = {char: en_str}
                json1 = json.dumps(data, ensure_ascii=False)

                if json1 not in  en_file_list:
                    en_file.writelines(json1 + '\n')
                    print('writing')
                    print(json1)
                else:
                    print('exist')


if __name__ == '__main__':
    fresh_hans_minus()