# 对“键-值”对的遍历，
# 学习.items()，和 keys(), values()的使用
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    'age': '29',
    'size': '29',
    'address': 'hangzhou city',
}

'''
for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: " + value)
'''

'''
for feature, value in user_0.items():
    print(feature.title() + " is " + value.title() + ".")
'''
'''
for feature in user_0.keys():
    print(feature.title())
'''

# 在字典的遍历中，需要注意的是在重复的元素的遍历中，可以用set()来找出独一无二的元素

for value in set(user_0.values()):
    print(value.title())
