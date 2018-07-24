
def minus1(a, b):
    return a - b


def minus2(a, b, c):
    return a - b - c


print("minus1(5, 2) :", minus1(5, 2))
print("__name__ :", __name__)

if __name__ == "__main__":
    print("main 실행중...")
    number1 = minus1(9, 1)
    number2 = minus2(9, 1, 2)

    print("number1 :", number1)
    print("number2 :", number2)

