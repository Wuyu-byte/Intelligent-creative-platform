import jiagu


def keywords_draw(text):

    keywords = jiagu.keywords(text, 5)
    return keywords
