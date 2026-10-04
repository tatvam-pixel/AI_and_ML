
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

    row_mean = []
    if mode == 'row':
        for i in matrix:
            row_mean.append(sum(i) / len(i))
        return row_mean

    column_mean = []
    total = 0
    length = len(matrix)
    elem = 0
    i = 0

    if mode == 'column':
        while elem < len(matrix[0]):
            total += matrix[i][elem]

            if i == len(matrix) - 1:
                column_mean.append(total / length)
                total = 0
                elem += 1
                i = 0
            else:
                i += 1

        return column_mean

    return []
