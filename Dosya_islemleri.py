
# coding: utf-8


class myClass():
    def __init__(self,my_file=""):
        f=open("dosya.txt","r")
        myContent=f.read() # tüm iceriği al
        mySentences=myContent.split(".") # . lara ayır
        self.myWords=[]
        
        for sentence in mySentences:
            Words_In_the_sentence=sentence.split(" ") 
            for word_1 in Words_In_the_sentence:   #karakter isteseydi bi for daha 
                self.myWords.append(word_1)
        #print(self.myWords)
        
        
    def my_frequency_1(self):
        self.frekans_list={}
        for i in (self.myWords):
            if(i in self.frekans_list):
                self.frekans_list[i]+=1
            else:
                self.frekans_list[i]=1


    def my_frequency_2(self):
        self.frequency_list_2={}
        for i in range(len(self.myWords)-1):
            w_1,w_2=self.myWords[i],self.myWords[i+1]
            if(w_1,w_2) in self.frequency_list_2:
                self.frequency_list_2[w_1,w_2]+=1
            else:
                self.frequency_list_2[w_1,w_2]=1
    
    def write_frequency_1(self):
        for word_1 in self.frekans_list:
            print(word_1+ " "+str(self.frekans_list[word_1]))
    def write_frequency_2(self):
        for w_1 in self.frequency_list_2:
            print(str(w_1)+ " "+str(self.frequency_list_2[w_1]))       
    


