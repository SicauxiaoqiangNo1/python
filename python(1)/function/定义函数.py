'''
#注意区分实参和形参。在这里，username是属于形参，后面的sicauman是实参，需要用引号括起来
def greet_user(username):
    print("Hello. " + username.title() + "!")


greet_user('sicauman')
'''

# 位置实参的顺序很重要，当然也可以用关键词实参

'''
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')

# 在编写函数时，可以给每一个形参指定默认值，
# 注意的是：在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参
# 这可以让python正确地解读位置实参
# def describe_pet(animal_type, pet_name='sicauam')
# describe_pet('dog') #直接最简单地在函数调用时只提供小狗的名字
'''

# 返回值：函数并不是直接显示输出，它可以处理一些数据，并返回一个或者一组数值

'''
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
'''
# 添加一个middle_name，但是不是每一个人独有middle_name,可以用if else语句来区分
# 将middle_name作为一个可选实参，使其在没有实参的情况下依然可行，给middle_name指定一个默认值——空字符串

'''
def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
'''

# return的返回值可以返回任何类型的值,比如字典

'''
def build_person(first_name, last_name, age=''):
    person = {'first': 'first_name', 'last': 'last_name'}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
'''

'''
#while循环与函数结合
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

#这是一个无限循环
while True:
    print('\nPlease input your name:')
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHellO," + formatted_name + "!")
'''

'''
# 增加一个break语句，使while在合适的地方停止

def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First_name: ")
    if f_name == 'q':
        break
    l_name = input("Last_name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
'''

# 函数------------列表


def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
