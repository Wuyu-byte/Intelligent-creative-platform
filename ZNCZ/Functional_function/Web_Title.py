# -*- coding: utf-8 -*-
import torch
from bert_seq2seq import Tokenizer, load_chinese_base_vocab
from bert_seq2seq import load_bert

auto_title_model = "ZNCZ\\model_trained\\roberta_auto_title.bin"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def autotitle(text):
    vocab_path = "ZNCZ\\model_trained\\roberta_vocab.txt"  # roberta模型字典的位置
    model_name = "roberta"
    # 加载字典
    word2idx = load_chinese_base_vocab(vocab_path)
    # 定义模型
    bert_model = load_bert(word2idx, model_name=model_name)
    bert_model.set_device(device)
    bert_model.eval()
    bert_model.load_all_params(model_path=auto_title_model, device=device)

    with torch.no_grad():
        name = bert_model.generate(text, beam_size=3)
    print('预测标题:', name)

    return name
