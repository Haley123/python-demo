#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
python除了之前介绍的基础数据类型（整数、浮点数、字符串），还有特殊数据类型（列表、元组、字典），下面一一介绍

list：列表 -> 有序集合，可随时添加和修改元素,如['1','2']
tuple:元组 -> 有序列表，初始化后不允许修改,如('1','2')
dict：字典 -> 以键-值(key-value)存储,比长列表更快捷

'''

# 演示阶段
# 1、list
name = ['Tom', 'Bob', 'pasca']   # 定义列表
print(name)  # 输入列表
print(name[0])   # 可以根据索引（列表个数，从0开始），输出某个指定的元素

name.append('News')  # 1、使用append(object)添加列表元素，这里添加是到原列表末尾
print(name)

name.insert(0, 'Qiniu')   # 2、使用insert(index, object)插入某个元素到指定索引处
print(name)

name.pop(4)    # 3、使用pop(index)删除指定的索引,不指定默认删除末尾元素，
print(name)

name[0] = 'qiniu'  # 4、使用这种方式可直接赋值替换索引位置的元素
print(name)

name[0] = ['qiniu1', 'qiniu2']  # 5、列表可以嵌套列表，如[['qiniu1', 'qiniu2'], 'Tom', 'Bob', 'pasca']
print(name)

mark = ['1', '2', '3']
new = []
new = mark + name     # 6、列表组合，直接用+
print(new)

print(len(new))  # 7、len(）计算列表长度

for i in new:print(i)    # 8、利用for循环输出所有的列表元素

# list 总结和拓展

'''
方法大全：
list.append(obj)     在列表末尾添加新的对象
list.count(obj)      统计某个元素在列表中出现的次数
list.extend(seq)     在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)      从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)  将对象插入列表
list.pop([index=-1])     移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)      移除列表中某个值的第一个匹配项
list.reverse()        反向列表中元素
list.sort(cmp=None, key=None, reverse=False)   对原列表进行排序
'''

# 2、tuple   备注：元组不可修改
tuple1 = ('Tom', 'Bob', 'pasca')
tuple2 = (1, 2, 3)

print(tuple1, tuple2)  # 1、输出元组

tuple3 = ()
tuple3 = tuple1+tuple2  # 不可修改，但是可+拼接，del删除
print(tuple3)
'''
tuple(seq)   将列表转换为元组。
len((1, 2, 3))	  计算元素个数

'''

# 3、dict 字典
'''
特点1：字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 
特点2：不允许同一个键出现两次，可被覆盖
特点3：键(key)不可变，so列表不可充当元素，其他皆可，而values可变，所有列表也行
'''
dict1 = {
    'name': 'pasca',
    'years': '21',
    'Career': 'it'
}
dict2 = {
    'height': 180
}
print(dict1)           # 1、输出字典
print(dict1['name'])   # 2、输出字典的对应的key值
print(dict1.keys())    # 3、输出字典所有的keys
print(dict1.values())  # 4、输出字典的所有values
print(dict1.items())   # 5、列表形式输出
dict1.update(dict2)
print(dict1)           # 6、字典合并

dict1['years'] = 22     #指定keys修改values值
dict1['company'] = 'qiniu'  # 直接添加没有的key=>value
print(dict1)
print(str(dict1))



'''
dict语法 拓展和总结：
1、len(dict)      计算长度
2、str(dict)      输出以字符串形式
3、dict.clear()   删除字典内所有元素
  dict.pop(key[,default])   删除某个指定的key:value
  dict.del(key[,default])   删除某个指定的key:value
  
4、dict.get(key, default=None)  返回指定键的值，如果值不在字典中返回default值
5、dict.has_key(key)            如果键在字典dict里返回true，否则返回false
6、dict.items()                 以列表返回可遍历的(键, 值) 元组数组
7、dict.update(dict2)           把字典dict2的键/值对更新到dict里

'''