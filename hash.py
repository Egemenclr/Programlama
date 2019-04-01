
# coding: utf-8

# In[32]:


import random
def createMyHash(n):
    #n should be prime
    myTable=[]
    for i in range(n):
        myTable.append(0)
    return myTable

def my_hash(size,numberToBeInserted):
    return numberToBeInserted%size

def insert(myTable,numberToBeInserted):
    isCollision=False
    index=my_hash(len(myTable),numberToBeInserted)
    if(myTable[index]==1):
        isCollision=True
    else:
        myTable[index]=1
        
    return isCollision

def test(size=13,numberToBeInserted=10):
    m_h_1=createMyHash(size)
    c=0
    for s in range(numberToBeInserted):
        number=random.randint(0,1000)
        if(insert(m_h_1,number)==True):
            c=c+1
    return c

test(203,50)

