def read_matrix_func():
    number_of_rows = int(input())
    current_matrix = []

    for row in range(number_of_rows):
        row_data = list(map(int, input().split()))
        current_matrix.append(row_data)

    return current_matrix


def get_primary_diagonal_sum(my_matrix):
    sum_of_primary_diagonal = [my_matrix[i][i] for i in range(len(my_matrix))]
    return sum(sum_of_primary_diagonal)

def get_secondary_diagonal_sum(my_matrix):
    sum_of_secondary_diagonal = 0
    for i in range(len(my_matrix) -1, -1, -1):
        sum_of_secondary_diagonal += my_matrix[i][(len(my_matrix)-1) - i]
    return sum_of_secondary_diagonal


matrix = read_matrix_func()

print(get_primary_diagonal_sum(matrix))
print(get_secondary_diagonal_sum(matrix))