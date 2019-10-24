import pickle
import os
class Vocab:
    def __init__(self,file='vectorizer.pk'):
        self.vocab_file = file
        pass
    def remove(self):
        if os.path.exists(self.vocab_file):
        #删除文件，可使用以下两种方法。
            os.remove(self.vocab_file)
        #os.unlink(my_file)
        else:
            print ('no such file:%s'%self.vocab_file)

    def bulid_vectorizer(self,sentences):
        """
        sentences=['生 的 小猫 也 爱吃 鸡蛋', '真是 好有爱 的 一对']
        word_dict  
        """

        word_list = " ".join(sentences).split()
        word_dict=self.add_vectorizer( word_list)
        # self.save(word_dict)
        return word_dict
    def save(self, word_dict):
        """
        保存词典
        """
        with open(self.vocab_file, 'wb') as fin:
        # pickle.dump(cv, fin)
            pickle.dump(word_dict, fin)
    def load(self):
        """
        加载词典
        """
        if os.path.exists(self.vocab_file):
        # 加载模型
            word_dict=pickle.load(open(self.vocab_file, "rb"))
            
        else:
            word_dict= {}
        return word_dict
    def add_vectorizer(self, text_arr):
        """
        添加新的字典元素
        """
        word_dict=self.load()
        word_arr=list(word_dict.keys())
        word_arr=word_arr+text_arr
        word_list = list(set(word_arr))
        word_dict = {w: i for i, w in enumerate(word_list)}
        self.save(word_dict)

        return word_dict

        

    def get_vectorizer(self, text_arr):
        """
        text_arr=['哈士奇','柯基犬']

        text_ids=[0, 8, 7, 4, 6, 1, 5, 6, 9, 2, 3]
        """
        if os.path.exists(self.vocab_file):
        # 加载模型
            word_dict=self.load()
        # print(vocabulary) 
        else:
            word_dict=self.bulid_vectorizer(text_arr)
        text_ids=[]
        for word in text_arr:
            try:
                text_ids.append(word_dict[word])
            except :
                word_dict=self.add_vectorizer([word])
                
                text_ids.append(word_dict[word]) 
        # print(word_dict)
        # print(text_ids)
        return text_ids
    def text_voc_ids(self,text):
    """
    逐字获取voc值
    """
    # print(list(a))
    word_list=list(text)
    vocab_list=self.get_vectorizer(word_list)
    # print(vocab_list)
    return vocab_list

# #测试代码
# text = "哈士奇 dam cat he 柯基犬"
# word_list = text.split()
# print('word_list',word_list)

# t = Vocab()
# ids = t.get_vectorizer(word_list)
# print(ids)



# sentences=['生 的 小猫 也 爱吃 鸡蛋', '真是 好有爱 的 一对']
# word_dict=t.bulid_vectorizer(sentences)
# print("word_dict",word_dict)

#  add_vectorizer(self, text_arr)