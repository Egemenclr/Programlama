import random
def get_n_random_integer(n):
    #random.seed(100)
    numbers=[]
    for i in range(n):
        s=random.randint(-100,100)
        numbers.append(s)
    return numbers
def get_mean_for_n_integer(numbers):
    toplam=0
    kactane=0
    for sayi in numbers:
        toplam=toplam+sayi
        kactane=kactane+1
    return (toplam/kactane)
def get_std_for_n_integer(numbers):
    toplam=0
    kactane=0
    ortalama=get_mean_for_n_integer(numbers)
    
    for sayi in numbers:
        toplam=toplam+(sayi-ortalama)**2
        kactane=kactane+1
    var_1=toplam/(kactane-1)
    std_1=var_1**0.5
    return std_1
def normalizasyon(numbers):
    new_numbers=[]
    ortalama=get_mean_for_n_integer(numbers)
    standart_sapma=get_std_for_n_integer(numbers)
    
    for x in numbers:
        new_x=(x-ortalama)/standart_sapma
        new_numbers.append(new_x)
    return new_numbers

sayilar=get_n_random_integer(5)
ortalama=get_mean_for_n_integer(sayilar)
standart_sapma=get_std_for_n_integer(sayilar)
yeni_sayilar=normalizasyon(sayilar)
print("sayilar :",sayilar)
print("ortalama :",ortalama)
print("standart sapma :",standart_sapma)
print("yeni normalize edilmis liste :",yeni_sayilar)
def get_mean_one_std_neighbor_ratio(numbers):
    
    kactane=0
    toplamkacsayi=0
    
    ortalama=get_mean_for_n_integer(numbers)
    standart_sapma=get_std_for_n_integer(numbers)
    
    low=ortalama-standart_sapma
    high=ortalama+standart_sapma
    
    for x in numbers:
        toplamkacsayi=toplamkacsayi+1
        if(x>low and x<high):
            kactane=kactane+1
    return kactane/toplamkacsayi
sayilar1=get_n_random_integer(100)
print("komsu:",get_mean_one_std_neighbor_ratio(yeni_sayilar))
print("yeni sayilar:",get_mean_for_n_integer(yeni_sayilar))
print("yeni ortalama:",get_std_for_n_integer(yeni_sayilar))
def insertation(numbers):
    sayilar2=numbers
    
    lenght_1=len(sayilar2)
    print("sayilar2:",sayilar2)
    for i in range(1,lenght_1):
        for j in range(i,0,-1):
            if (sayilar2[j]):
                temp=sayilar2[j-1]
                sayilar2[j-1]=sayilar2[j]
                sayilar2[j]=temp
    print(sayilar2)
    return sayilar2
insertation(yeni_sayilar)