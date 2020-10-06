def init_matrix(rows):
    matrix = []

    for row in range(rows):
        temp = list(map(int, input().split(' ')))
        matrix.append(temp)

    return matrix


a_rows, a_cols = input().split()
matrix_a = init_matrix(int(a_rows))

b_rows, b_cols = input().split()
matrix_b = init_matrix(int(b_rows))

if a_rows == b_rows and a_cols == b_cols:
    print('they match')
else:
    print('ERROR')
