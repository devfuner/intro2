
# 모듈
클래스, 함수, 변수등을 모아놓은 파일.  
파이썬 프로그램에서 사용할 수 있는 단위.  
논리적으로 공통적인 것들을 모아놓는다.  


#### import
모듈을 불러와서 사용할 수 있도록 하는 키워드

```python
import sys

print(sys.path)
```


### from sys import path
sys 모듈에서 path, exit만 불러와서 사용할 때
하나 이상을 불러올때는 ','로 구분한다.

```python
from sys import path, exit

print(path)
exit(0)
```


### * import
해당 모듈에 있는 모든 것을 불러오겠다는 것.

```python
from sys import *

print(path)
```


### __name__
실행되는 모듈의 이름을 가지고 있는 변수

```python
if __name__ == "__main__":
    print("모듈이 직접 실행되었음.")
```