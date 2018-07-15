
# 조건문
if 5 > 3:
    print("참")
else:
    print("거짓")


num = 5

if num > 3:
    print("참")
elif num == 5:
    print("같다")
else:
    print("거짓")

# 비교연산자
# < > <= >= == !=
print("10 > 10 은", 10 > 10)
print("10 >= 10 은", 10 >= 10)
print("5 < 10 은", 5 < 10)
print("5 <= 10 은", 5 <= 10)
print("5 == 4 은", 5 == 4)
print("5 != 4 은", 5 != 4)

# 논리연산자
# and, or, not

# noinspection PyChainedComparisons
if num > 1 and num < 10:
    print("참")

# 파이썬에서는 위의 조건식을 아래와 같이 표현 할 수 있어요.
if 1 < num < 10:
    print("참")

num1 = 5
num2 = 10
if num1 > 3 or num2 > 5:
    print("참")

if not num == 5:
    print("참")
