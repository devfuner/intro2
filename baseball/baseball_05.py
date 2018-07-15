
print("+----------------------------------------------------------+")
print("|                      숫자 야구 게임                      |")
print("+----------------------------------------------------------+")
print("| 수비수가 고른 세자릿수를 맞춰보세요.                     |")
print("| 0에서 9까지 서로 다른 숫자이다. (같은 숫자 사용 금지)    |")
print("| 스트라이크 : 공격수가 제시한 숫자와 위치가 모두 맞을 경우|")
print("| 볼 : 공격수가 제시한 숫자는 맞고 위치가 틀릴 경우        |")
print("| 아웃 : 공격수가 제시한 숫자가 모두 틀릴 경우             |")
print("+----------------------------------------------------------+")

print("> 수비수가 고른 숫자")
numbers = [3, 2, 0]
print(numbers[0])
print(numbers[1])
print(numbers[2])

guess_numbers = []
print("> 첫 번째 숫자를 입력하세요.")
guess_numbers.append(int(input("prompt>")))
print("> 두 번째 숫자를 입력하세요.")
guess_numbers.append(int(input("prompt>")))
print("> 세 번째 숫자를 입력하세요.")
guess_numbers.append(int(input("prompt>")))

print("> 공격수가 고른 숫자")
print(guess_numbers[0])
print(guess_numbers[1])
print(guess_numbers[2])

if guess_numbers[0] == guess_numbers[1] \
        or guess_numbers[0] == guess_numbers[2] \
        or guess_numbers[1] == guess_numbers[2]:
    print("같은 숫자를 입력하면 안 됩니다.")
else:
    strike_count = 0
    ball_count = 0

    if guess_numbers[0] == numbers[0]:
        strike_count = strike_count + 1
    elif guess_numbers[0] == numbers[1] or guess_numbers[0] == numbers[2]:
        ball_count = ball_count + 1

    if guess_numbers[1] == numbers[1]:
        strike_count = strike_count + 1
    elif guess_numbers[1] == numbers[0] or guess_numbers[1] == numbers[2]:
        ball_count = ball_count + 1

    if guess_numbers[2] == numbers[2]:
        strike_count = strike_count + 1
    elif guess_numbers[2] == numbers[0] or guess_numbers[2] == numbers[1]:
        ball_count = ball_count + 1

    print("스트라이크 :", strike_count)
    print("볼 :", ball_count)
    print("아웃 :", 3 - strike_count - ball_count)
