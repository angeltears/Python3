# sort排序　sorted临时排序　sort(reverse = True) 倒序排序　
# reverse 倒置
# len  长度
# pop 弹出(有返回值) 可以在参数列表中带下标　默认列表尾
# del 下标
# remove 元素名
# insert 插入　append追加到列表尾
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print("len = " + str(len(bicycles)))
bicycles.sort()
print(bicycles)
bicycles.sort(reverse = True)
print(bicycles)
print(sorted(bicycles))
bicycles.reverse();
print(bicycles)
bicycles.append("ducati")
print(bicycles)
bicycles.insert(0, "suzuki")
print(bicycles)
del bicycles[0]
print(bicycles)
pop_name = bicycles.pop()
print(bicycles)
print(pop_name)
pop_name = bicycles.pop(2)
print(bicycles)
print(pop_name)
bicycles.remove('trek')
print(bicycles)
