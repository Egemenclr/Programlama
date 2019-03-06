import random
def generate_array (n):
    array= []
    for i in range (n):
        array.append(random.randint(0,100))
    return array

def bubble_sort(array):
    for i in range (len(array)):
        for j in range (len(array)-1):
            if (array[j] > array[j+1]):
                array[j],array[j+1]= array[j+1],array[j]
    print(array)



def selection_sort (arr):
    for i in range (len(arr)-1):
        smallest =i
        for j in range (i+1,len(arr)):
            if (arr[j] < arr[smallest]):
                smallest = j
        arr[i],arr[smallest] = arr[smallest],arr[i]

