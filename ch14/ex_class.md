# CLASS

클래스 만드는법
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_deco_name(self):
        return self.deco()

    def deco(self):
        return "[" + self.name + "]"


my_class = MyClass("devfuner")
print(my_class.get_name())
```

클래스의 메서드는 첫번째 인자로 무조건 self를 받는다.
인스턴스 변수는 self.xxx로 사용한다.
인스턴스 메서드 self.xxx()로 사용한다.
