alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25;
print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)


# 遍历操作
user_0 = {'username':'efermi',
                'first': 'enrico',
                'last':'fermi'}
for key,value in user_0.items():
        print('\nkey: ' + key)
        print('value: ' + value)

for name in user_0.keys():   # values()  都返回的是一个列表 可以直接用if进行判断元素是否在其中
        print(name +" "+ user_0[name].title())

# 数据结构之间可以相互嵌套！
