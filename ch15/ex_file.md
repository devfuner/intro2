# 파일 입출력

```python
f = open('untitle.txt', 'w')
f.close()
```

파일 열기 모드 설명  
r : 읽기모드 - 파일을 읽기만 할 때 사용  
w : 쓰기모드 - 파일에 내용을 쓸 때 사용  
a : 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용  


파일에 데이터 쓰기
```python
datas = ['dayoming', 'junheeee', 'devfuner']
f = open('datas.txt', 'w')
for data in datas:
    f.write(data + "\n")
f.close()
```


파일에서 데이터 읽기

- read() : 파일을 전부 읽어온다.
- readline() : 파일을 한줄만 읽어온다.
- readlines() : 파일의 각각의 줄을 리스트에 담아 돌려준다.

read()
```python
f = open('datas.txt', 'r')
datas = f.read()
f.close()

print(datas)
```

readline()
```python
f = open('datas.txt', 'r')
while True:
    line = f.readline()
    
    if not line:
        break
    print(line)
f.close()
```

readlines()
```python
f = open('datas.txt', 'r')
for line in f.readlines():
    print(line)
f.close()
```


기존 파일에 내용 추가 하기
```python
append_datas = ['python', 'django', 'crawler']
f = open('datas.txt', 'a')
for data in append_datas:
    f.write(data)
f.close()
```


with 사용하기
```python
with open('datas.txt', 'r') as f:
    for line in f.readlines:
        print(line)
```

with문은 close()를 자동으로 실행해 준다.


파일 또는 디렉토리가 있는지 없는지 확인하기
```python
import os

# file
file_exists = os.path.exists('datas.txt')
print(file_exists)

# dir
dir_exists = os.path.exists('../ch15')
print(dir_exists)
```


파일인지 디렉토리인지 확인하기
```python
import os

# file
is_file = os.path.isfile('datas.txt')
print(is_file)

# dir
is_dir = os.path.isdir('D:\PycharmProjects\intro2\ch15')
print(is_dir)

```
