
# coding: utf-8

# In[417]:


def toplam(matris):
    satir=[]
    sutun=[]
    size=len(matris)
    for i in range(size):
        for j in range(size):
            satir.append(0)
            sutun.append(0)
    for i in range(size):
        for j in range(size):
            satir[i]+=matris[i][j]
            sutun[i]+=matris[j][i]
    gecici=satir[0]
    counter=0
    gecicisutun=[]
    for i in range(size):
        if(gecici < satir[i]):
            gecici=satir[i]
            counter+=1
    gecici1=sutun[0]
    counter1=0
    for j in range(size):
        if(gecici1 < sutun[j]):
            gecici1=sutun[j]
            counter1+=1
    for k in range(size):
        gecicisutun.append([])
        gecicisutun[k]=matris[k][counter1]
    buyuk=gecici
    if(buyuk < gecici1):
        return gecicisutun
    else:
        return matris[counter]


# In[418]:


matris_1=[[1,2,3],[7,8,9],[4,5,6]]
toplam(matris_1)

