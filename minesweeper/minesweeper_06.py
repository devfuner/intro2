"""
숙제
- 게임판의 크기를 지정하도록 변경
- 게임판의 크기에 따라 지뢰의 갯수 변경
- 지뢰 표시 기능 추가
- 지뢰의 위치를 저장한 리스트를 따로 사용하고 매트릭스는 하나만 사용하도록 수정
- 게임에 성공했을때 지뢰의 위치를 오픈한다.

"""
import sys
import time
import random


mines = []
matrix = []


def mine_counter(row_index, column_index):
    """
    주변 9칸의 지뢰 갯수를 찾는 함수

    row_index = 2
    column_index = 2
    라고 가정했을 때 확인해야할 인덱스들
    
    (-1, -1) (-1, -) (-1, +1)
     (-, -1)  (2, 2)  (-, +1)
    (+1, -1) (+1, -) (+1, +1)

    :param row_index:
    :param column_index:
    :return: mine count
    """

    # 확인하려는 인덱스의 값이 지뢰일때는 바로 반환
    if (row_index, column_index) in mines:
        return '*'

    # 확인할 인덱스 생성
    row = [row_index - 1, row_index, row_index + 1]
    column = [column_index - 1, column_index, column_index + 1]

    mine_count = 0

    for i in row:
        for j in column:
            if row_index == row and column_index == column:
                continue

            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                if (i, j) in mines:
                    mine_count = mine_count + 1
                else:
                    matrix[i][j] = '.'
    return mine_count


def view_matrix():
    """
    게임판 출력 함수
    :return: None
    """
    print("{0:>3}".format(' '), end="")
    for i in range(len(matrix[0])):
        print("{0:>2}".format(i+1), end="")
    print()

    for i in range(len(matrix)):
        print("{0:>3}".format(len(matrix[0]) * i + 1), end="")
        for j in range(len(matrix[0])):
            print("{0:>2}".format(matrix[i][j]), end="")
        print()


def end_game(user_input):
    """
    게임 종료 함수
    :param user_input: q or Q
    :return: None
    """
    if 'Q' == user_input.upper():
        print("게임을 그만합니다.")
        sys.exit(0)


def get_row_and_column(index):
    """
    선택한 값을 매트릭스의 인덱스 값으로 변환 해주는 함수
    :param index: 사용자가 선택한 칸의 값
    :return: (row, column)
    """
    index = index - 1
    row = index // len(matrix[0])
    column = index % len(matrix[0])
    return row, column


def found_mine_counter():
    """
    게임 성공 조건이 맞는지 확인하는 함수
    :return: None
    """
    plus_count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            value = matrix[i][j]
            if value == '+' or value == '?':
                plus_count = plus_count + 1

    return plus_count == len(mines)


def set_mines(length):
    """
    게임판에 지뢰를 심는 함수
    :param length: 게임판의 전체 칸 수
    :return: None
    """
    for i in random.sample(range(1, length + 1), length // 5):
        row_and_column = get_row_and_column(i)
        mines.append(row_and_column)


def set_matrix(row, column):
    """
    게임판을 생성하는 함수
    :param row: 게임판의 세로 크기
    :param column: 게임판의 가로 크기
    :return: None
    """
    matrix.clear()

    for i in range(row):
        temp_list = list()
        for j in range(column):
            temp_list.append('+')
        matrix.append(temp_list)


def set_mine_checker(index):
    """
    선택한 칸을 지뢰로 체크하는 함수
    :param index: 사용자가 선택한 칸의 값
    :return: None
    """
    i, j = get_row_and_column(index)
    matrix[i][j] = '?'


def open_mines():
    for i, j in mines:
        matrix[i][j] = '*'


def main():
    """
    지뢰찾기 게임의 메인 함수
    :return: None
    """
    start_time = time.time()

    while True:
        view_matrix()

        user_input = input('> ')

        end_game(user_input)

        if user_input.startswith('?'):
            set_mine_checker(int(user_input[1:]))
            continue

        i, j = get_row_and_column(int(user_input))
        mine_count = mine_counter(i, j)
        matrix[i][j] = mine_count

        if mine_count == '*':
            view_matrix()
            print("지뢰를 밟았습니다!")
            end_time = time.time()
            print(int(end_time - start_time), "초 경과")
            sys.exit(0)

        if found_mine_counter():
            open_mines()
            view_matrix()
            print("모든 지뢰를 찾았습니다.")
            end_time = time.time()
            print(int(end_time - start_time), "초 경과")
            sys.exit(0)


if __name__ == '__main__':
    print("지뢰찾기 게임~ 지뢰를 밟아봐!")
    print("선택하고 싶은 칸의 번호를 입력하세요.")
    print("지뢰 체크는 ?3 처럼 입력하세요.")

    print("게임판의 크기를 지정하세요.")
    print("(ex : M x N)")
    m = int(input("M > "))
    n = int(input("N > "))
    set_matrix(m, n)
    set_mines(m * n)
    # print(mines)

    main()
