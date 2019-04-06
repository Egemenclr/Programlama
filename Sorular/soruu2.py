
# coding: utf-8

# In[80]:



def kelime_listesi(string):
    my_Words=[]
    kelimeler=string.split()
    for kelime in kelimeler:
        my_Words.append(kelime)
    liste=[]
    
    for i in range(len(my_Words)):
        kontrol=1
        for j in range(int(len(my_Words[i])/2)):
            if(my_Words[i][j] !=my_Words[i][len(my_Words[i])-j-1]):
                kontrol=0
                break
        if(kontrol==1):
            liste.append(my_Words[i])
    return liste

kelime_listesi("ege inceler efe anna kavak kfgdfgdfgk")

