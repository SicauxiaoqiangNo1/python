# 文件的读取

with open('123.txt', encoding='utf-8') as f:
    contents = f.read()
    print(contents)
    f.close()
