def init_matrix(rows):
    matrix = []

    for row in range(rows):
        temp = list(map(int, input().split(' ')))
        matrix.append(temp)

    return matrix


def add_matrix():
    a_rows, a_cols = input().split()
    matrix_a = init_matrix(int(a_rows))

    b_rows, b_cols = input().split()
    matrix_b = init_matrix(int(b_rows))

    if a_rows == b_rows and a_cols == b_cols:
        result = [[matrix_a[row][col] + matrix_b[row][col] for col in range(len(matrix_a[0]))] for row in range(len(matrix_a))]
        [print(' '.join(map(str, result[row]))) for row in range(len(result))]
    else:
        print('ERROR')


# def multiply_matrix():
m_rows, m_cols = input().split()
temp_matrix = init_matrix(int(m_rows) + 1)
matrix_m = temp_matrix[:-1]
constant = temp_matrix[-1]

multiply_result = [[matrix_m[row][col] * constant[0] for col in range(len(matrix_m[0]))] for row in range(len(matrix_m))]
[print(' '.join(map(str, multiply_result[row]))) for row in range(len(multiply_result))]
