#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
from AutoBUlidVocabulary import Vocab

import jieba




def text_jieba(text,sequence_length):
    """
    分词
    固定长度
    """
    seg_list = jieba.cut(text)  # 默认是精确模式
    # print( len(seg_list))
    n_seg_list =[]
    for it in seg_list:
        n_seg_list.append(it)

    print(n_seg_list)
    seg_list=n_seg_list
    if len(seg_list)>sequence_length:
        seg_list=seg_list[:sequence_length]
    else:
        seg_list=seg_list+(sequence_length-len(seg_list))*['None']
            #   return " ".join(seg_list)
            
    return seg_list


def jieba_sentences(sentences,sequence_length):
  new_s=[]
  for s in sentences:
    new_s.append(text_jieba(s,sequence_length))
  print(new_s)
  return new_s


# 3 words sentences (=sequence_length is 3)
# sentences = ["我 喜欢 你", "he loves me", "she likes baseball", "i hate you", "sorry for that", "this is awful"]
sentences=["哈士奇，完美地契合了家里排行老二的性格。",
           "上面有大哥阿拉斯加罩着，二哈是无忧无虑爱冒险的孩子。",
           "下面又有一个比它小，万千宠爱于一身的萨摩，所以二哈没有机会被惯坏，它是个比较独立自主思考的孩子。",
           "制造业是立国之本、强国之基。",
           "70年砥砺奋进，我国已成为全世界唯一拥有全部工业门类的国家。",
           "新起点再出发，中国制造将迈向怎样的未来？央视网和您一起从总书记的有力话语中找寻答案。",
           ]
sequence_length=30
sentences_l =jieba_sentences(sentences,sequence_length)
print(sentences_l)

for word_list in sentences_l:

    # word_list=["哈士奇","狗子"]
    vocab=Vocab()
    vocab_list=vocab.vocab_list(word_list)
    print(vocab_list)