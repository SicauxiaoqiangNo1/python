# with open打开文件一直失败，尝试用写入方式创建文件

file_name = 'test.txt'


with open(file_name, 'w') as f_obj:
    f_obj.write("This is a test sentence!")

