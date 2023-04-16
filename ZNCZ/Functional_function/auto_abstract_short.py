import jiagu


def auto_abstract_short(text):

    summarize = jiagu.summarize(text, 2)  # 摘要
    # print(summarize)
    return summarize
