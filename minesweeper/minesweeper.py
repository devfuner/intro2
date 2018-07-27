
matrix = [['-', '-', '-', '*', '-'],
          ['-', '*', '-', '-', '-'],
          ['-', '-', '-', '-', '*'],
          ['-', '*', '-', '-', '-'],
          ['-', '-', '*', '-', '-']]

matrix_i_length = len(matrix)
matrix_j_length = len(matrix[0])


def mine_counter(row_index, column_index):
    """
    주변 9칸의 지뢰 갯수를 찾는 함수

    row_index = 2
    column_index = 2
    라고 가정했을 때 확인해야할 인덱스들
    
    (-1, -1) (-1, -) (-1, +1)
     (-, -1)  (2, 2)  (-, +1)
    (+1, -1) (+1, -) (+1, +1)

    """

    # 확인하려는 인덱스의 값이 지뢰일때는 바로 반환
    if matrix[row_index][column_index] == '*':
        return '*'

    # 확인할 인덱스 생성
    row = [row_index - 1, row_index, row_index + 1]
    column = [column_index - 1, column_index, column_index + 1]

    mine_count = 0

    for i in row:
        for j in column:
            if row_index == row and column_index == column:
                continue

            if 0 <= i < matrix_i_length and 0 <= j < matrix_j_length:
                # print("(", i, j, ")", end=", ")
                # print(matrix[i][j], end="")
                if matrix[i][j] == '*':
                    mine_count = mine_count + 1
        # print()
    return mine_count


# 지뢰 갯수 찾아서 설정
for i in range(matrix_i_length):
    for j in range(matrix_j_length):
        matrix[i][j] = mine_counter(i, j)


# 지뢰 출력
for i in range(matrix_i_length):
    for j in range(matrix_j_length):
        print("{0:>2}".format(matrix[i][j]), end="")
    print()
