class 이어말하기_앞: 
    def __init__ (self,word):
        self.word=word
        

class 이어말하기_뒤 : 
    def __init__(self,first_word,second_word):
        self.second_word=second_word
        print(first_word,second_word) 

first= 이어말하기_앞("낮 말은 새가 듣고")
second = 이어말하기_뒤(first.word,"밤 말은 쥐가 듣는다") #first 의 word 객체가 second 객체의 매기변수로서 메세지를 전달한다.

