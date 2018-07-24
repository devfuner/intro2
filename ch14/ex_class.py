
# ch04 calc 참조
# 클래스를 사용하여 계산기 만들기


class Calc:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


calc = Calc(5, 2)

print("calc.sum() :", calc.sum())
print("calc.sub() :", calc.sub())
print("calc.mul() :", calc.mul())
print("calc.div() :", calc.div())
