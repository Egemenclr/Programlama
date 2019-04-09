
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
def matris_olustur(my_Words):
    matris=[]
    size=int(math.sqrt(len(my_Words[0])))
    for i in range(size):
        matris.append([])
        for j in range(size):
            matris[i].append(0)
    sayac=0
    if(sayac!=size-1):
        for k in range(size):
            for t in range(size):
                print(k,t,sayac)
                matris[k][t]=my_Words[0][sayac]
                sayac+=1
            
    return matris
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
a=fonk("egemeninc")
b=matris_olustur(a)
arama("ime",b)


