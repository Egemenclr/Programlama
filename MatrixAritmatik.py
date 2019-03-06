matrix_1 = [[1,2,3],[4,5,6]]
matrix_2 = [[7,8,9],[10,11,12]]
matrix_3 = [[13,24,35,46],[37,48,59,61],[52,63,37,84]]

for row in matrix_1:
    for element in row :
        print(element,end=" ")
    print()

def matrix_addition(matrix1,matrix2):
    result = []
    for row in range (len(matrix1)):
        result.append([])
        for column in range (len(matrix1[0])):
            result[row].append(matrix1[row][column] + matrix2[row][column])
    return result

def matrix_substraction(matrix1,matrix2):
    result = []
    for row in range (len(matrix1)):
        result.append([])
        for column in range (len(matrix1[row])):
            result[row].append(matrix1[row][column] - matrix2[row][column])
    return result



def matrix_scalar_product(matrix1,alpha):
    result=[]
    for row in range (len(matrix1)):
        result.append([])
        for column in range (len(matrix1[row])):
            result[row].append(matrix1[row][column]*alpha)
    return result

def getColumn (matrix, col):
    liste = []
    for i in range (len(matrix)):
        liste.append(matrix[i][col])
    return liste


def my_vectors_inner_product (v,w):
    size = len(v)
    my_result = []
    for i in range (size):
        my_result.append(0)
    for i in range (size):
        my_result[i] = v[i]*w[i]
    t=0
    for i in range(size):
        t = t+my_result[i]
    return t


def multiply_matrix(matrix1,matrix2):
    result = []
    for row in range (len(matrix1)):
        result.append([])
        for column in range (len(matrix2[row])):
            tempMatrix = my_vectors_inner_product(matrix1[row],getColumn(matrix2,column))
            result[row].append(tempMatrix)
    return result


print(multiply_matrix(matrix_1, matrix_3))