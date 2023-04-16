import jiagu
import datetime
import json


def auto_abstract_long(text):
    # fin = open('./data/input.txt', 'r', encoding='utf-8')
    # text = fin.read()
    # fin.close()

    summarize = jiagu.summarize(text, 4)  # 摘要
    # print(summarize)
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
    # print(time_str)
    # with open('A9/static/json/record.json', 'r', encoding='utf8') as fp:
    #     json_data = json.load(fp)
    # # print(json_data)
    #     json_content = []
    #     id = json_data["id"]
    #     title = json_data["title"]
    #     content = json_data["content"]
    #     ab = json_data["ab"]
    #     time=json_data["time"]
    #
    #     item_dict = {
    #         "id": id,
    #         "title": title,
    #         "time":time,
    #         "content": content,
    #         "ab": ab,
    #     }
    #
    # json_content.append(item_dict)
    # axis = {"axis": [22, 10, 33]}
    # json_content.append(axis)
    #
    # with open('A9/static/json/record.json', 'w') as f_new:
    #     json.dump(json_data, f_new)

    return summarize
