from typing import List 
def set_matrix_zero(arr:List=[]):
    zero_row_index = []
    zero_column_index = []

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                zero_row_index.append(i)
                zero_column_index.append(j)
    zero_row_index = set(zero_row_index)
    zero_column_index = set(zero_column_index)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i in zero_row_index or j in zero_column_index:
                arr[i][j] = 0
    return arr
                

if __name__=="__main__":
    arr = [[1,1,1],[1,0,1],[1,1,1]]
    print(arr)
    arr = set_matrix_zero(arr)
    print(arr)