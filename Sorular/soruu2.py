
# coding: utf-8

# In[80]:


def ayir(text):
    sentences=text.split(".")
    my_Words=[]
    for cumleler in sentences:
        kelimeler=cumleler.split()
        for i in kelimeler:
            my_Words.append(i)
    liste=[]
    for i in range(len(my_Words)):

        for j in range(int(len(my_Words[i])/2)):
            if(my_Words[i][j]!=my_Words[i][len(my_Words[i])-j-1]):  
                break
        else:
            liste.append(my_Words[i])
    return liste

ayir("egemen inceler.kavak.anna  efe.kflsdkask")

