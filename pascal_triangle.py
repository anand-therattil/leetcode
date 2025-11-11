def pascal_triangle(n):
    result = [] 
    for i in range(n):
        row = [1]*(i)
        for j in range(1,i-1):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result
    
if "__main__" == __name__:
    print(pascal_triangle(6))