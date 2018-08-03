import os

# 코드 1
f = open('untitle.txt', 'w')
f.close()

# 코드 2
# datas = ['dayoming', 'junheeee', 'devfuner']
# f = open('datas.txt', 'w')
# for data in datas:
#     f.write(data + "\n")
# f.close()

# 코드 3
# f = open('datas.txt', 'r')
# datas = f.read()
# f.close()
# print(datas)


# 코드 4
# f = open('datas.txt', 'r')
# while True:
#     line = f.readline()
#
#     if not line:
#         break
#     print(line)
# f.close()


# 코드 5
# f = open('datas.txt', 'r')
# for line in f.readlines():
#     print(line)
# f.close()


# 코드 6
# append_datas = ['python', 'django', 'crawler']
# f = open('datas.txt', 'a')
# for data in append_datas:
#     f.write(data)
# f.close()


# 코드 7
# with open('datas.txt', 'r') as f:
#     for line in f.readlines:
#         print(line)


# 코드 8
# file
file_exists = os.path.exists('datas.txt')
print(file_exists)

# dir
dir_exists = os.path.exists('D:\PycharmProjects\intro2\ch15')
print(dir_exists)


# 코드 9
# file
is_file = os.path.isfile('datas.txt')
print(is_file)

# dir
is_dir = os.path.isdir('D:\PycharmProjects\intro2\ch15')
print(is_dir)

