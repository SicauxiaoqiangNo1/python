# 字典列表， 将每一个字典嵌套到列表，通过逗号进行隔开
'''
alien_0 = {'color': 'red', 'point': '5'}
alien_1 = {'color': 'green', 'point': '6'}
alien_2 = {'color': 'pink', 'point': '7'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
'''

'''
# 现实中的字典是不值这么多的，我们自己自动生成
# 创建一个用于储存外星人的空列表
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', "point": '5', 'speed': 'slow'}
    aliens.append(new_alien)

# 只要显示前五个外星人字典
for alien in aliens[:5]:
    print(alien)
print("...")
# x显示一下，总共有多少个外星人
print('Total number of aliens：' + str(len(aliens)))
'''

'''
# 怎么实现对每一个外星人进行独立的修改，利用FOR语句
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', "point": '5', 'speed': 'slow'}
    aliens.append(new_alien)

# 利用FOR语句对前三个的外星人进行修改
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'high'
        alien['point'] = 20
for alien in aliens[0:5]:
    print(alien)
print('...')
'''

# 怎么在字典里面储存列表
# 储存披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}
print('Your order a ' + pizza['crust'] +
      '-crust pizza ' + 'with the following toppings：')
for topping in pizza['toppings']:
    print("\n", topping)
