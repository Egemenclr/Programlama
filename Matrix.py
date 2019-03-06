def det_from_2_by_2(m1):
    s_1=m1[0][0]*m1[1][1]
    s_2=m1[0][1]*m1[1][0]
    s_3=s_1-s_2

    return s_3

def delete_row_col_from_matrix(m1,m,n):
    result=[]
    size_1=len(m1)
    size_2=len(m1[0])
    for i in range(size_1):
        if(i==m):
            continue
        row_1=[]
        for j in range(size_2):
            if(j==n):
                continue
            row_1.append(m1[i][j])
        result.append(row_1)
    return result
def det_from_3_by_3(m1):
    a=m1[0][0]*det_from_2_by_2(delete_row_col_from_matrix(m1,0,0))
    b=m1[0][1]*det_from_2_by_2(delete_row_col_from_matrix(m1,0,1))
    c=m1[0][2]*det_from_2_by_2(delete_row_col_from_matrix(m1,0,2))
    return a-b+c

matris1=[[1,2,3],[4,5,6],[7,8,10]]
print(det_from_3_by_3(matris1))