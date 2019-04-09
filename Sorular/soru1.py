
# coding: utf-8

def fonk(text):
    mySentences=text.split(".")
    myWords=[]
    for cumle in mySentences:
        kelimeler=cumle.split(" ")
        for kelime in kelimeler:
            myWords.append(kelime)
            
    return myWords
def var_mi(myWords,string):
    
    if(string in myWords):
        return myWords.index(string),True
    else:
        return False
def index_listesi(myWords,string):
    my_list=[]
    for i in range(len(myWords)):
        
        if(string ==myWords[i]):
            my_list.append(i)
          
    return my_list

text1="Do you egemen know about egemen their egemen art project?” asked Amy. 'It’s about graffiti, I think,' said Tara. “They’re working on egemen it at the old house behind the egemen factory."
kelimeler=fonk(text1)
#kelimeler
#var_mi(kelimeler,"know")
string_listesi(kelimeler,"egemen")

