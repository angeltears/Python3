magicians = ['alice', 'david', 'carolina']
for magician in magicians :
    print(magician.title() + ", that was a great trick ! ");
    print("I can't wait to see your next trick, " + magician.title() + '.\n');
print(" Thank you everyone, That was a  great magic show !")


for value in range(1, 5):
    print(value)

numbers = list(range(2, 11, 2)) 
print(numbers) 

squares = [value**2 for value in range(1, 11) ]
print(squares)
# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-1: ])
# 复制列表　如果用切片　提取副本创建一个新的列表
#  直接赋值　导致两个变量指向同一个列表
my_foods = ['pizza','falafel', 'carrot cake']
friend_foods = my_foods[:]
# friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods is :" + str(my_foods[:]))
print("friend favorite foods is: " + str(friend_foods[:]))
# 元组 不可以修改但是可以重新定义
dimensions = (200, 50)
print(str(dimensions))


