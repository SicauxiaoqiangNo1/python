# 熟练地使用字典，去明白为何他们可以高效地模拟现实世界的情形
# 在python中，字典是一系列的 “键-值” 对。每一个“键” 都与一个值相关联。
'''
alien_0 = {'color': 'green', 'point': '5', 'size': '10px'}

print(alien_0['color'])
print(alien_0['point'])
print(alien_0['size'])
'''

'''
new_point = alien_0['point']
print("You just got " + str(new_point) + "point.")

print(alien_0)
alien_0['x_position'] = 32
alien_0['y-positoon'] = 21
print(alien_0)
'''

'''
alien_0 = {}
alien_0['color'] = 'red'
alien_0['point'] = 5
alien_0['size'] = '10cm'
print('the alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'pink'
print('the alien is ' + alien_0['color'] + '.')
'''

alien_0 = {'x_position': 23, 'y_position': 41, 'speed': 'medium'}
print("The original position is :" + str(alien_0['x_position']))
# 下面将外星人向右边移动
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x_position is " + str(alien_0['x_position']))

print(alien_0)
del alien_0['speed']
print(alien_0)
