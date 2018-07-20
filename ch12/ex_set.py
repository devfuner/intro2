import random


# set
# 값의 중복을 허용하지 않는다.
# 값의 순서가 없다.
set1 = set([1, 2, 3])
set2 = set([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6])

print("set1 :", set1)
print("set2 :", set2)


# set에 값 추가하기
set1.add(4)
print("set1.add(4) :", set1)

set1.add(3)
print("set1.add(3) :", set1)


# set에 한번에 여러 값 추가하기
set1.update([4, 5, 6])
print("set1.update([4, 5, 6]) :", set1)

set3 = set()
print("set3 :", set3)

set3.update(set1)
print("set3.update(set1) :", set3)


# set에서 값 지우기
set1.remove(4)
print("set1.remove(4) :", set1)



# 교집합, 합집합, 차집합
set4 = set([1, 2, 3, 4, 5, 6])
set5 = set([4, 5, 6, 7, 8, 9])


# 교집합
print("교집합 & :", (set4 & set5))
print("교집합 intersection :", set4.intersection(set5))


# 합집합
print("교집합 | :", (set4 | set5))
print("교집합 union :", set4.union(set5))


# 차집합
print("차집합 - :", (set4 - set5))
print("차집합 difference :", set4.difference(set5))


set_numbers = set()

while len(set_numbers) < 3:
    set_numbers.add(random.randrange(0, 10))

print(set_numbers)
