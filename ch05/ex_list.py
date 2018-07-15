
number_list = [6, 2, 1, 9, 4, 7]
print(number_list)

# 인덱스 번호로 리스트에 들어있는 값을 가져올 수 있어요.
print(number_list[0])
print(number_list[3])

# 인덱스 번호로 해당 인덱스의 값을 변경 할 수 있어요.
number_list[2] = 4
print(number_list[2])

# append함수로 리스트에 값을 추가할 수 있어요.
number_list.append(99)
print(number_list)

# pop함수로 리스트의 마지막 값을 반환 받고 리스트에서는 삭제 할 수 있어요.
pop = number_list.pop()
print(pop)
print(number_list)
