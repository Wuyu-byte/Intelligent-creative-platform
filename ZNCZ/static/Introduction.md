# 关于我们

本系统旨在打造一个基于人工智能语言模型的智能文字辅助系统，同时设计了完备的⽤户图形界⾯，提供注册和登录登出操作，简化了⽤户的操作。本系统能够⽣成与⽂章内容⾼度契合的、表现出⽂章⼤意的摘要，同时，根据摘要的⽣成结果，⽤不同种⽅法进⾏标题提取。在训练语料方面，拥有大约80%的新闻内语料，对于新闻领域的生成有着极佳的效果。此外，关键词提取，文本纠错等功能也能辅助文字工作者更好地完成工作。

**特别指出：由于本项目运行在腾讯云主机下，受限于2G的运存影响、CPU性能限制和模型偏大，导致在标题生成时的反应速度远远满于本地，为正常情况。**

**且为了方便用户，本系统所有的文本输入都可以使用直接输入文本和上传相关文件两个不同的方式。**

## 功能介绍

### 标题生成

标题生成功能是本系统的核心功能。该功能可以根据输入的文章内容，自动生成具有吸引力和概括性的标题，以吸引读者的注意力并准确地传达文章的主旨。

在生成标题时，系统会自动分析文章的关键词和句子，并结合一些常见的标题语言模式和规则，生成符合语法和逻辑规则的标题。同时，系统也会考虑标题的长度和可读性，以确保生成的标题易于阅读和理解。标题生成功能不仅可以帮助用户快速生成标题，还可以提高标题的品质和吸引力，从而吸引更多的读者。此外，对于那些需要写作或编辑文章的人来说，标题生成功能也可以作为一个创作灵感的来源，帮助他们更好地组织文章结构和内容，提高写作效率和质量。

该功能的实现基于NLP方向大语言预训练模型roBerta-wwm，通过经过了25w条新闻数据的训练，具体的训练数据如下：

![p9ndcPf.jpg](https://s1.ax1x.com/2023/04/24/p9ndcPf.jpg)

一篇文章，两个标题，样例如下：

![p9n0VpT.png](https://s1.ax1x.com/2023/04/24/p9n0VpT.png)

### 摘要提取

文章摘要功能是本系统的核心功能之一。通过使用自然语言处理技术，系统可以自动抽取文章中最重要的信息，并将其汇总成一个简洁的摘要，以便读者快速了解文章的主旨和重点。在生成文章摘要时，系统会自动分析文章中的各个段落和句子，识别出其中的关键词和句子，并从中提取出最重要的信息。除此之外，系统还会考虑文章的结构和逻辑关系，确保生成的摘要内容能够准确地反映文章的核心内容，同时尽可能简洁明了。

通过使用文章摘要功能，用户可以快速了解一篇文章的主要内容和要点，无需阅读整篇文章。这对于那些时间紧张或需要快速了解多篇文章的人来说非常有用。此外，对于那些需要写作或编辑文章的人来说，文章摘要功能也可以作为参考，帮助他们更好地组织文章结构和内容，提高写作效率和质量。

**我们根据用户不同的需要，给出三种不同长度的摘要供其选择。**

使用NLP领域流行的P、R值作为指标，相比其他中文分词器，本系统所用jiagu分词准确率和召回率表现优秀，哪怕是长文本，本系统依旧能快速应对，生成摘要。

| 分词器      | P            | R            |
| ----------- | ------------ | ------------ |
| Jieba       | 80.809       | 80.599       |
| HanLP       | 82.360       | 80.973       |
| SnowNLP     | 80.272       | 84.851       |
| FoolNLTK    | 83.117       | 86.953       |
| ***Jiagu*** | ***89.746*** | ***91.771*** |
| Pyltp       | 86.140       | 87.223       |
| THULAC      | 82.805       | 90.524       |

​																																																						**上表的结果以msr测试结果为例*

一篇文章，三类摘要，样例如下：

![p9n0mX4.png](https://s1.ax1x.com/2023/04/24/p9n0mX4.png)

### 关键字提取

该功能可以自动从文章中提取出最具代表性和重要性的关键词，并为用户提供有用的参考信息，帮助他们更好地理解文章的主题和内容。在提取关键字时，系统会通过自然语言处理技术分析文章的语言特征和上下文信息，自动识别出文章中最频繁出现的关键词。同时，系统也会考虑关键词的权重和相关性，以确保生成的关键词列表具有代表性和准确性。

通过使用关键字提取功能，用户可以更好地理解文章的主题和内容，并快速定位到感兴趣的关键词和概念。此外，关键字提取功能也可以作为文章索引和分类的依据，帮助用户更好地组织和管理文章。对于那些需要写作或编辑文章的人来说，关键字提取功能也可以作为一个创作灵感的来源，帮助他们更好地选择关键词和主题，提高写作效率和质量。

样例如下：

![p9n0G9K.png](https://s1.ax1x.com/2023/04/24/p9n0G9K.png)

### 文本纠错

该功能可以自动检测和纠正文章中的拼写错误、语法错误、标点符号错误等问题，提高文章的准确性和可读性。在进行文本纠错时，系统会通过自然语言处理技术分析文章的语言特征和上下文信息，自动识别出文章中的错误，并提供正确的修正建议。同时，系统也会考虑文章的语言风格和表达习惯，以确保生成的修正建议符合文章的整体风格和意图。（本系统的文本纠错主要体现在打错常用字方面，如：人才打成人材）

通过使用文本纠错功能，用户可以大大提高文章的质量和准确性，避免因为拼写错误和语法错误等问题影响文章的可读性和可信度。此外，文本纠错功能也可以作为一个学习和提高语言能力的工具，帮助用户识别和纠正自己的语言错误，提高写作水平和语言表达能力。

样例如下：

![p9n0s9f.png](https://s1.ax1x.com/2023/04/24/p9n0s9f.png)



