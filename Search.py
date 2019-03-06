def binary_search(array,item):
    first = 0
    last = len(array) - 1
    found = False
    step = 0
    while first <= last and not found:
        step += 1
        midpoint = (first + last) // 2
        if (array[midpoint] == item):
            found = True
        else:
            if (item < array[midpoint]):
                last = midpoint - 1
            else:
                first = midpoint + 1
    print("step = ", step)
    return found, midpoint

def my_searchSelection(array):
    swap_sayisi = 0
    for i in range(len(array) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, i + 1):
            # print("location:",location,"  i:",i)
            if (array[location] > array[positionOfMax]):
                positionOfMax = location
        array[location]= array[positionOfMax]  # degistirme islemi
        array[positionOfMax]=array[location]
        swap_sayisi += 1
    return ("swap sayisi =", swap_sayisi)

array1 = [21,12,13,44,25,2,126]
print(my_searchSelection(array1))
print()
print(binary_search(array1,126))
print(array1)