#Alınan sayının asal çarpanları ve asal olup olmadığı
liste=[]
def prime(n):
    x=5
    for i in range(n):
        if(n%2==0):
            liste.append(2)
            n=n/2
        elif(n%3==0):
            liste.append(3)
            n=n/3
        elif(n%x==0):
            liste.append(x)
            n=n/x

        else:
            x+=2

    if(len(liste)==1):
        return "Asal"

    return liste

print(prime(49))


#Verilen listenin ardışık toplamlarının en büyüğü
liste2=[4,-3,2,-1,-2,6,-5]
maxx=liste2[0]
toplam=0
n=len(liste2)
for i in range(n):
    for j in range(i+1,n):
        #print(i,j)
        toplam=0
        for k in range(i,j+1):

            toplam+=liste2[k]
            if(toplam > maxx):
                maxx=toplam

        #print(toplam)
print("---")
print(maxx)
