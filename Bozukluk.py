
bozukluks=[1,5,10,21,25,50]
size=len(bozukluks)

def bozukluk(para, bozukluklar):
    liste = []
    adım=para
    for i in range(size):
        temp= []
        toplam = 0
        k = i
        while (toplam <= para and k >= 0):
            if (toplam + bozukluklar[k] <= para):
                toplam += bozukluklar[k]
                temp.append(bozukluklar[k])

            else:
                k -= 1
        if(len(temp) < adım):
            adım = len(temp)
            liste = temp
    return liste,adım
print(bozukluk(15, bozukluks))


def recursiveCoin(coinValueList, change, knownResults):
    minCoins = change

    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recursiveCoin(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
                
    return minCoins
