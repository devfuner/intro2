
print("+----------------------------------------------------------+")
print("|                      청기 백기 게임                      |")
print("+----------------------------------------------------------+")
print("| 진행자의 지시에 맞춰 깃발을 움직이세요.                  |")
print("| 진행자의 지시는 각 깃발에 대해 아래의 경우가 있습니다.   |")
print("| - 올려                                                   |")
print("| - 내려                                                   |")
print("| - 올리지마                                               |")
print("| - 내리지마                                               |")
print("| - 올리지말고 내려                                        |")
print("| - 내리지말고 올려                                        |")
print("|                                                          |")
print("| 조작법                                                   |")
print("| 청기 올리기 : R 버튼                                     |")
print("| 청기 내리기 : F 버튼                                     |")
print("| 백기 올리기 : U 버튼                                     |")
print("| 백기 내리기 : J 버튼                                     |")
print("+----------------------------------------------------------+")

print("> 게임이 시작합니다.")

result = "R"
print("> 청기 올려")

user_input = input("> ")

if result == user_input.upper():
    print("성공!")
else:
    print("실패!")


result = "F"
print("> 청기 내려")

user_input = input("> ")

if result == user_input.upper():
    print("성공!")
else:
    print("실패!")


result = "U"
print("> 백기 올려")

user_input = input("> ")

if result == user_input.upper():
    print("성공!")
else:
    print("실패!")


result = "J"
print("> 백기 내려")

user_input = input("> ")

if result == user_input.upper():
    print("성공!")
else:
    print("실패!")
