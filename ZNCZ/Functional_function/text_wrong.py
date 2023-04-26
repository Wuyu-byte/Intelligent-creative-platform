import xmnlp
import re

xmnlp.set_model('ZNCZ\\model_trained\\xmnlp-models')


def text_wrong(text):
    text = str(text)
    global i
    pipei = r'\'(.*?)\''
    pipei2 = r'\((.*?)\,'
    result = xmnlp.checker(text, True, 1)
    print(result)
    key = str((next(iter(result))))
    key = str(re.findall(pipei2, key))
    key = key.replace("['", "")
    index = int(key.replace("']", ""))
    key = text[index - 1] + text[index] + text[index + 1]

    for i in result.values():
        i = str(i)
        i = str(re.findall(pipei, i))
        i = i.replace("['", "")
        i = i.replace("']", "")

    result = i
    result = key.replace(text[index], result)

    return key + '-->' + result
