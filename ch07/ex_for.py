number_list = [1, 2, 3, 4, 5]

# 리스트에 들어있는 값을 하나씩 i에 담아줘요.
for i in number_list:
    print(i)


# len() 함수에 대해서 검색해보세요.
# range() 함수에 대해서 검색해보세요.
# range(5)는 0부터 5-1 까지 연속된 숫자를 반환해줘요.
for i in range(len(number_list)):
    print(i)
    print(number_list[i])


# 5부터 10-1 까지 연속된 숫자를 반환해줘요.
for i in range(5, 10):
    print(i)

# 5부터 10-1 까지 2씩 증가하는 연속된 숫자를 반환해줘요.
for i in range(5, 10, 2):
    print(i)
