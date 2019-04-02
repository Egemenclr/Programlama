
# coding: utf-8

# In[43]:


import random
def fonk_1(m,n):
    my_list=[]
    for i in range(m):
        my_list.append([])
        for j in range(n):
            my_list[i].append(random.randint(1,10))
            
    return my_list

def fonk_1_print(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist[0])):
            print(mylist[i][j],end=" ")
            
def fonk_1_contvert_to_hash(mylist):
    my_dict={}
    for i in range(len(mylist)):
        for j in range(len(mylist[0])):
            my_dict[(i,j)]=mylist[i][j]
    return my_dict

def fonk_hash_print(hashlist):
    for item in hashlist:
        print(hashlist[item],end=" ")


# In[49]:


liste_1=fonk_1(3,3)
#fonk_1_print(liste_1)
b=fonk_1_contvert_to_hash(liste_1)

print(b,fonk_hash_print(b))

