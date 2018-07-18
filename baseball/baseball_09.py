# blueflag를 하고 난 이후에 진행할 내용

from random import *

print("+----------------------------------------------------------+")
print("|                      숫자 야구 게임                      |")
print("+----------------------------------------------------------+")
print("| 수비수가 고른 세자릿수를 맞춰보세요.                     |")
print("| 0에서 9까지 서로 다른 숫자이다. (같은 숫자 사용 금지)    |")
print("| 스트라이크 : 공격수가 제시한 숫자와 위치가 모두 맞을 경우|")
print("| 볼 : 공격수가 제시한 숫자는 맞고 위치가 틀릴 경우        |")
print("| 아웃 : 공격수가 제시한 숫자가 모두 틀릴 경우             |")
print("+----------------------------------------------------------+")

baseball_number_length = 3
numbers = []
index = 0

set_numbers = set()

while len(set_numbers) < baseball_number_length:
    set_numbers.add(randrange(0, 10))

numbers = list(set_numbers)
shuffle(numbers)

print("> 수비수가 고른 숫자")
for number in numbers:
    print(number)

guess_numbers = []
input_message = ["> 첫 번째 숫자를 입력하세요.", "> 두 번째 숫자를 입력하세요.", "> 세 번째 숫자를 입력하세요."]

while True:
    guess_numbers.clear()

    for i in range(baseball_number_length):
        print(input_message[i])
        guess_numbers.append(int(input("prompt>")))

    print("> 공격수가 고른 숫자")

    for i in range(baseball_number_length):
        print(guess_numbers[i])

    set_guess_numbers = set(guess_numbers)
    if len(set_guess_numbers) < 3:
        print("같은 숫자를 입력하면 안 됩니다.")

        continue

    if guess_numbers == numbers:
        print("정답입니다.")
        break

    strike_count = 0
    ball_count = 0

    for i in range(baseball_number_length):
        if guess_numbers[i] == numbers[i]:
            strike_count = strike_count + 1
        elif guess_numbers[i] in numbers:
            ball_count = ball_count + 1

    print("스트라이크 :", strike_count)
    print("볼 :", ball_count)
    print("아웃 :", baseball_number_length - strike_count - ball_count)

    if strike_count == baseball_number_length:
        print("정답입니다.")
        break
