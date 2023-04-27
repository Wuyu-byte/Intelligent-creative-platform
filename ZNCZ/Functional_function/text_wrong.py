import xmnlp
import re

xmnlp.set_model('ZNCZ\\model_trained\\xmnlp-models')


def text_wrong(text):
    text = str(text)
    # global i
    # pipei = r'\'(.*?)\''
    # pipei2 = r'\((.*?)\,'
    pattern = r"(?<=\().*?(?=,)"  # 匹配(和,之间的字符串
    pattern1 = r"\d+"  # 字符串中的数字
    pattern3 = re.compile(r'[\u4e00-\u9fa5]+')  # 匹配汉字

    result = xmnlp.checker(text, True, 1)
    key_list = result.keys()
    str_keylist = str(key_list)
    index = re.findall(pattern, str_keylist)
    matches = re.findall(pattern1, str(index))
    index_list = list(map(int, matches))
    print(index_list)
    print(result)
    values_list = []
    for key, value in result.items():
        values_list.append(value)
    values_list = pattern3.findall(str(values_list))
    # values_list = ['@' + str(item) + '@' for item in values_list]
    print(values_list)
    for i, index in enumerate(index_list):
        if index < len(text):
            text = text[:index] + values_list[i] + text[index + 1:]

    return text
