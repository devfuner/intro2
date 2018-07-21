# function

# 다영이가 헷갈리는 화면에 출력되는 것과 결과값으로 받는것 설명


def plus(a, b):  # 함수의 일반적인 형태
    return a + b


def return_10():  # 인자가 없는 함수
    return 10


def return_none():  # 반환값이 없는 함수
    pass


# def는 뭐지?
# 함수를 만들겠다는 예약어(키워드)

# sum_value는 sum(9, 5)의 결과값을 대입 받는다.
sum_value = plus(9, 5)
# print(sum_value)는 sum_value의 값을 화면에 출력한다.
print(sum_value)

# 결과값은 함수에서 리턴되는 값
# 또는 어떤 식의 계산된 결과값


# 함수의 결과값은 하나
# sum(a, b)를 실행하면 더해진 숫자 하나만 결과값으로 반환된다.

# 두개 혹은 그 이상 반환할 수 있을까?
def plus_and_multiply(a, b):
    return a + b, a * b  # 어디서 본 것 같지 않나?


two_values = plus_and_multiply(3, 5)
print(two_values)  # 결과값은?


# 아래로 쭉 내려보세요.















# 반환된 값은 tuple
one_value, two_value = plus_and_multiply(3, 5)
print(one_value)
print(two_value)
