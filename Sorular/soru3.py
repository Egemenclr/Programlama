
import math
def ayir(text):
    sentences=text.split(".")
    my_Words=[]
    for cumleler in sentences:
        kelimeler=cumleler.split()
        for i in kelimeler:
            my_Words.append(i)
    return my_Words
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
                matris[k][t]=my_Words[0][sayac]
                sayac+=1      
    return matris
def var_mi(matris,string):
    if(len(string)>3):
        return 
    else:
         w=[]
    for i in string:
        w.append(i)
    size=len(matris[0])
    for i in range(size):#satir
        for j in range(size): #sutun
            if(matris[i][j]!=w[j] 
              and matris[j][i]!=w[j]
              and matris[size-j-1][size-i-1]!=w[j]
              and matris[size-i-1][size-j-1]!=w[j]):
                break
        else:
            print("var")
words=ayir("egemeninc")
matrix=matris_olustur(words)
var_mi(matrix,"cni")
