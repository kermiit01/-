def get_matrix(n,m,value):
    matrix=[]
    mas=[]
    for i in range(m):
        mas.append(value)
    for i in range(n):
        matrix.append(mas)
    print(matrix)
    return
get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)