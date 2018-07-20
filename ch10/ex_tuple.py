# tuple
# packing and unpacking

# tuple은 list와 비슷하다.
# 다른점
#   - [] VS ()
#   - value의 추가, 수정, 삭제 못함.

t1 = (1, 2, 3)
# print(t1)
# print(t1[0])
# print(t1.get(0))  # get 함수 없음.

# t1[0] = 9  # 수정 안된다고 했잖아~ ㅋ
# t1.append(6)  # append 같은것도 없음.

# value 인자의 인덱스 값을 돌려줌.
# print(t1.index(1))

t2 = (3, 2, 3)
# print(t2[0])
# print(t2[1])
# print(t2[2])


# 슬라이싱
# print(t1[1:])
# print(t1[2:])
# print(t1[:1])
# print(t1[:2])


# 더하기
t3 = (5, 6)
t4 = (7, 8)
# t4 = [7, 8]

# print(t3 + t4)


# 곱하기
# print(t3 * 2)
# print(t3 * 3)


# packing
t5 = 10, 20
# unpacking
first_value, second_value = t5
print("first_value :", first_value)
print("second_value :", second_value)


# swap
# first_value와 second_value의 값을 바꾸자.
temp_value = first_value
first_value = second_value
second_value = temp_value
print("first_value :", first_value)
print("second_value :", second_value)


# swap (packing & unpacking)
first_value, second_value = second_value, first_value
print("first_value :", first_value)
print("second_value :", second_value)
