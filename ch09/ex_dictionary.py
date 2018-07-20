# dictionary

order = {"청기 올려": "R", "청기 내려": "F",
         "백기 올려": "U", "백기 내려": "J"}

# 사전의 키만 가져온다.
keys = order.keys()

# for key in keys:
#     print(key)

# 사전의 값만 가져온다.
values = order.values()

# for value in values:
#     print(value)


# key는 변경되지 않는 값만을 사용할 수 있다.
# key는 중복된 값을 사용할 수 없다.
# value는 중복된 값을 사용할 수 있다.
order2 = {"청기 올려": "R",
          "청기 올려": "U",
          "청기 내려": "F",
          "청기 내려": "J"}

keys = order2.keys()

# for key in keys:
#     print(key)

values = order2.values()

# for value in values:
#     print(value)


order3 = {"청기 올려": "R",
          "청기 내리지말고 올려": "R",
          "청기 내려": "F",
          "청기 올리지말고 내려": "F",
          "백기 올려": "U",
          "백기 내리지말고 올려": "U",
          "백기 내려": "J",
          "백기 올리지말고 내려": "J"}

value = order3["청기 올려"]
# print(value)

value = order3["백기 내리지말고 올려"]
# print(value)

# value = order3[0]
# print(value)

value = order3.get(0)
# print(value)

value = order3.pop("백기 내리지말고 올려")
# print(value)

items = order3.items()
print(items)
print(type(items))

items2 = list(items)
print(items2)
print(type(items2))
