#encoding=utf-8
from __future__ import unicode_literals
import sys
# sys.path.append("../")
from AutoBUlidVocabulary import *

# # word_list=["哈士奇","狗子",'niub']
# vocab=Vocab()


# # vocab_list=vocab.get_vectorizer(word_list)
# # print(vocab_list)

# # vocab_list=vocab.add_vectorizer(word_list)
# # print(vocab_list)


# # c= vocab.text_voc_ids("饿猫饿喜欢而伟长吃饿而我热土什么")
# # print(c)

# # word_list=['n']
# text="哦哦喵星人真是太可爱了"
# word_list=list(text)
# vocab.add_vectorizer(word_list)

# print(vocab.load())


ids_list=GVocab(path='./test/').sentence_ids(" “哈士奇手机",text_len=100)

# text_list=['[CLS]']+text_list+['[SEP]']
# print(text_list)

# ids_list=GVocab(path='./test/').get(text_list)

print(ids_list)
