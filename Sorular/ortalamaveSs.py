
# coding: utf-8

# In[295]:


import math
def ort(liste):
    toplam=0
    for i in (liste):
        toplam+=i
    return toplam/len(liste)
def ss(liste):
    farklarinkaresi=[]
    toplam=0
    for i in liste:
        farklarinkaresi.append((ort(liste)-i)**2)
    for i in farklarinkaresi:
        toplam+=i
    toplam/=len(liste)-1
    toplam=math.sqrt(toplam)
    return toplam
    


# In[296]:


liste_1=[1,2,3,4,5,6,7,8,9]
ss_ort(liste_1)
ss(liste_1)

