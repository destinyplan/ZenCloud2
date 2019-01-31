# -*- coding: utf-8 -*-
from snownlp import SnowNLP

s1=SnowNLP('你真漂亮')
s2=SnowNLP('你说你是不是有毛病')
print(s1.sentiments)
print(s2.sentiments)

filetxt = open('./demo.txt',encoding='utf-8')
text=filetxt.readlines()
filetxt.close()
for line in text:
    print(line,end='------')
    s=SnowNLP(line)
    if s.sentiments>0.6:
        print('这是好评')
    else:
        print('这是差评')

# import jieba
# strlist = jieba.cut_for_search('利用目前的三个分词工具(jieba、snownlp、pynlpir)简单的实现了短文本的分词效果')
# print('/'.join(strlist))