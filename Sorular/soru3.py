
# coding: utf-8

# In[163]:


import math
def fonk(text):
    cumleler=text.split(".")
    myWords=[]
    harfler=[]
    for kelimeler in cumleler:
        kelime=kelimeler.split()
        for x in kelime:
            myWords.append(x)
            
    my_dict={}
    for i in range(len(myWords)):
        for j in range(len(myWords[i])):
            my_dict[(i,j)]=myWords[i][j]
    return my_dict
def matris_olustur(my_tuple):
    size=math.sqrt(len(my_tuple))
    matris=[]
    for i in range(int(size)):
        matris.append([])
        for j in range(int(size)):
            matris[i].append(0)
    sayac=0 
    while(sayac<len(my_tuple)):
        for k in range(int(size)):
            for t in range(int(size)):
                matris[k][t]=my_tuple[(0,sayac)]
                sayac+=1
    return matris


# In[170]:


def arama(string,matrix):
    w=[]
    for i in string:
        w.append(i)
    size=len(matrix[0])
    for k in range(size):
        for t in range(size):
            if(w[t]!=matrix[k][t] 
                and w[t]!=matrix[t][k]
              and w[t]!=matrix[size-k-1][size-t-1]
              and w[t]!=matrix[size-t-1][size-k-1]):
                break
        else:
            print("var")


# In[171]:


a=fonk("egemeninc")
len(a)
b=matris_olustur(a)


# In[177]:


arama("ime",b)


# In[173]:


a=5
a

