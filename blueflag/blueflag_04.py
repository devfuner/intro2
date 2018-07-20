from random import randrange

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

order = {"청기 올려": "R", "청기 내려": "F",
         "청기 내리지말고 올려": "R", "청기 올리지말고 내려": "F",
         "백기 올려": "U", "백기 내려": "J",
         "백기 내리지말고 올려": "U", "백기 올리지말고 내려": "J"}

order_messages = list(order.keys())
success_count = 0

while True:
    random_index = randrange(len(order_messages))
    message = order_messages[random_index]

    print(">", message)
    result = order[message]

    user_input = input("> ")

    if "Q" == user_input.upper():
        print(success_count, "번 성공했네요.")
        print("게임을 종료합니다.")

        exit(0)

    if not result == user_input.upper():
        print(success_count, "번 성공했네요.")

        break

    success_count = success_count + 1

